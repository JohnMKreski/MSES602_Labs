# MSES602 – DevOps Lab Assignments

This repository contains my **lab assignments for MSES602 (DevOps)** at Regis University. It serves as a consolidated workspace for hands-on exercises focused on **automation, system inspection, and infrastructure tooling**, rather than a single-purpose project.

Course materials and reference utilities provided by Regis University can be found here:

* [https://github.com/RegisUniversity/MSES602_DevOpsUtils.git](https://github.com/RegisUniversity/MSES602_DevOpsUtils.git)
* [https://github.com/RegisUniversity/MSES602_ansible.git](https://github.com/RegisUniversity/MSES602_ansible.git)
* [https://github.com/RegisDevOps/MSES602_HelloWorld](https://github.com/RegisDevOps/MSES602_HelloWorld)

---

## Repository Purpose

The goal of this repository is to:

* Maintain one organized location for all MSES602 lab work
* Track incremental learning across multiple DevOps-related topics
* Capture both working artifacts (scripts, playbooks) and written reflections

Labs are organized by number and evolve as concepts build throughout the course.

---

## Lab Structure

```text
labs/
├── lab01/        # Python scripting and system inspection
├── lab02/        # Ansible + Jenkins automation
└── labXX/        # Future labs
```

Each lab directory typically contains:

* A `.md` with the lab write-up and reflection
* Supporting assets (screenshots, diagrams)
* Lab-specific code or configuration files

---

## [Lab 1 – Python Scripting Basics](labs/lab01/lab1.md)

Lab 1 focuses on using Python for operational and system-level tasks, emphasizing safe inspection and understanding over complex automation.

Topics include:

* Reading system state (uptime, CPU, memory)
* Basic network reachability checks
* Auditing local Linux user accounts (read-only)

The intent is to learn how scripting supports DevOps workflows without treating scripts as black boxes.

---

## [Lab 2 – Ansible and Jenkins Automation](labs/lab02/lab2.md)

Lab 2 introduces configuration management and CI tooling using Ansible to provision Jenkins on a headless Linux server.

Topics include:

* Infrastructure as Code concepts
* Package management and service control with Ansible
* Secure repository and GPG key handling
* Jenkins installation, initial configuration, and plugin review

This lab highlights the difference between provisioning tools (Ansible) and continuous automation platforms (Jenkins).

---

## [Lab 3 - Continuous Integration with Git, Jenkins, and SonarQube](labs/lab03/lab3.md)

Lab 3 builds on the provisioned Jenkins environment by implementing a basic Continuous Integration workflow triggered by Git commits.

Topics include:

* Git-based build triggering (SCM polling)
* Automated dependency installation and test execution
* Static code analysis with SonarQube
* Build result interpretation (SUCCESS vs UNSTABLE)
* Jenkins workspace inspection and artifact review

This lab demonstrates how version control, automation servers, and quality analysis tools integrate to provide immediate feedback within a CI pipeline.

---

## [Lab 4 – Infrastructure Monitoring with Prometheus and Grafana](labs/lab04/lab4.md)

Lab 4 focuses on implementing a self-hosted infrastructure monitoring stack on a bare-metal Ubuntu Server, emphasizing real-world deployment and operational validation over purely vendor-based research.

Topics include:

* Installing and configuring node_exporter for host-level metrics
* Deploying Prometheus for metrics scraping and time-series storage
* Integrating Grafana for visualization and dashboarding
* Designing and validating alert rules using PromQL
* Testing alert lifecycle transitions (Inactive → Pending → Firing → Resolved)
* Understanding scrape intervals, evaluation timing, and multi-core CPU behavior

This lab demonstrates how observability systems operate in practice, highlighting the relationship between metrics collection, alert evaluation, and operational response within a DevOps environment.

---

## [Lab 5 – Static Analysis with SonarQube](labs/lab05/lab5.md)

Lab 5 focuses on performing standalone static code analysis using SonarQube on a self-hosted Ubuntu Server environment, emphasizing manual scan execution and interpretation of quality metrics rather than CI-triggered automation.

Topics include:

* Verifying SonarQube installation and service availability
* Executing `sonar-scanner` against a sample Node/Express application
* Reviewing `sonar-project.properties` configuration
* Analyzing Bugs, Code Smells, and Security Hotspots
* Interpreting coverage and duplication metrics
* Understanding rule classifications in SonarQube 9.9 LTS

This lab demonstrates how static analysis provides early insight into code quality, maintainability, and potential security concerns, reinforcing the role of automated scanning within a DevOps feedback loop.

---

## Supporting Scripts

Reusable or general-purpose scripts may appear outside individual lab folders, such as:

* Environment validation helpers
* Utility scripts reused across labs

These are kept separate from lab-specific artifacts to avoid duplication.

---

## Prerequisites

* Linux system (tested primarily on Ubuntu Server)
* Python 3 installed from system packages
* Internet access (for package installation where required)

Most scripts rely primarily on Python’s standard library. Third-party dependencies, when used, are documented explicitly.

---

## Learning Philosophy

This repository reflects a learning-first DevOps approach:

* Emphasis on understanding system behavior
* Preference for safe, non-destructive operations
* Incremental adoption of tooling and best practices
* Acceptance that solutions evolve as experience grows

The repository is intentionally structured to support experimentation, revision, and reflection rather than rigid step-following.

## AI Additional Tools

ChatGPT and Microsoft Copilot were used as supplemental tools for research, documentation review, and scripting assistance, consistent with common professional DevOps and software engineering workflows.

- OpenAI, ChatGPT: https://openai.com/chatgpt
- Microsoft Copilot: https://learn.microsoft.com/en-us/copilot/

