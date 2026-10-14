from enum import Enum
from collections.abc import Callable

from fastapi import Depends, HTTPException, status

from Backend.auth.dependencies import get_current_user


class Role(str, Enum):
    """Application-wide roles used for access control."""

    ADMIN = "admin"
    PROJECT_MANAGER = "project_manager"
    DEVELOPER = "developer"


def normalize_role(role: str | None) -> str | None:
    """Normalize a stored role without granting elevated privileges."""
    if not isinstance(role, str):
        return None

    normalized = role.strip().lower()
    valid_roles = {item.value for item in Role}

    if normalized in valid_roles:
        return normalized

    # Legacy users retain developer-level access, never elevated privileges.
    if normalized == "member":
        return Role.DEVELOPER.value

    return None

def require_role(*allowed_roles: Role) -> Callable:
    """Create a dependency that allows only the specified application roles."""

    def role_checker(
        current_user: dict = Depends(get_current_user),
    ) -> dict:
        user_role = normalize_role(current_user.get("role"))

        allowed_values = {role.value for role in allowed_roles}

        if user_role not in allowed_values:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action.",
            )

        return current_user

    return role_checker
