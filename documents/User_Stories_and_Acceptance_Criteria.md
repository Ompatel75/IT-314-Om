# User Stories & Acceptance Criteria

## AI Software Project Health & Risk Analyzer

**Prepared by:** Gaurav Rathod \| IT314 Software Engineering

------------------------------------------------------------------------

## US-01 --- View Commit History

**Functional Requirement:** FR-1

**User Story**

As a Team Lead, I want to view commit history from the project's GitHub
repository, including author, timestamp, and change size, so I can track
ongoing development activity.

**Acceptance Criteria**

1.  The system retrieves commit history from the linked GitHub
    repository.
2.  Each commit displays its author, timestamp, and size of changes.
3.  The system analyzes the repository's default branch unless a
    different branch has been configured.
4.  If the repository cannot be accessed, the system indicates that the
    commit data could not be retrieved.

------------------------------------------------------------------------

## US-02 --- Track GitHub Pull Requests

**Functional Requirement:** FR-2

**User Story**

As a Team Lead or Code Reviewer, I want to track GitHub pull requests,
including their opening time, reviewer, open duration, and merge/close
status, so I can monitor review progress.

**Acceptance Criteria**

1.  Each tracked pull request displays its opening time, reviewer(s),
    current open duration, and status.
2.  The system distinguishes pull requests that are open, merged, or
    closed.
3.  The open duration is available for pull requests that remain open.

------------------------------------------------------------------------

## US-03 --- View GitHub Issue Information

**Functional Requirement:** FR-3

**User Story**

As a Team Lead, I want to view issue information from GitHub Issues,
including status, assignee, labels, and time since last update, so I can
monitor the issue queue.

**Acceptance Criteria**

1.  Each tracked issue displays status, assignee, labels, and time since
    its last update.
2.  Each tracked issue includes its latest-update information so that
    its age can be compared with the project's configured stale-issue
    threshold.
3.  Time since the last update reflects the latest available issue
    information.

------------------------------------------------------------------------

## US-04 --- View Sprint Progress and Velocity

**Functional Requirement:** FR-4

**User Story**

As a Scrum Master, I want to view planned and completed tasks and sprint
velocity from GitHub Projects and milestones, so I can understand
progress against the sprint timeline.

**Acceptance Criteria**

1.  The system displays planned and completed tasks for a sprint based
    on the project's GitHub Projects and milestone data.
2.  The system displays the velocity for completed sprints.
3.  The system infers sprint progress from whatever milestone/issue
    structure is configured for the project, which may vary in
    granularity across projects.
4.  The displayed sprint data matches the most recently available
    project and sprint data.

------------------------------------------------------------------------

## US-05 --- Create and Configure a Project

**Functional Requirement:** FR-5

**User Story**

As a Team Lead or Project Manager, I want to create and configure a
project by linking its GitHub repositories, sprint data, and team-member
GitHub usernames, so I can ensure development activity is attributed
correctly.

**Acceptance Criteria**

1.  An authorized user can create a project and associate it with target
    GitHub repositories and sprint data.
2.  Team members can be mapped to their GitHub usernames.
3.  The system attributes commits, pull requests, and issue activity to
    the mapped team members.
4.  The project cannot be configured without the required repository
    information.

------------------------------------------------------------------------

## US-06 --- Identify Development Bottlenecks and Blockers

**Functional Requirement:** FR-6

**User Story**

As a Team Lead or Scrum Master, I want the system to identify
development bottlenecks and recurring blockers, such as unreviewed
pull-request queues or workflow stages where work gets stuck, so I can
address slowdowns before they affect delivery.

**Acceptance Criteria**

1.  The system identifies potential development bottlenecks and
    recurring blockers from project activity.
2.  A detected bottleneck or blocker identifies the relevant source of
    the slowdown, where available.
3.  The system presents identified bottlenecks and blockers to an
    authorized user for investigation.

------------------------------------------------------------------------

## US-07 --- Identify Possible Team Member Overload

**Functional Requirement:** FR-7

