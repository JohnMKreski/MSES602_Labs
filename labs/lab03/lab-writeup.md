# Lab 3 – Continuous Integration with Git, Jenkins, and SonarQube

## Overview

This lab focused on implementing a basic **Continuous Integration (CI)** workflow by connecting **GitHub**, **Jenkins**, and **SonarQube**. The goal was to observe how a code commit triggers an automated pipeline that performs dependency installation, test execution, and static code analysis.

Unlike Lab 2, which centered on provisioning infrastructure with Ansible, this lab emphasized automated validation of application code after changes are pushed to source control. The objective was not only to complete a successful build, but also to interpret build results and identify quality signals surfaced by the pipeline.

---

## Environment and Setup

* Ubuntu Server (headless)
* Jenkins running as a systemd service (installed via Ansible in Lab 2)
* SonarQube installed and configured in Lab 2
* GitHub repository: `MSES602_HelloWorld`
* Node.js environment available on the Jenkins host

All work was performed via SSH and Jenkins web interface access.

---

# SonarQube Installation and Playbook Adjustments (From Lab 2)

Before this CI workflow could function, SonarQube had to be installed and configured during Lab 2 using Ansible automation.

### Playbook Enhancements

The following modifications were made to the Lab 2 playbooks to support SonarQube:

* Installed required Java runtime (Sonar dependency)
* Downloaded and configured SonarQube server
* Configured service permissions and ownership
* Ensured SonarQube runs on port `9000`
* Verified service startup and systemd integration

Special attention was given to:

* Proper package installation order (Java before Sonar)
* Service enablement at boot
* Local firewall/network accessibility
* Validating SonarQube availability in browser

SonarQube was confirmed accessible at:

```
http://127.0.0.1:9000
```

![sonar running](assets/sonar_running.jpg)

This provisioning work enabled Jenkins integration in this lab.

---

# Git Commit and Triggering the Build

Within the project directory:

```
/home/osboxes/projects/MSES602_HelloWorld
```

The following Git commands were executed:

```
git status
git add .
git commit -m "Change name to Bill Masters"
git push origin master
```

After pushing to GitHub, Jenkins automatically detected the change and triggered a new build.

![git commit](assets/git_commit.jpg)

---

# Jenkins Build Execution

The Jenkins job output confirmed:

```
Started by an SCM change
```

The build process performed the following steps:

* Checked out the latest revision from GitHub
* Executed `npm install`
* Ran `npm test`
* Executed SonarScanner analysis
* Attempted to publish JUnit test results

![jenkins build start](assets/jenkins_build_start.jpg)

---

# SonarQube Static Analysis

SonarScanner successfully analyzed the project and uploaded results to the SonarQube server.

Console output confirmed:

```
ANALYSIS SUCCESSFUL
EXECUTION SUCCESS
```

The project dashboard was visible in the Sonar UI.

![sonar dashboard](assets/sonar_dashboard.jpg)

This verified:

* Jenkins-to-Sonar connectivity
* Successful project indexing
* Static analysis execution
* Quality data publication

---

# Build Result: UNSTABLE

Although the pipeline completed successfully, Jenkins marked the build as:

```
Finished: UNSTABLE
```

This occurred due to the JUnit publishing step:

```
Build step 'Publish JUnit test result report' changed build result to UNSTABLE
```

The UNSTABLE status indicates:

* Test reports were missing, incomplete, or contained failures
* The pipeline executed but did not meet quality thresholds

Importantly, the build did not fail entirely — it surfaced quality concerns for review.

![jenkins unstable](assets/jenkins_unstable.jpg)

---

# Observations and Technical Findings

## Node.js Version Mismatch

SonarScanner reported:

```
Only Node.js v14.17 or later is supported, got 10.19
```

This indicates that the Jenkins host is running an outdated Node version. While the scan completed, JavaScript rules may not have executed fully.

This highlights the importance of toolchain version alignment in CI environments.

---

## Dependency Vulnerabilities

During `npm install`, the following was reported:

```
found 20 vulnerabilities (4 low, 1 moderate, 15 high)
```

This demonstrates how CI pipelines surface dependency risks early in the development lifecycle.

---

# Jenkins Workspace Review

Jenkins builds occur inside an isolated workspace located at:

```
/var/lib/jenkins/workspace/Hello World
```

The workspace contains:

* Checked-out source code
* Installed dependencies
* Sonar scanner artifacts
* Build-generated files

Exploring this directory reinforced how Jenkins separates build environments from developer systems.

![workspace view](assets/workspace_view.jpg)

---

# Reflection

This lab demonstrated how Continuous Integration connects version control, automation servers, and quality analysis tools into a single feedback loop.

Key takeaways include:

* Infrastructure automation (Lab 2) enables CI workflows
* Every Git commit can trigger automated validation
* Static analysis integrates directly into the pipeline
* Quality issues are surfaced immediately
* Environment misconfiguration can impact analysis accuracy

The UNSTABLE build result was not a failure, but rather a valuable feedback signal indicating areas for improvement.

Together, Labs 2 and 3 illustrate the relationship between **provisioning tools (Ansible)** and **continuous automation platforms (Jenkins + SonarQube)** in a DevOps workflow.

---

# TODO – Improvements for Stability

* [ ] Upgrade Node.js to version 14.17 or later
* [ ] Verify and correct JUnit test report file path
* [ ] Ensure tests generate valid XML reports
* [ ] Address npm vulnerabilities (`npm audit fix`)
* [ ] Confirm latest Git commit is being built
* [ ] Re-run pipeline and validate STABLE / SUCCESS status

---

# References

* Jenkins Documentation: [https://www.jenkins.io/doc/](https://www.jenkins.io/doc/)
* SonarQube Documentation: [https://docs.sonarsource.com/](https://docs.sonarsource.com/)
* Git Documentation: [https://git-scm.com/docs](https://git-scm.com/docs)
* Node.js Documentation: [https://nodejs.org/en/docs](https://nodejs.org/en/docs)

---

## AI Additional Tools

ChatGPT and Microsoft Copilot were used as supplemental tools for troubleshooting, documentation refinement, and clarification of CI/CD concepts, consistent with modern DevOps workflows.

* OpenAI, ChatGPT: [https://openai.com/chatgpt](https://openai.com/chatgpt)
* Microsoft Copilot: [https://learn.microsoft.com/en-us/copilot/](https://learn.microsoft.com/en-us/copilot/)
