# AI Software Project Health & Risk Analyzer

**Functional Requirements Specification**

---

## Table of Contents

- [1. Data Collection & Integration](#1-data-collection--integration)
- [2. AI-Based Analysis](#2-ai-based-analysis)
- [3. Reporting & Recommendations](#3-reporting--recommendations)
- [4. Dashboard & User Interaction](#4-dashboard--user-interaction)
- [5. Access Control & Administration](#5-access-control--administration)

---

## 1. Data Collection & Integration

Covers how the system connects to source data — repositories, pull requests, issues, and sprint activity — and how projects and teams are configured.

| ID | Requirement | Description |
|:---|:---|:---|
| **FR-1** | Repository and commit analysis | Connect to a project's GitHub repository and retrieve commit history — author, timestamp, and size of changes — to track ongoing development activity. |
| **FR-2** | Pull request tracking | Track GitHub pull requests, including when they are opened, who is reviewing them, how long they remain open, and their eventual merge or close status. |
| **FR-3** | Issue tracking | Pull issue data from GitHub Issues, including status, assignee, labels, and time since last update. |
| **FR-4** | Sprint activity monitoring | Track sprint-level data from GitHub Projects and milestones — planned vs. completed tasks and velocity per sprint — to understand progress against the sprint timeline. |
| **FR-5** | Team and project configuration | Allow an authorized user to create a project, associate it with target GitHub repositories and sprint data, and map team members to their GitHub usernames so all activity is accurately attributed. |

---

## 2. AI-Based Analysis

Covers the GenAI layer that detects bottlenecks, overload, stale work, and schedule risk, and explains its reasoning.

| ID | Requirement | Description |
|:---|:---|:---|
| **FR-6** | Bottleneck and blocker detection | The GenAI layer identifies development bottlenecks and recurring blockers, such as a pile-up of unreviewed pull requests or a workflow stage where tasks consistently get stuck. |
| **FR-7** | Overloaded team member detection | Compare each team member's commit, PR, and task activity against the team average and flag individuals who appear overloaded, so leads can rebalance work. |
| **FR-8** | Stale issue detection | Identify GitHub Issues with no activity for a configurable period and flag them as stale so they are not forgotten in the backlog. |
| **FR-9** | Schedule risk assessment | Assess whether the current sprint or overall project timeline is at risk of slipping, based on sprint velocity, task completion rate, and remaining backlog, and present this as a risk indicator. |
| **FR-10** | Threshold configuration | Allow thresholds used for flags (overloaded, bottleneck, stale, at-risk) to be reviewed and adjusted. |
| **FR-11** | Explainable AI flags | Whenever the system raises a flag, it provides a plain-language explanation of the data and reasoning behind that flag. |

---

## 3. Reporting & Recommendations

Covers automated status reporting, recommendations, scheduling, and export.

| ID | Requirement | Description |
|:---|:---|:---|
| **FR-12** | Automated status report generation | Use GenAI to automatically generate project status reports summarizing overall health, key risks, bottlenecks, and progress — without requiring manual compilation. |
| **FR-13** | Actionable recommendations | Generate specific, actionable recommendations alongside each report, such as reassigning tasks from an overloaded member or adding a reviewer to reduce PR wait time. |
| **FR-14** | Report scheduling and delivery | Allow users to choose report frequency (daily, weekly, or end-of-sprint) and deliver reports to the dashboard, by email, or to Slack. |
| **FR-15** | Report export | Allow a project manager to export a generated status report — for example, to PDF — for sharing outside the platform. |

---

## 4. Dashboard & User Interaction

Covers the central health dashboard and how flagged individuals can respond to AI-raised flags.

| ID | Requirement | Description |
|:---|:---|:---|
| **FR-16** | Project health dashboard | Provide a dashboard giving a unified view of overall project health, combining bottlenecks, overloaded members, stale issues, and schedule risk in one place. |
| **FR-17** | Feedback and appeal on AI flags | A team member flagged by the system (for example, as overloaded) can view that flag and submit feedback or an appeal, which a team lead or admin can review and resolve. |

---

## 5. Access Control & Administration

Covers role-based permissions, platform integration setup, authentication, and project lifecycle administration.

| ID | Requirement | Description |
|:---|:---|:---|
| **FR-18** | Role-based data access | Restrict access to individual-level metrics based on user role, so only team leads, managers, and authorized roles can view per-developer data, while other stakeholders see only aggregated summaries. |
| **FR-19** | Integration configuration | Allow an administrator to connect the platform to GitHub and configure credentials for the LLM/GenAI provider. |
| **FR-20** | User account and authentication | Allow users to sign up and log in, and assign each user a role (developer, team lead, project manager, or admin) that determines what they are permitted to see and do. |
| **FR-21** | Project deactivation and access management | Allow administrators to archive or delete projects, and deactivate user accounts to revoke access. |

---

*Total requirements: 21 | Categories: 5*
