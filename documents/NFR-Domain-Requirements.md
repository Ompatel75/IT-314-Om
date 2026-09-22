# Non-Functional Requirements + Domain Requirements

## Non-Functional Requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Usability | The system shall present key information (risk status, alerts, recommendations) on the dashboard in a way that is understandable without training or a user manual. |
| NFR-02 | Performance / Latency | Dashboard views and API responses shall load within 3 seconds under normal network conditions. AI risk recalculation shall complete within 60 seconds of a triggering GitHub or Slack webhook event. |
| NFR-03 | Error Handling | The system shall detect invalid API responses and external-service outages (GitHub, Slack) and display a clear degraded-mode message rather than failing silently or crashing. |
| NFR-04 | API Efficiency | The system shall batch and minimize external API calls so as to remain within the external service's rate limits (e.g., GitHub REST API's authenticated-request limit). |
| NFR-05 | Caching | The system shall cache repository, commit, and pull-request data for a defined interval (e.g., 15 minutes) and invalidate the cache when a relevant webhook event is received. |
| NFR-06 | Security | The system shall store GitHub credentials, API keys, and project-related information encrypted at rest (e.g., via environment variables or a secrets manager) and shall never expose them in logs or client-side code. |
| NFR-07 | Explainability | The system shall provide a human-readable explanation, naming the contributing metrics, for every AI-generated risk flag or recommendation. |
| NFR-08 | Feedback / Appeal | The system shall allow a developer affected by an AI-generated warning to submit feedback disputing it, and shall record that feedback for review. |
| NFR-09 | Fairness | The system's risk-scoring logic shall be reviewed to avoid systematically penalizing contributors with legitimately different but non-problematic work patterns (e.g., part-time contributors, or reviewers with slower but thorough turnaround). |
| NFR-10 | Auditability | The system shall log key actions (external API calls, generated warnings, configuration changes) in a retrievable format for administrator review. |
| NFR-11 | Resource Constraint | The system shall operate within the limits of the selected free-tier deployment plan (e.g., request quotas, compute and storage caps). |

## Domain Requirements

| ID | Domain Concept | Domain Requirement |
|---|---|---|
| DR-01 | Repository | GitHub repository metadata (branches, default branch, visibility) defines the scope of analyzable data; the system shall operate against the repository's default branch unless configured otherwise. |
| DR-02 | Commit | Commit activity reflects only work that has been pushed to GitHub; local or uncommitted work is invisible to the system and shall not be treated as an absence of work. |
| DR-03 | Contributor / Workload | GitHub provides no standardized workload or capacity metric; "overload" is a domain-specific, configurable threshold rather than a fixed API value, and the system shall treat it as such. |
| DR-04 | Issue | Issue "staleness" has no universal definition across teams; the system shall allow the inactivity threshold that defines a stale issue to be configured per project. |
| DR-05 | Pull Request / Code Review | Acceptable review-turnaround time varies by team norm and by PR size/complexity; the system shall treat "delay" as a configurable threshold rather than a fixed duration. |
| DR-06 | Sprint | Sprint structures and blocker definitions differ across tools (GitHub Projects, Jira, etc.); the domain model shall accommodate this variation rather than assume one fixed sprint structure. |
| DR-07 | Milestone / Task | GitHub milestones do not enforce task-level granularity; the system shall infer progress from whatever milestone/issue structure a project actually uses, which may be incomplete or inconsistent. |
| DR-08 | Schedule & Project Risk | Schedule-risk indicators (e.g., velocity, burn-down trends) are estimates derived from historical activity, not guaranteed predictors; the system shall present them as indicative, not deterministic. |
| DR-09 | Project Health | "Project health" is a composite, subjective judgment rather than a directly measurable quantity; the system shall base it on a transparent, explainable combination of selected metrics rather than a single opaque score. |
| DR-10 | Integration | GitHub and Slack impose their own API rate limits, authentication models (OAuth/tokens), and webhook event formats; the system's integration layer shall conform to these external constraints rather than assume custom control over them. |
