# Non-Functional Requirements

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
