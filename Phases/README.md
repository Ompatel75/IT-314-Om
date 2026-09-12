# AI Software Project Health & Risk Analyzer
## Software Engineering Project — Phase-Wise Development Document

> **Project Goal:** Build a software project management platform that analyzes Git repositories, issues, pull requests, commits, and sprint activity to evaluate project health. GenAI identifies development bottlenecks, overloaded team members, stale issues, schedule risks, and generates project status reports with actionable recommendations.

> **Course Process:** The project must follow the **Agile (SCRUM) methodology throughout development**. The course instructions require stakeholder identification, requirement elicitation, application of elicitation techniques, user stories/product backlog, EPICs and Sprints, conflict identification/resolution, and the start of Sprint 1 with a concept poster.

---

## Table of Contents

- [Phase 0 — Project Understanding & Setup](#phase-0--project-understanding--setup)
- [Phase 1 — Identify Stakeholders and End Users](#phase-1--identify-stakeholders-and-end-users)
- [Phase 2 — Identify Requirement Elicitation Techniques](#phase-2--identify-requirement-elicitation-techniques)
- [Phase 3 — Apply Elicitation Techniques](#phase-3--apply-elicitation-techniques)
- [Phase 4 — Requirements Engineering](#phase-4--requirements-engineering)
- [Phase 5 — User Stories & Product Backlog](#phase-5--user-stories--product-backlog)
- [Phase 6 — EPICs & Sprint Planning](#phase-6--epics--sprint-planning)
- [Phase 7 — Identify & Resolve Requirement Conflicts](#phase-7--identify--resolve-requirement-conflicts)
- [Phase 8 — Sprint 1 & Concept Poster](#phase-8--sprint-1--concept-poster)
- [Phase 9 — System Architecture & Technical Planning](#phase-9--system-architecture--technical-planning)
- [Phase 10 — Development](#phase-10--development)
- [Phase 11 — Testing & Validation](#phase-11--testing--validation)
- [Phase 12 — Deployment & Final Demonstration](#phase-12--deployment--final-demonstration)
- [Phase 13 — Documentation & Evidence](#phase-13--documentation--evidence)
- [Phase 14 — Final Readiness Checklist](#phase-14--final-readiness-checklist)

---

# Phase 0 — Project Understanding & Setup

## Objective

Establish a common understanding of the problem, define the project's scope, and create the team's working environment before implementation begins.

## What the system should do

The system will:

1. Connect to a GitHub repository.
2. Collect relevant repository/project-management activity through APIs.
3. Store or cache useful project data.
4. Calculate project-health metrics.
5. Identify project risks and bottlenecks.
6. Use GenAI to explain important findings and generate recommendations.
7. Present the results through a web dashboard.
8. Generate a project status report.

## Resource Constraints

The implementation should be designed around:

- Free Vercel hosting for the frontend.
- A free-tier backend.
- Only free/limited API calls; no assumption of unlimited API usage.
- No dedicated GPU.
- No requirement to train a large language model.
- API-first GitHub data collection rather than cloning/analyzing an entire repository unnecessarily.
- Caching and metric aggregation before sending data to an LLM.

## Suggested High-Level Architecture

```text
User
  |
  v
Frontend (Vercel)
  |
  v
Backend API
  |
  +------------------+-------------------+
  |                  |                   |
  v                  v                   v
GitHub API       Database/Cache        LLM API
  |                  |                   |
  +------------------+-------------------+
                     |
                     v
             Metrics / Risk Engine
                     |
                     v
             AI Insights & Report
                     |
                     v
                Dashboard
```

## Checkpoints

- [ ] Read and understand the project problem.
- [ ] Agree on the project scope.
- [ ] Define what is inside the MVP.
- [ ] Define what is explicitly out of scope.
- [ ] Create the team's GitHub repository.
- [ ] Add every team member as a contributor.
- [ ] Create the team's Slack workspace/channels.
- [ ] Decide the Scrum cadence and responsibilities.
- [ ] Create the initial project README.

**Deliverables**
- Project scope
- Initial architecture
- GitHub repository
- Slack workspace
- Initial README

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 1 — Identify Stakeholders and End Users

## Objective

Identify everyone who has a stake in the system or interacts with it.

The course specifically requires groups to list stakeholders and end users, including users, administrators, and relevant third parties.

## Recommended Stakeholders

| Stakeholder | Role in the system | Main interest |
|---|---|---|
| Project Manager | Main user | Project health, risks, reports |
| Team Lead | Main user | Workload, bottlenecks, PR activity |
| Developer | End user | Assigned work, project status |
| Product Owner | Stakeholder/user | Progress and delivery risks |
| Repository Administrator | Administrator | GitHub integration/access |
| Client/Instructor | External stakeholder | Project status and outcomes |
| Development Team | Builders/operators | Requirements and technical feasibility |

> The final stakeholder list should be validated using your actual project context and elicitation activities.

## Questions to answer

- Who will use the dashboard?
- Who provides repository access?
- Who needs project reports?
- Who benefits from risk detection?
- Who is affected by incorrect analysis?
- Who can approve or change requirements?
- Who is responsible for the GitHub repository?

## Checkpoints

- [ ] List all primary stakeholders.
- [ ] List all end users.
- [ ] List administrators.
- [ ] Identify external/third-party stakeholders.
- [ ] Record each stakeholder's goals and concerns.
- [ ] Validate the stakeholder list with the team.
- [ ] Finalize the stakeholder table.

**Deliverable**
- Stakeholder Analysis Document

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 2 — Identify Requirement Elicitation Techniques

## Objective

For every important stakeholder, choose one or more requirement-elicitation techniques and justify why the technique fits.

## Recommended Techniques

### 1. Interview

Useful for:
- Project Manager
- Team Lead
- Product Owner

Purpose:
- Understand decision-making needs.
- Discover pain points.
- Discover reporting requirements.

### 2. Survey

Useful for:
- Developers
- Larger groups of potential users

Purpose:
- Collect preferences efficiently.
- Rank desired features.
- Identify common problems.

### 3. Observation

Useful for:
- Development teams
- Team leads

Purpose:
- Observe how GitHub issues, PRs, and sprint work are currently handled.

### 4. Brainstorming

Useful for:
- Project team
- Stakeholder workshops

Purpose:
- Discover possible features and AI use cases.

### 5. Document Analysis

Useful for:
- Existing project-management documents
- GitHub repositories
- Sprint documents
- Existing reports

Purpose:
- Identify existing workflows and domain requirements.

## Example Technique Mapping

| Stakeholder | Technique | Why |
|---|---|---|
| Project Manager | Interview | Captures detailed reporting/risk needs |
| Team Lead | Interview + Observation | Reveals workflow and bottlenecks |
| Developer | Survey + Observation | Captures practical development needs |
| Product Owner | Interview | Clarifies delivery and reporting goals |
| Administrator | Interview | Identifies access/integration constraints |
| Existing GitHub data | Document Analysis | Reveals project/domain information |

## Checkpoints

- [ ] Select elicitation techniques.
- [ ] Map each technique to stakeholders.
- [ ] Write justification for every technique.
- [ ] Prepare interview questions.
- [ ] Prepare survey questions.
- [ ] Prepare observation/document-analysis plan.
- [ ] Review the plan with the team.

**Deliverable**
- Requirement Elicitation Plan

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 3 — Apply Elicitation Techniques

## Objective

Actually collect requirements. Do not stop at describing the techniques.

The collected information should cover:

- Functional requirements
- Non-functional requirements
- Domain requirements

## Example Interview Questions

### Project Manager

1. How do you currently monitor project health?
2. Which indicators help you detect project delays?
3. How do you identify overloaded developers?
4. What should a weekly project report contain?
5. How frequently should project data be refreshed?

### Team Lead

1. How do you identify PR bottlenecks?
2. How do you handle stale issues?
3. How do you distribute tasks?
4. Which metrics indicate an unhealthy project?

### Developer

1. Which dashboard information is useful during a sprint?
2. What project information is difficult to find?
3. What kind of recommendations would actually help developers?

## Survey Areas

Possible survey dimensions:

- Most useful metrics
- Preferred dashboard information
- Importance of PR analysis
- Importance of issue aging
- Importance of workload analysis
- Usefulness of AI recommendations
- Preferred report format

## Observation Areas

Observe:

- GitHub issue workflow
- Pull-request workflow
- Code-review workflow
- Sprint planning
- Task assignment
- Progress tracking
- Reporting process

## Evidence to Keep

- Interview questions and answers
- Survey questions/results
- Observation notes
- Brainstorming outcomes
- Documents analyzed
- Decisions made from collected evidence

## Checkpoints

- [ ] Conduct interviews.
- [ ] Conduct survey.
- [ ] Perform observation where applicable.
- [ ] Analyze relevant documents.
- [ ] Record findings.
- [ ] Consolidate duplicate requirements.
- [ ] Convert findings into requirement candidates.
- [ ] Confirm important findings with stakeholders.

**Deliverable**
- Elicitation Evidence + Findings Document

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 4 — Requirements Engineering

## Objective

Transform elicitation findings into clear, testable requirements.

---

## 4.1 Functional Requirements

Functional requirements describe what the system must do.

### Initial examples

| ID | Requirement |
|---|---|
| FR-01 | The system shall allow a user to connect a GitHub repository. |
| FR-02 | The system shall validate the repository information. |
| FR-03 | The system shall retrieve repository activity through GitHub APIs. |
| FR-04 | The system shall retrieve issue information. |
| FR-05 | The system shall retrieve pull-request information. |
| FR-06 | The system shall retrieve contributor activity. |
| FR-07 | The system shall calculate project-health metrics. |
| FR-08 | The system shall identify stale issues. |
| FR-09 | The system shall identify PR bottlenecks. |
| FR-10 | The system shall estimate contributor workload imbalance. |
| FR-11 | The system shall identify project risks. |
| FR-12 | The system shall generate AI-based project insights. |
| FR-13 | The system shall generate actionable recommendations. |
| FR-14 | The system shall generate a project status report. |
| FR-15 | The system shall display project metrics in a dashboard. |

> These are starter examples. Final requirements must be derived and validated through elicitation.

---

## 4.2 Non-Functional Requirements

Examples:

| ID | Requirement |
|---|---|
| NFR-01 | The system should provide a responsive web interface. |
| NFR-02 | The system should handle invalid API responses gracefully. |
| NFR-03 | The system should minimize unnecessary external API calls. |
| NFR-04 | The system should cache appropriate data/results where practical. |
| NFR-05 | The system should protect GitHub credentials/tokens. |
| NFR-06 | The system should provide understandable explanations for risk results. |
| NFR-07 | The system should be usable within the selected free-tier deployment limits. |
| NFR-08 | The backend should provide consistent API responses. |

---

## 4.3 Domain Requirements

Possible domain concepts:

- Repository
- Commit
- Contributor
- Issue
- Pull Request
- Code review
- Sprint
- Milestone
- Task
- Issue age
- PR merge time
- Development activity
- Project risk
- Project health

## Requirement Quality Check

Every important requirement should be:

- Clear
- Specific
- Testable
- Feasible
- Traceable to a user/stakeholder need

## Checkpoints

- [ ] Write functional requirements.
- [ ] Write non-functional requirements.
- [ ] Write domain requirements.
- [ ] Assign unique IDs.
- [ ] Remove duplicates.
- [ ] Remove ambiguous wording.
- [ ] Check feasibility against free-tier/no-GPU constraints.
- [ ] Review requirements with stakeholders/team.
- [ ] Freeze the initial requirement baseline.

**Deliverable**
- Software Requirements Specification / Requirements Document

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 5 — User Stories & Product Backlog

## Objective

Convert requirements into user stories with acceptance criteria.

The course requires the front of the user-story card to contain:

- Role
- Goal
- Benefit

The back should contain:

- Acceptance criteria / conditions of satisfaction

## User Story Template

### US-XX — Story Title

**Role:** As a `<role>`

**Goal:** I want `<goal>`

**Benefit:** So that `<benefit>`

### Acceptance Criteria

```text
Given ...
When ...
Then ...
```

---

## Example

### US-01 — Connect GitHub Repository

**Role:** As a Project Manager

**Goal:** I want to connect a GitHub repository

**Benefit:** So that the system can analyze project activity.

### Acceptance Criteria

- [ ] Given a valid repository URL, the system accepts the repository.
- [ ] The system retrieves basic repository information.
- [ ] The repository is associated with the project.
- [ ] An invalid/inaccessible repository produces a clear error.

---

## Example: Stale Issue Detection

### US-02 — Identify Stale Issues

**Role:** As a Team Lead

**Goal:** I want the system to identify inactive issues

**Benefit:** So that unresolved work can be reviewed or prioritized.

### Acceptance Criteria

- [ ] The system calculates issue inactivity.
- [ ] The configured stale threshold is applied.
- [ ] Issues exceeding the threshold are marked as stale.
- [ ] The dashboard displays the affected issues.

---

## Product Backlog Fields

Recommended fields:

| Field | Purpose |
|---|---|
| Story ID | Unique identifier |
| User Story | Requirement in user-story form |
| EPIC | Parent feature group |
| Priority | Business/team priority |
| Story Points | Estimated effort |
| Sprint | Planned sprint |
| Acceptance Criteria | Conditions of satisfaction |
| Status | Backlog / To Do / In Progress / Done |
| Assignee | Responsible member |

## Checkpoints

- [ ] Convert requirements into user stories.
- [ ] Add acceptance criteria.
- [ ] Assign story IDs.
- [ ] Assign priorities.
- [ ] Estimate story points.
- [ ] Remove duplicate stories.
- [ ] Review stories for testability.
- [ ] Build the initial Product Backlog.
- [ ] Put the backlog under version control/documentation.

**Deliverable**
- Product Backlog

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 6 — EPICs & Sprint Planning

## Objective

Group related user stories into EPICs and use the EPICs to plan Sprints.

## Recommended EPIC Structure

### EPIC 1 — User & Repository Management

Possible stories:
- Connect repository
- Validate repository
- Configure project
- Manage repository information

### EPIC 2 — GitHub Data Collection

Possible stories:
- Fetch commits
- Fetch issues
- Fetch PRs
- Fetch contributors
- Store/cache data

### EPIC 3 — Project Analytics

Possible stories:
- Calculate health score
- Analyze issue activity
- Analyze PR activity
- Analyze contributor activity
- Analyze sprint progress

### EPIC 4 — Risk Detection

Possible stories:
- Stale issues
- PR bottlenecks
- Workload imbalance
- Schedule risk

### EPIC 5 — GenAI Insights

Possible stories:
- Generate project summary
- Explain risk findings
- Generate recommendations
- Generate project status report

### EPIC 6 — Dashboard & Visualization

Possible stories:
- Health dashboard
- Charts
- Risk view
- Report view

### EPIC 7 — Quality & Deployment

Possible stories:
- Unit testing
- Integration testing
- Error handling
- Deployment
- Monitoring/basic logging

---

## Suggested Sprint Structure

### Sprint 1 — Foundation

Focus:
- Project setup
- Requirements
- Architecture
- Frontend/backend skeleton
- Database foundation
- Concept poster

### Sprint 2 — GitHub Integration

Focus:
- GitHub API
- Repository connection
- Issues
- PRs
- Commits
- Contributors

### Sprint 3 — Analytics

Focus:
- Metrics engine
- Health score
- Issue analytics
- PR analytics
- Workload analysis
- Dashboard charts

### Sprint 4 — AI & Risk

Focus:
- Risk analysis
- AI insights
- Recommendations
- AI report generation

### Sprint 5 — Quality & Finalization

Focus:
- Testing
- Bug fixes
- UI refinement
- Deployment
- Final documentation
- Final demonstration

> Sprint count/duration should be adjusted to your course calendar.

## Sprint Planning Checklist

- [ ] Define Sprint Goal.
- [ ] Select stories from the backlog.
- [ ] Confirm capacity of team members.
- [ ] Break stories into tasks.
- [ ] Assign tasks.
- [ ] Estimate effort.
- [ ] Define Definition of Done.
- [ ] Create Sprint Board.
- [ ] Record Sprint Goal.
- [ ] Review dependencies and blockers.

**Deliverables**
- EPIC list
- Product Backlog
- Sprint Backlog
- Sprint Goals
- Sprint Board

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 7 — Identify & Resolve Requirement Conflicts

## Objective

Identify conflicting requirements or user stories across stakeholders and EPICs and document how the team resolves them.

## Example Conflict 1

**Requirement A:** Project Manager wants frequent GitHub synchronization.

**Requirement B:** System must stay within free API limits.

### Resolution

Use controlled synchronization, caching, refresh buttons, rate-limit handling, and only request necessary data.

---

## Example Conflict 2

**Requirement A:** Team Lead wants detailed developer analytics.

**Requirement B:** Developers want minimal exposure of potentially sensitive personal metrics.

### Resolution

Define appropriate visibility levels and show only metrics required for legitimate project management. Document what is visible and to whom.

---

## Example Conflict 3

**Requirement A:** User wants AI analysis on every dashboard refresh.

**Requirement B:** AI calls are limited/cost-constrained.

### Resolution

Cache AI analysis and only regenerate when the underlying metric snapshot changes or the user explicitly requests a refresh.

## Conflict Table

| Conflict ID | Stakeholder/Requirement A | Stakeholder/Requirement B | Resolution | Decision Owner |
|---|---|---|---|---|
| C-01 | Frequent sync | Limited API | Cached/controlled sync | Team |
| C-02 | Detailed analytics | Appropriate privacy | Role-based visibility | Team |
| C-03 | AI every refresh | Limited AI calls | Cached analysis | Team |

## Checkpoints

- [ ] Review requirements for conflicts.
- [ ] Record conflicting requirements.
- [ ] Identify affected stakeholders.
- [ ] Discuss alternatives.
- [ ] Select a resolution.
- [ ] Record rationale.
- [ ] Update the backlog/specification.
- [ ] Obtain stakeholder/team agreement.

**Deliverable**
- Requirement Conflict & Resolution Log

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 8 — Sprint 1 & Concept Poster

## Objective

Start development for Sprint 1 and prepare the required concept poster.

The concept poster should serve as a visual reference for the system and its development direction.

## Concept Poster Content

Include:

### 1. Problem

Software teams often have project information distributed across GitHub issues, PRs, commits, and sprint activities, making project health difficult to understand quickly.

### 2. Proposed Solution

An AI-assisted project health and risk analysis platform that converts repository/project activity into metrics, risk indicators, explanations, and actionable recommendations.

### 3. Target Users

- Project Managers
- Team Leads
- Developers
- Product Owners

### 4. Core Features

```text
GitHub Integration
      ↓
Data Collection
      ↓
Project Metrics
      ↓
Risk Detection
      ↓
GenAI Insights
      ↓
Dashboard + Report
```

### 5. Technology

- Frontend: Next.js/React
- Deployment: Vercel
- Backend: FastAPI/Python or equivalent
- Database: Free-tier database
- GitHub APIs
- Free/limited LLM API
- No GPU dependency

### 6. Expected Output

- Project Health Score
- Risk Indicators
- Bottlenecks
- Contributor Workload Insights
- Stale Issues
- Schedule Risks
- AI Recommendations
- Project Status Report

## Sprint 1 Definition of Done

A story should be considered Done only when:

- [ ] Implementation is complete.
- [ ] Basic validation/testing is complete.
- [ ] Code is committed by the actual contributor.
- [ ] Pull request/review process is followed where applicable.
- [ ] Acceptance criteria are satisfied.
- [ ] Documentation is updated.

## Checkpoints

- [ ] Sprint 1 Goal defined.
- [ ] Sprint 1 backlog selected.
- [ ] Architecture drafted.
- [ ] Frontend skeleton created.
- [ ] Backend skeleton created.
- [ ] Database strategy decided.
- [ ] GitHub repository initialized.
- [ ] Slack communication structure established.
- [ ] Concept poster created.
- [ ] Sprint 1 work started.

**Deliverables**
- Sprint 1 Backlog
- Concept Poster
- Initial Working Software
- Sprint Evidence

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 9 — System Architecture & Technical Planning

## Objective

Translate the approved requirements into an implementable architecture.

## Recommended Components

### Frontend

Responsibilities:

- Project/repository connection UI
- Dashboard
- Charts
- Risk views
- AI insights
- Report interface

### Backend

Responsibilities:

- Authentication/authorization if included
- GitHub API integration
- Data processing
- Metrics calculation
- Risk engine
- AI orchestration
- Report generation
- Database access

### GitHub Integration

Collect only the information required by the product.

Potential categories:

- Repository metadata
- Commits
- Issues
- Pull Requests
- Contributors
- Milestones/project activity as supported by the selected API design

### Metrics Engine

Example metrics:

```text
commit_count
commit_frequency
issue_count
stale_issue_count
issue_resolution_time
open_pr_count
pr_merge_time
review_delay
contributor_activity
contribution_distribution
sprint_completion
```

### Risk Engine

Example rules:

```text
IF stale_issue_count is high
THEN stale-issue risk increases

IF PR review delay is high
THEN review bottleneck risk increases

IF one contributor has unusually high workload share
THEN workload imbalance risk increases

IF sprint progress is below expected progress
THEN schedule risk increases
```

### GenAI Layer

Send compact, derived project metrics rather than unnecessary raw repository data.

```text
Raw GitHub Data
      ↓
Metrics Engine
      ↓
Compact Project Snapshot
      ↓
LLM
      ↓
Explanation + Recommendations
```

This design reduces unnecessary AI calls and makes results easier to test.

## Checkpoints

- [ ] Define component architecture.
- [ ] Define API boundaries.
- [ ] Define database schema.
- [ ] Define GitHub data model.
- [ ] Define metric formulas.
- [ ] Define risk rules.
- [ ] Define AI input/output structure.
- [ ] Define caching strategy.
- [ ] Define API error-handling strategy.
- [ ] Review architecture against free-tier limits.

**Deliverable**
- System Architecture Document

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 10 — Development

## Objective

Implement the product incrementally according to the Product Backlog and Sprint Backlogs.

## GitHub Workflow

Recommended flow:

```text
main
 |
 +-- feature/github-integration
 +-- feature/dashboard
 +-- feature/analytics
 +-- feature/risk-engine
 +-- feature/ai-report
 +-- feature/testing
```

Each member should:

1. Work on assigned tasks.
2. Create commits for actual work.
3. Open pull requests when appropriate.
4. Participate in reviews.
5. Keep issue/task status updated.
6. Document meaningful decisions.

The course requires development through GitHub, all team members to be contributors, and commits to reflect actual individual contribution.

## Suggested Repository Structure

```text
project/
├── frontend/
├── backend/
├── docs/
├── tests/
├── .github/
├── README.md
└── docker/            # only if actually needed
```

## Checkpoints

- [ ] Feature branches defined.
- [ ] Issues created for development tasks.
- [ ] Developers assigned to issues.
- [ ] Commits reflect actual individual work.
- [ ] Pull requests reviewed.
- [ ] Features integrated incrementally.
- [ ] Documentation updated.
- [ ] Sprint board updated.

**Deliverables**
- Working software increments
- GitHub history
- Pull Requests
- Updated documentation

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 11 — Testing & Validation

## Objective

Verify that the system satisfies requirements and acceptance criteria.

## Testing Levels

### Unit Testing

Test individual functions:

- Health score calculations
- Stale issue detection
- Workload calculations
- Risk rules
- Data transformation

### Integration Testing

Test:

```text
Frontend → Backend
Backend → GitHub API
Backend → Database
Backend → LLM API
```

### System Testing

Test complete workflows:

```text
Connect Repository
       ↓
Fetch Data
       ↓
Analyze
       ↓
Generate Insights
       ↓
View Dashboard
       ↓
Generate Report
```

### Acceptance Testing

Check each user story against its acceptance criteria.

## Important Edge Cases

- Invalid repository
- Private/inaccessible repository
- GitHub API failure
- API rate limit
- Empty repository
- Repository with no issues
- Repository with no pull requests
- LLM API failure
- Database failure
- Missing/partial data

## Checkpoints

- [ ] Unit tests written.
- [ ] Integration tests written.
- [ ] System workflows tested.
- [ ] User-story acceptance criteria verified.
- [ ] Error paths tested.
- [ ] API-limit behavior tested.
- [ ] AI failure behavior tested.
- [ ] Bugs recorded and prioritized.
- [ ] Regression testing performed.

**Deliverable**
- Test Plan
- Test Cases
- Test Results
- Bug/Issue Log

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 12 — Deployment & Final Demonstration

## Objective

Deploy the final system using free-tier infrastructure and demonstrate an end-to-end workflow.

## Deployment

Suggested:

```text
Frontend → Vercel
Backend  → Free-tier backend platform
Database → Free-tier database
AI       → Free/limited API
```

## Deployment Checklist

- [ ] Production environment configured.
- [ ] Environment variables secured.
- [ ] Frontend deployed.
- [ ] Backend deployed.
- [ ] Database configured.
- [ ] GitHub integration tested in production.
- [ ] AI integration tested in production.
- [ ] API limits reviewed.
- [ ] Error handling verified.
- [ ] Final URL documented.

## Demonstration Flow

Use one repository as a live/example project:

```text
1. Open application
2. Connect repository
3. Fetch/analyze data
4. Show project metrics
5. Show health score
6. Show stale issues
7. Show PR bottlenecks
8. Show workload imbalance
9. Show project risks
10. Generate AI recommendations
11. Generate project report
```

**Deliverable**
- Deployed Application
- Demo Script
- Final Presentation

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 13 — Documentation & Evidence

## Objective

Maintain evidence of the Software Engineering process, not only the final code.

## Evidence to Maintain

### Requirements

- [ ] Stakeholder analysis
- [ ] Elicitation plan
- [ ] Elicitation results
- [ ] Requirements
- [ ] User stories
- [ ] Acceptance criteria
- [ ] Product backlog
- [ ] EPICs
- [ ] Conflict log

### Agile/Scrum

- [ ] Sprint goals
- [ ] Sprint backlog
- [ ] Sprint board
- [ ] Stand-up records
- [ ] Reviews
- [ ] Retrospectives
- [ ] Burndown/progress evidence where used

### Development

- [ ] GitHub repository
- [ ] Issues
- [ ] Branches
- [ ] Commits
- [ ] Pull Requests
- [ ] Reviews

### Testing

- [ ] Test cases
- [ ] Test results
- [ ] Bugs
- [ ] Fixes
- [ ] Final verification

### Final Product

- [ ] Architecture
- [ ] Screenshots
- [ ] Deployment
- [ ] User guide
- [ ] Final report
- [ ] Final presentation

## Slack Evidence

The course requires team communication to happen over Slack rather than personal chat applications.

Maintain evidence of:

- Decisions
- Sprint updates
- Blockers
- Technical discussions
- Team coordination

[Back to top](#ai-software-project-health--risk-analyzer)

---

# Phase 14 — Final Readiness Checklist

## Requirements

- [ ] Stakeholders identified
- [ ] Elicitation techniques identified
- [ ] Elicitation performed
- [ ] Functional requirements completed
- [ ] Non-functional requirements completed
- [ ] Domain requirements completed
- [ ] User stories completed
- [ ] Acceptance criteria completed
- [ ] Product backlog completed
- [ ] EPICs completed
- [ ] Sprint planning completed
- [ ] Requirement conflicts documented and resolved

## Scrum

- [ ] Scrum process followed throughout
- [ ] Sprint goals recorded
- [ ] Sprint backlogs recorded
- [ ] Team responsibilities visible
- [ ] Reviews/retrospectives documented

## GitHub

- [ ] All members added as contributors
- [ ] Individual contribution is visible
- [ ] Commits reflect actual work
- [ ] Issues used for tasks
- [ ] Pull requests used appropriately
- [ ] Repository README updated

## Slack

- [ ] Team communication maintained on Slack
- [ ] Technical decisions recorded
- [ ] Sprint updates recorded
- [ ] Blockers recorded

## Product

- [ ] GitHub integration works
- [ ] Data collection works
- [ ] Metrics work
- [ ] Risk detection works
- [ ] Dashboard works
- [ ] AI insights work
- [ ] Recommendations work
- [ ] Project report works
- [ ] Error handling works
- [ ] Free-tier constraints respected
- [ ] No GPU dependency

## Testing

- [ ] Unit tests complete
- [ ] Integration tests complete
- [ ] System testing complete
- [ ] Acceptance testing complete
- [ ] Major bugs fixed

## Deployment

- [ ] Frontend deployed
- [ ] Backend deployed
- [ ] Database configured
- [ ] Production APIs tested
- [ ] Final demo workflow tested

## Final Submission

- [ ] Final report
- [ ] Concept poster
- [ ] Architecture diagram
- [ ] Requirements documentation
- [ ] Product backlog
- [ ] Sprint evidence
- [ ] Testing evidence
- [ ] GitHub evidence
- [ ] Slack evidence
- [ ] Deployment link
- [ ] Presentation/demo

---

# Recommended Definition of the MVP

The MVP should be achievable under the team's **free hosting, limited API, and no-GPU constraints**.

## MVP Core

```text
GitHub Repository
      ↓
Data Collection
      ↓
Metric Calculation
      ↓
Project Health Dashboard
      ↓
Risk Detection
      ↓
AI Explanation
      ↓
Recommendations
      ↓
Project Report
```

## Defer Until the Core System Works

Avoid making these mandatory early features:

- Training your own large language model
- Large-scale codebase embeddings
- GPU-based model training
- Continuous real-time processing of every GitHub event
- Full Jira replacement
- Complex microservices
- Unnecessary autonomous agents

Build the reliable engineering pipeline first; add advanced features only if time and resources allow.

---

# Overall Project Flow

```text
PHASE 0
Project Understanding & Setup
        ↓
PHASE 1
Stakeholders
        ↓
PHASE 2
Elicitation Techniques
        ↓
PHASE 3
Apply Elicitation
        ↓
PHASE 4
Requirements
        ↓
PHASE 5
User Stories + Product Backlog
        ↓
PHASE 6
EPICs + Sprints
        ↓
PHASE 7
Conflict Resolution
        ↓
PHASE 8
Sprint 1 + Concept Poster
        ↓
PHASE 9
Architecture
        ↓
PHASE 10
Development
        ↓
PHASE 11
Testing
        ↓
PHASE 12
Deployment + Demo
        ↓
PHASE 13
Documentation + Evidence
        ↓
PHASE 14
Final Readiness
```

---

# Course Requirement Traceability

| Course Instruction | Covered In |
|---|---|
| Agile/SCRUM throughout development | Phase 0, Phase 6, Phase 8, Phase 10, Phase 13 |
| Identify stakeholders/end users | Phase 1 |
| Identify elicitation techniques | Phase 2 |
| Apply elicitation techniques | Phase 3 |
| Functional requirements | Phase 4 |
| Non-functional requirements | Phase 4 |
| Domain requirements | Phase 4 |
| User stories + acceptance criteria | Phase 5 |
| Product Backlog | Phase 5 |
| EPICs and Sprints | Phase 6 |
| Identify and resolve conflicts | Phase 7 |
| Start Sprint 1 | Phase 8 |
| Concept poster | Phase 8 |
| GitHub collaboration | Phase 10, Phase 13 |
| Slack collaboration | Phase 0, Phase 13 |

---

# Final Principle

This project should be treated as:

**A Software Engineering project with an AI capability**, not merely an AI project.

The strongest implementation strategy is:

```text
Reliable Software Engineering Metrics
              +
      Deterministic Risk Rules
              +
       GenAI Explanation
              +
       Actionable Dashboard
```

This makes the system easier to validate, cheaper to operate, compatible with free-tier resources, and easier to defend in a Software Engineering viva.
