# Lab 1 – Python Scripting for Operational Tasks

## Overview

This lab focused on using Python as a scripting language for common operational and system-administration tasks. Rather than strictly following the original lab scripts, the goal was to understand what each script was doing, why it was written that way, and how it could be improved to better reflect modern Linux systems and real-world DevOps practices.

All work was performed on a headless Ubuntu Server accessed via SSH. The scripts were cloned from a course-provided repository and then incrementally modified for correctness, clarity, and usability. The emphasis throughout the lab was experimentation and learning rather than rote execution of steps.

Screenshots referenced in this document are included where appropriate to demonstrate script output and behavior.

---

## passChk.py – Account and Password Auditing

### Original behavior

The original `passChk.py` script attempted to identify weak user accounts by checking:

* Usernames shorter than a fixed length
* Password fields shorter than a fixed length

Upon review, this logic was misleading on modern Linux systems. Passwords are not stored in plaintext and cannot be meaningfully evaluated by length alone.

### Modifications

The script was rewritten to:

* Read user accounts from `/etc/passwd`
* Inspect password status using `/etc/shadow` via the `spwd` module
* Correctly detect accounts that are:

  * Locked or disabled
  * Missing a password
* Optionally exclude system accounts based on UID thresholds

The script was intentionally designed to be **read-only** and non-destructive. It performs no writes and makes no system changes. When run without sufficient permissions, it exits safely with an explanatory message.

### Outcome

Running the script on the server correctly identified the `nobody` account as locked/disabled, which is expected behavior on Ubuntu systems. No weak user-created accounts were detected.

*(Screenshot: passChk.py output)*

---

## netmon.py – Network Reachability Monitoring

### Purpose

The goal of `netmon.py` was to demonstrate basic network monitoring from the application layer, similar to what an operations engineer might use for simple diagnostics.

### Modifications

The script was refactored to:

* Use `ping` via Python’s `subprocess` module
* Support different connectivity targets (e.g., public internet vs. LAN)
* Avoid hardcoding environment-specific values (such as a private gateway IP)

To prevent leaking local network details, environment-specific values were externalized using environment variables and optionally a `.env` file (excluded via `.gitignore`). This reflects standard DevOps practices for configuration separation.

### Outcome

The script reliably reports whether network connectivity is available and can be adapted to different environments without modifying source code.

*(Screenshot: netmon.py output)*

---

## envChk.py – System Environment Inspection

### Purpose

This script evolved into a more comprehensive system-inspection utility designed to provide a snapshot of system health. It mirrors the type of information commonly checked during incident response or routine system validation.

### Implemented features

The script now reports:

* System boot time
* CPU usage and core counts
* Load averages (1, 5, and 15 minutes)
* Temperature sensor readings (human-readable, with optional raw JSON)
* Memory and swap usage
* Disk usage across mounted filesystems (excluding virtual filesystems)

Output formatting was improved to favor readability while preserving access to raw data when useful for debugging or learning.

### Design considerations

* All metrics are collected using `psutil`, a widely used system utilities library
* Output is clearly sectioned and labeled
* The script remains safe and non-invasive
* Raw JSON output is available but optional

*(Screenshot: envChk.py output)*

---

## Version Control and Workflow

A dedicated Git repository was created to manage these scripts. Work was performed directly on the server using Git and later enhanced with VS Code Remote SSH for improved editing and navigation.

Key practices adopted:

* Using branches and pull requests to protect the `main` branch
* Avoiding hardcoded environment values in committed code
* Using `.gitignore` to exclude local configuration files

This workflow mirrors real-world DevOps practices and reinforces the importance of reproducibility and safety.

---

## Reflection

This lab demonstrated how Python can be used as a practical scripting tool for operational tasks. More importantly, it emphasized understanding system behavior, questioning flawed assumptions in legacy scripts, and gradually adopting best practices.

Rather than simply running provided examples, modifying and extending the scripts provided deeper insight into:

* Linux account management
* System resource monitoring
* Network diagnostics
* Configuration management

This approach aligns closely with real-world DevOps work, where learning and experimentation are critical to building reliable systems.
