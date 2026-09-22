# Stakeholders
**Project:** AI Software Project Health & Risk Analyzer
**Course:** IT314 — Software Engineering, Autumn 2026-27

---

## 1. Overview

This document identifies the stakeholders of the AI Software Project Health & Risk Analyzer and describes their relevance to the system.

---

## 2. Stakeholder List

| # | Stakeholder |
|---|---|
| 1 | Individual Developers |
| 2 | Code Reviewers / Senior Engineers |
| 3 | Engineering / Team Leads |
| 4 | Scrum Masters / Agile Coaches |
| 5 | Project Managers |
| 6 | System Administrators / DevOps Engineers |

---

## 3. Stakeholder Details

### 3.1 Individual Developers
Their commits, pull requests, and issue history are the raw data the system runs on. They need visibility into their own metrics, and a way to understand and contest AI-generated flags such as being marked a "bottleneck" or "overloaded," since these directly affect them.

### 3.2 Code Reviewers / Senior Engineers
PR review turnaround time is an explicit bottleneck signal the system tracks. Reviewers are both measured by the tool and rely on it to see review-queue health, giving them a distinct usage pattern from developers.

### 3.3 Engineering / Team Leads
The core power users of the system. They read the dashboard, decide how to rebalance workload, and act on the AI's recommendations on a day-to-day basis, making them central to the tool's practical value.

### 3.4 Scrum Masters / Agile Coaches
Use sprint-activity and schedule-risk output during sprint planning, daily standups, and retrospectives to improve team process — an Agile-specific use case distinct from Team Leads' workload management.

### 3.5 Project Managers
The main audience for the auto-generated status reports. They track overall delivery risk against the project timeline, focusing on schedule and delivery rather than individual workload.

### 3.6 System Administrators / DevOps Engineers
Deploy, configure, and keep the platform running; manage integration credentials and webhooks with GitHub and Slack. Without them, the mandatory tool integrations required by this project cannot function.
