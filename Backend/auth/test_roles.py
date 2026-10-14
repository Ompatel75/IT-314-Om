
import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from Backend.auth.dependencies import get_current_user
from Backend.auth.roles import Role, require_role


app = FastAPI()


@app.get("/admin")
def admin_route(user: dict = Depends(require_role(Role.ADMIN))):
    return {"user": user["name"]}


@app.get("/project")
def project_route(
    user: dict = Depends(
        require_role(Role.ADMIN, Role.PROJECT_MANAGER)
    ),
):
    return {"user": user["name"]}


client = TestClient(app)


@pytest.fixture
def user_role():
    def override(role):
        app.dependency_overrides[get_current_user] = lambda: {
            "name": "Test User",
            "role": role,
        }

    yield override
    app.dependency_overrides.clear()


def test_admin_allowed_for_admin_route(user_role):
    user_role("admin")
    response = client.get("/admin")
    assert response.status_code == 200


def test_developer_denied_admin_route(user_role):
    user_role("developer")
    response = client.get("/admin")
    assert response.status_code == 403


def test_project_manager_allowed_project_route(user_role):
    user_role("project_manager")
    response = client.get("/project")
    assert response.status_code == 200


def test_developer_denied_project_route(user_role):
    user_role("developer")
    response = client.get("/project")
    assert response.status_code == 403


def test_unknown_role_denied_admin_route(user_role):
    user_role("unknown")
    response = client.get("/admin")
    assert response.status_code == 403