**User Story**

As a Team Lead, I want the system to identify team members whose
activity indicates possible overload, so I can rebalance work when
necessary.

**Acceptance Criteria**

1.  The system compares a team member's commit, pull-request, and task
    activity with the team average.
2.  The system flags members whose activity meets the configured
    overloaded threshold.
3.  The overload threshold is a configurable, project-specific value
    rather than a fixed platform-defined value.
4.  The system identifies the activity information contributing to the
    overload indication.

------------------------------------------------------------------------

## US-08 --- Identify Stale GitHub Issues

**Functional Requirement:** FR-8

**User Story**

As a Team Lead, I want the system to identify GitHub Issues that have
had no activity for a configurable period, so I can prevent stale work
from being forgotten.

**Acceptance Criteria**

1.  An issue whose last activity exceeds the configured stale-period
    threshold is identified as stale.
2.  The stale-period threshold can be configured on a per-project basis.
3.  The system allows identified stale issues to be distinguished from
    active issues.
4.  An issue is no longer considered stale when new activity is recorded
    on it.

------------------------------------------------------------------------

## US-09 --- Identify Schedule Risk

**Functional Requirement:** FR-9

**User Story**

As a Project Manager, I want to see whether the sprint or project
schedule is at risk, based on sprint velocity, task completion rate, and
remaining backlog, so I can take corrective action early.

**Acceptance Criteria**

1.  The system evaluates schedule risk using sprint velocity, task
    completion rate, and remaining backlog.
2.  The schedule-risk indicator is presented to the Project Manager as
    an indicative estimate rather than a guaranteed prediction.
3.  The displayed risk indicator is based on the most recently available
    sprint velocity, task completion rate, and remaining backlog data.

------------------------------------------------------------------------

## US-10 --- Configure Project-Health Thresholds

**Functional Requirement:** FR-10

**User Story**

As a Team Lead or Admin, I want to review and adjust thresholds used for
project-health flags, so I can adapt the flagging behavior to the team's
context.

**Acceptance Criteria**

1.  An authorized user can view the configured thresholds for the
    supported flag types.
2.  An authorized user can update a threshold.
3.  The updated threshold is used in subsequent flag evaluations.
4.  Invalid threshold values are rejected.

------------------------------------------------------------------------

## US-11 --- Explain AI-Generated Flags

**Functional Requirement:** FR-11

**User Story**

As a Developer or Team Lead, I want to see a plain-language explanation
for each AI-generated flag, so I can understand the data and reasoning
behind it.

**Acceptance Criteria**

1.  Each bottleneck, blocker, overload, stale-issue, or schedule-risk
    flag includes an explanation.
2.  The explanation names the specific metrics that contributed to the
    flag.
3.  The explanation is presented in plain, non-technical language to the
    user permitted to view the flag.

------------------------------------------------------------------------

## US-12 --- Generate Project Status Report

**Functional Requirement:** FR-12

**User Story**

As a Project Manager, I want the system to automatically generate a
project status report containing overall health, key risks, bottlenecks,
and progress, so I can avoid compiling the information manually.

**Acceptance Criteria**

1.  The generated report includes overall project health, key risks,
    bottlenecks, and progress.
2.  The report's health, risk, bottleneck, and progress information
    matches the project data available when the report is generated.
3.  The report can be generated without requiring manual compilation of
    the information.

------------------------------------------------------------------------

## US-13 --- Provide Actionable Recommendations

**Functional Requirement:** FR-13

**User Story**

As a Team Lead or Project Manager, I want to receive actionable
recommendations with the project status report, so I can know what
actions can be taken to improve project health.

**Acceptance Criteria**

1.  Recommendations are provided for relevant active project risks or
    issues.
2.  Each recommendation describes a specific action relevant to the
    detected condition.
3.  Recommendations are based on the project's detected bottlenecks,
    blockers, overload, stale issues, or schedule risks where
    applicable.

------------------------------------------------------------------------

## US-14 --- Configure Status Report Frequency and Delivery

