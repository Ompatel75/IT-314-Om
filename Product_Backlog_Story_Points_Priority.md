# IT314 Software Engineering
## Product Backlog — Story Points and Priority

**Project:** AI Software Project Health & Risk Analyzer  
**Prepared by:** Prince Savaliya  
**Task:** Story Points, Priority, and the Complete Product Backlog

---

## 1. Introduction

The Product Backlog is the single, ordered list of work represented by the current user stories for the AI Software Project Health & Risk Analyzer. The IT314 project instructions require each requirement to be represented by a user story with acceptance criteria; together these form the Product Backlog.

This document adds Story Points, Priority, and dependencies while preserving the current User Stories and Acceptance Criteria structure.

---

## 2. Current Project Baseline

| Artifact | Current Baseline |
|---|---|
| Functional Requirements | FR-1 to FR-21 (21 total) |
| User Stories | US-01 to US-21 (21 total) |
| Non-Functional Requirements | NFR-01 to NFR-11 (11 total) |
| Domain Requirements | DR-01 to DR-10 (10 total) |
| Stakeholder Groups | 6 |

### Traceability

The current Functional Requirements and User Stories documents use the direct mapping:

**FR-1 → US-01, FR-2 → US-02, ..., FR-21 → US-21**

The earlier Product Backlog contained an outdated 24-FR baseline and mismatch warnings. Those outdated statements are not part of this final version.

---

## 3. Story Point Estimation Method

Story Points represent relative effort, complexity, uncertainty, dependencies, integration difficulty, testing effort, and breadth — not hours or calendar days.

The backlog uses the Fibonacci-like scale:

- **3 points:** relatively contained data retrieval/display or straightforward configuration work.
- **5 points:** moderate computation, integration, validation, or foundational configuration/security work.
- **8 points:** GenAI-dependent analysis/explanation or features aggregating several upstream capabilities.
- **13 points:** not used in the current backlog.

**Total:** 110 story points across 21 stories.

---

## 4. Priority Classification

Priority is assigned as **High, Medium, or Low** using importance to the core project, stakeholder value, dependency impact, and importance to an initial usable version.

- **High:** core data ingestion, analysis/detection, authentication, integration credentials, role-based access, explanations, reporting, and dashboard capabilities.
- **Medium:** threshold configuration, report scheduling/delivery, and the appeal workflow.
- **Low:** report export and project/user archival or deactivation.

---

## 5. Complete Product Backlog

