# System Environment

## Purpose

This document describes the system environment used to complete the DevOps Python scripting labs. It is provided to give context for script behavior, outputs, and design decisions, and to clarify deviations from any default virtual machine or operating system referenced in the lab instructions.

---

## Hardware and Host Context

* **Platform**: Bare-metal server (not a virtual machine)
* **Access method**: SSH (headless, no local GUI)
* **Use case**: Dedicated personal lab server for DevOps and system experimentation

Running the labs on a bare-metal server more closely reflects real-world operational environments than a preconfigured classroom VM.

---

## Operating System

* **Distribution**: Ubuntu Server
* **Environment**: Headless (CLI-only)
* **User account**: Non-root administrative user with `sudo` access

System administration tasks (such as reading `/etc/shadow`) were performed using `sudo` where required. No scripts were run as root by default.

---

## Access and Tooling

### Shell and Access

* SSH access from a local workstation
* Terminal-based workflow using standard Linux utilities

### Development Tools

* **Python**: Installed via Ubuntu system packages
* **Git**: Installed via Ubuntu system packages
* **Editor**:

  * Terminal editors (nano) for initial work
  * VS Code with **Remote SSH** for later editing and navigation

VS Code Remote SSH was used purely as an interface convenience. All code execution, file edits, and Git operations occurred directly on the server.

---

## Python Environment

* **Python version**: Python 3 (system-managed)
* **Package management**: `pip3`
* **Virtual environments**: Optional; not required for the lab

The scripts primarily rely on Python’s standard library. Third-party dependencies (such as `psutil`) were installed globally to match the lab instructions and simplify execution on a server environment.

---

## Version Control Workflow

* Git repository cloned directly onto the server
* Changes committed and pushed from the server
* Branch protection enabled on `main` to prevent accidental direct pushes

This workflow mirrors common DevOps practices where servers maintain working copies of repositories and changes are managed through version control.

---

## Security and Safety Considerations

* Scripts are **read-only** and non-destructive
* No credentials or sensitive configuration values are committed to the repository
* Environment-specific values (e.g., network targets) are externalized via environment variables or ignored files

All scripts were designed to safely inspect system state without modifying configuration, users, or services.

---

## Summary

This environment was intentionally chosen to emphasize realism, safety, and learning. By working on a headless Ubuntu Server with standard system tools, the lab more accurately reflects how Python scripting is used in real DevOps and operations contexts.