**Functional Requirement:** FR-14

**User Story**

As a Project Manager, I want to choose the frequency and delivery
channel for status reports, so I can receive them according to my
workflow.

**Acceptance Criteria**

1.  The user can select daily, weekly, or end-of-sprint report
    generation.
2.  The user can select the report delivery destination(s): dashboard,
    email, or Slack.
3.  Reports are generated and delivered according to the selected
    settings.

------------------------------------------------------------------------

## US-15 --- Export Project Status Report

**Functional Requirement:** FR-15

**User Story**

As a Project Manager, I want to export a generated status report, such
as in PDF format, so I can share it outside the platform.

**Acceptance Criteria**

1.  A generated status report can be exported.
2.  PDF is supported as an export format.
3.  The exported report contains the relevant health, risk, bottleneck,
    and progress information from the generated report.

------------------------------------------------------------------------

## US-16 --- View Overall Project Health Dashboard

**Functional Requirement:** FR-16

**User Story**

As a Team Lead, I want to view overall project health through a single
dashboard combining bottlenecks, blockers, overloaded members, stale
issues, and schedule risk in one place, so I can assess project status.

**Acceptance Criteria**

1.  The dashboard presents project-health information in one place.
2.  Bottleneck, blocker, overloaded-member, stale-issue, and
    schedule-risk information is available from the dashboard.
3.  The dashboard displays the most recently available project-health
    data for the selected project.
4.  The user can access further details for the displayed indicators.

------------------------------------------------------------------------

## US-17 --- Submit Feedback or Appeal on a Flag

**Functional Requirement:** FR-17

**User Story**

As a Developer, I want to view a flag raised against me and submit
feedback or an appeal, so I can provide context about the flag and have
it reviewed.

**Acceptance Criteria**

1.  A flagged team member can view the flag and its explanation.
2.  The user can submit feedback or an appeal for the specific flag.
3.  A team lead or admin can review and resolve the submitted appeal.
4.  The resolution status is available to the affected user.

------------------------------------------------------------------------

## US-18 --- Control Access to Individual-Level Metrics

**Functional Requirement:** FR-18

**User Story**

As an Admin, I want to control access to individual-level project
metrics according to user roles, so I can protect individual privacy
while allowing authorized users to access detailed information.

**Acceptance Criteria**

1.  Authorized roles can access individual-level metrics for projects
    they are permitted to view.
2.  Users without the required permissions receive only the permitted
    aggregated information.
3.  Unauthorized attempts to access individual-level data are denied.

------------------------------------------------------------------------

## US-19 --- Configure GitHub and LLM/GenAI Integrations

**Functional Requirement:** FR-19

**User Story**

As an Admin or System Administrator, I want to connect the platform to
GitHub and configure credentials for the LLM/GenAI provider, so I can
manage the system's core integrations.

**Acceptance Criteria**

1.  An authorized user can configure the connection between the platform
    and GitHub.
2.  An authorized user can configure credentials for the LLM/GenAI
    provider.
3.  Configured credentials are stored encrypted at rest and are never
    exposed in logs or client-side code.

------------------------------------------------------------------------

## US-20 --- Sign Up, Log In, and Receive a Role

**Functional Requirement:** FR-20

**User Story**

As a New User, I want to sign up, log in, and be assigned a role, so I
can access the features and information permitted for that role.

**Acceptance Criteria**

1.  A new user can create an account.
2.  A registered user can log in with valid credentials.
3.  Each user has an assigned role.
4.  Access permissions correspond to the user's assigned role.
5.  Invalid login attempts are rejected.

------------------------------------------------------------------------

## US-21 --- Archive or Delete Projects and Deactivate Users

**Functional Requirement:** FR-21

**User Story**

As an Admin, I want to archive or delete projects and deactivate user
accounts, so I can control access to project data.

**Acceptance Criteria**

1.  An admin can archive a project so that it is no longer treated as an
    active project.
2.  An admin can delete a project.
3.  A deactivated user cannot log in or access project data.