| Story ID | FR ID | User Story | Primary Role | Priority | Points | Dependencies | Acceptance Criteria (condensed) |
|---|---|---|---|---|---:|---|---|
| US-01 | FR-1 | As a Team Lead, I want to view commit history from the project's GitHub repository, including author, timestamp, and change size, so I can track ongoing development activity. | Team Lead | High | 5 | US-05 | Retrieves commit history; each commit shows author/timestamp/size; uses configured/default branch; indicates failure if repository cannot be accessed. |
| US-02 | FR-2 | As a Team Lead or Code Reviewer, I want to track GitHub pull requests, including their opening time, reviewer, open duration, and merge/close status, so I can monitor review progress. | Team Lead / Code Reviewer | High | 3 | US-05 | Each PR shows opening time, reviewer(s), open duration, and status; distinguishes open/merged/closed; open duration is available for open PRs. |
| US-03 | FR-3 | As a Team Lead, I want to view issue information from GitHub Issues, including status, assignee, labels, and time since last update, so I can monitor the issue queue. | Team Lead | High | 3 | US-05 | Each issue shows status, assignee, labels, and time since update; latest-update data supports stale comparison; reflects latest available information. |
| US-04 | FR-4 | As a Scrum Master, I want to view planned and completed tasks and sprint velocity from GitHub Projects and milestones, so I can understand progress against the sprint timeline. | Scrum Master | High | 5 | US-05 | Displays planned/completed tasks and sprint velocity; infers progress from the configured milestone/issue structure; uses most recent project data. |
| US-05 | FR-5 | As a Team Lead or Project Manager, I want to create and configure a project by linking its GitHub repositories, sprint data, and team-member GitHub usernames, so I can ensure development activity is attributed correctly. | Team Lead / Project Manager | High | 5 | US-19, US-20 | Authorized user creates a project, links repositories/sprint data, maps team members to GitHub usernames, and attributes activity correctly; required repository information is enforced. |
| US-06 | FR-6 | As a Team Lead or Scrum Master, I want the system to identify development bottlenecks and recurring blockers, such as unreviewed pull-request queues or workflow stages where work gets stuck, so I can address slowdowns before they affect delivery. | Team Lead / Scrum Master | High | 8 | US-02, US-03 | Identifies potential bottlenecks/blockers from project activity; identifies the source where available; presents findings to an authorized user. |
| US-07 | FR-7 | As a Team Lead, I want the system to identify team members whose activity indicates possible overload, so I can rebalance work when necessary. | Team Lead | High | 5 | US-01, US-02, US-04 | Compares member commit/PR/task activity with the team average; flags activity meeting the configured overload threshold; identifies contributing activity data. |
| US-08 | FR-8 | As a Team Lead, I want the system to identify GitHub Issues that have had no activity for a configurable period, so I can prevent stale work from being forgotten. | Team Lead | High | 3 | US-03 | Flags issues exceeding the configured stale-period threshold; threshold is project-specific; stale and active issues are distinguishable; new activity removes staleness. |
| US-09 | FR-9 | As a Project Manager, I want to see whether the sprint or project schedule is at risk, based on sprint velocity, task completion rate, and remaining backlog, so I can take corrective action early. | Project Manager | High | 5 | US-04 | Evaluates schedule risk from velocity, completion rate, and backlog; presents it as an indicative estimate; uses the latest available data. |
| US-10 | FR-10 | As a Team Lead or Admin, I want to review and adjust thresholds used for project-health flags, so I can adapt the flagging behavior to the team's context. | Team Lead / Admin | Medium | 3 | US-20 | Authorized user can view and update supported thresholds; updated values affect subsequent evaluations; invalid values are rejected. |
| US-11 | FR-11 | As a Developer or Team Lead, I want to see a plain-language explanation for each AI-generated flag, so I can understand the data and reasoning behind it. | Developer / Team Lead | High | 8 | US-06, US-07, US-08, US-09 | Each bottleneck/blocker/overload/stale/schedule-risk flag includes a plain-language explanation naming the contributing metrics. |
| US-12 | FR-12 | As a Project Manager, I want the system to automatically generate a project status report containing overall health, key risks, bottlenecks, and progress, so I can avoid compiling the information manually. | Project Manager | High | 8 | US-06, US-07, US-08, US-09, US-11 | Generated report includes health, risks, bottlenecks, and progress; matches data available at generation time; requires no manual compilation. |
| US-13 | FR-13 | As a Team Lead or Project Manager, I want to receive actionable recommendations with the project status report, so I can know what actions can be taken to improve project health. | Team Lead / Project Manager | High | 5 | US-12 | Recommendations address active risks/issues; each describes a specific action; recommendations use detected bottlenecks, blockers, overload, stale issues, or schedule risks where applicable. |
| US-14 | FR-14 | As a Project Manager, I want to choose the frequency and delivery channel for status reports, so I can receive them according to my workflow. | Project Manager | Medium | 5 | US-12 | User selects daily/weekly/end-of-sprint generation and dashboard/email/Slack destinations; reports follow the selected settings. |
| US-15 | FR-15 | As a Project Manager, I want to export a generated status report, such as in PDF format, so I can share it outside the platform. | Project Manager | Low | 3 | US-12 | Generated status report can be exported; PDF is supported; export contains relevant health, risk, bottleneck, and progress information. |
| US-16 | FR-16 | As a Team Lead, I want to view overall project health through a single dashboard combining bottlenecks, blockers, overloaded members, stale issues, and schedule risk in one place, so I can assess project status. | Team Lead | High | 8 | US-06, US-07, US-08, US-09 | Dashboard presents project-health information in one place; all core indicators are available; data is current to the latest available project data; further detail is accessible. |
| US-17 | FR-17 | As a Developer, I want to view a flag raised against me and submit feedback or an appeal, so I can provide context about the flag and have it reviewed. | Developer | Medium | 5 | US-11 | Flagged user can view the flag/explanation, submit feedback or appeal, and see resolution status; a team lead/admin can review and resolve it. |
| US-18 | FR-18 | As an Admin, I want to control access to individual-level project metrics according to user roles, so I can protect individual privacy while allowing authorized users to access detailed information. | Admin | High | 8 | US-20 | Authorized roles can access permitted individual-level metrics; other users receive only permitted aggregated information; unauthorized access is denied. |
| US-19 | FR-19 | As an Admin or System Administrator, I want to connect the platform to GitHub and configure credentials for the LLM/GenAI provider, so I can manage the system's core integrations. | Admin / System Administrator | High | 5 | US-20 | Authorized user configures GitHub and LLM/GenAI connections; credentials are stored encrypted at rest and never exposed in logs or client-side code. |
| US-20 | FR-20 | As a New User, I want to sign up, log in, and be assigned a role, so I can access the features and information permitted for that role. | New User | High | 5 | None (foundational) | User can create an account and log in with valid credentials; every user has a role; access matches the role; invalid login attempts are rejected. |
| US-21 | FR-21 | As an Admin, I want to archive or delete projects and deactivate user accounts, so I can control access to project data. | Admin | Low | 5 | US-05, US-18 | Admin can archive/delete a project; deactivated users cannot log in or access project data. |

