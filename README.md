# MSES602 – Python Scripting (DevOps Lab)

This repository contains small, beginner-friendly Python scripts, modified
as part of the [MSES602 DevOps labs](https://github.com/RegisUniversity/MSES602_DevOpsUtils.git).

# Labs:
 - [Lab 1](./labs/lab1.md)

 ---

The focus of this repo is on learning and experimentation rather than rigid step-following:

* Understanding how Python can be used for operational and system tasks
* Reading, modifying, and reasoning about scripts instead of treating them as black boxes
* Applying safe, non-destructive checks to inspect system state
* Gradually adopting best practices at a learner’s pace

These scripts are intentionally simple and meant to evolve as understanding improves.

## What’s in this repo?

* `envChk.py` – Displays basic system information such as uptime, CPU usage, and hardware metrics (where available)
* `netmon.py` – Periodically checks connectivity using `ping` (LAN or Internet depending on target)
* `passChk.py` – Audits local Linux user accounts using `/etc/passwd` and `/etc/shadow`

## Prerequisites

* Linux system (tested on Ubuntu Server)
* Python 3 installed from system packages
* Internet access (for installing optional dependencies)

Note: These lab scripts primarily rely on Python’s standard library. A virtual environment
may be used for learning and experimentation but is **not required** for the lab.

## Python dependencies

Some scripts use third-party Python packages (not part of the standard library). Those are
listed in `requirements.txt`.

To install the third-party packages:

```bash
pip3 install -r requirements.txt
```

Notes:

* Only third-party packages appear in `requirements.txt`.
* Standard library modules (such as `os`, `pwd`, or `subprocess`) do not need to be installed.

## Setup (optional: virtual environment)

Using a virtual environment is optional and provided here as a best-practice learning option.

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you choose not to use a virtual environment, you may install required packages globally
(e.g., `pip3 install psutil`) as shown in the lab instructions.

## Run the scripts

From the repository directory:

### 1) Environment check

```bash
python3 envChk.py
```

Notes:

* Uses `psutil` (if installed)
* Some metrics (such as temperatures) depend on hardware and permissions

### 2) Network monitor

```bash
python3 netmon.py
```

Notes:

* Uses `ping` to test a configured target (for example, `8.8.8.8` for Internet or your gateway IP for LAN)
* Logs 4 pings each cycle (similar to running `ping -c 4 <host>`)
* The sleep interval is controlled by a constant inside the script

### 3) Account audit (Linux only)

```bash
sudo python3 passChk.py
```

Notes:

* Reads `/etc/passwd` and `/etc/shadow`
* Requires `sudo` to inspect password state
* **Does not modify users or passwords** (read-only audit)
* Intended to highlight weak account characteristics for learning purposes

## Editor notes (not required for the lab)

* Any terminal-based editor (nano, vim) is sufficient
* VS Code and Remote SSH are optional conveniences
* All scripts can be run directly from an SSH session

## Learning intent

This repository reflects an experimental, learner-focused approach encouraged by the course:

* Scripts may differ from the original lab examples
* Improvements are made to better reflect modern Linux systems
* The emphasis is on understanding *what the code does and why*, not just producing output
