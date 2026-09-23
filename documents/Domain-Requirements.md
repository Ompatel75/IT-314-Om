# Domain Requirements

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
| DR-10 | Integration | GitHub and Slack impose their own API rate limits, authentication models (OAuth/tokens), and webhook event formats; the system's integration layer shall conform to these external constraints rather than assume custom control over them. .|