---

## 6. Story Point Distribution

| Story Points | No. of Stories | Story IDs |
|---:|---:|---|
| 1 | 0 | — |
| 2 | 0 | — |
| 3 | 5 | US-02, US-03, US-08, US-10, US-15 |
| 5 | 11 | US-01, US-04, US-05, US-07, US-09, US-13, US-14, US-17, US-19, US-20, US-21 |
| 8 | 5 | US-06, US-11, US-12, US-16, US-18 |
| 13 | 0 | — |
| **TOTAL** | **21** | **110 story points** |

---

## 7. Priority Distribution

| Priority | No. of Stories | Story IDs |
|---|---:|---|
| High | 16 | US-01, US-02, US-03, US-04, US-05, US-06, US-07, US-08, US-09, US-11, US-12, US-13, US-16, US-18, US-19, US-20 |
| Medium | 3 | US-10, US-14, US-17 |
| Low | 2 | US-15, US-21 |
| **TOTAL** | **21** | **21 stories** |

---

## 8. Dependency Summary

- **Foundation → data ingestion:** US-05 (project/team configuration) and US-19 (GitHub/LLM credentials) must exist before commit, PR, issue, or sprint data can be pulled (US-01–US-04).
- **Data → detection:** US-06 needs PR and issue data (US-02, US-03); US-07 needs commit, PR, and task activity (US-01, US-02, US-04); US-08 needs issue data (US-03); US-09 needs sprint data (US-04).
- **Detection → explanation → reporting:** US-11 depends on US-06–US-09; US-12 depends on detection and explanation; US-13, US-14, and US-15 depend on US-12.
- **Detection → dashboard:** US-16 aggregates US-06–US-09.
- **Threshold configuration:** US-10 can follow the detection stories with sensible defaults, but it feeds into the four detection capabilities once built.
- **Access control:** US-18 controls individual-level data access; US-21 depends on both US-05 and US-18.
- **Authentication:** US-20 is a universal dependency for role-gated functionality.

---

## 9. Foundational User Stories

| Story | Why Foundational | What Depends on It |
|---|---|---|
| US-20 | Authentication and role assignment are required for role-gated functionality. | All other 20 stories |
| US-19 | GitHub and GenAI credentials are required for external integrations. | US-01–US-04 and downstream analysis/reporting |
| US-05 | A project and team mapping must exist before repository-specific activity can be attributed/retrieved. | US-01–US-04 and downstream capabilities |
| US-01 / US-02 / US-03 / US-04 | These are the raw activity-data sources: commits, PRs, issues, and sprint/task data. | US-06–US-09, US-12, and US-16 |

---

## 10. Backlog Validation

| Check | Result |
|---|---|
| All current user stories included | PASS — 21/21 |
| No duplicate stories | PASS |
| No stories omitted from the current 21 | PASS |
| Correct FR ↔ User Story mapping | PASS — FR-1→US-01 through FR-21→US-21 |
| Priority assigned to every story | PASS — 21/21 |
| Story Points assigned to every story | PASS — 21/21 |
| Dependencies documented | PASS |
| Acceptance criteria preserved | PASS — condensed only in the backlog table |
| Story Point total correct | PASS — 110 |
| Priority counts correct | PASS — High: 16, Medium: 3, Low: 2 |
| Current NFR/Domain baseline reflected | PASS — NFR-01..NFR-11 and DR-01..DR-10 |

---

## 11. Conclusion

This final Product Backlog contains all 21 current user stories, their FR traceability, acceptance criteria, priorities, story points, and dependencies.

The estimates total **110 story points**, with the documented priority distribution of **16 High, 3 Medium, and 2 Low**.

The backlog is internally consistent with the current supplied Functional Requirements and User Stories documents and is ready to be used as input for the next Scrum planning stage: grouping stories into EPICs and Sprints.

**Prepared by Prince Savaliya | IT314 Software Engineering | Autumn 2026–27**
