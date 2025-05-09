# Playwright + Pytest Web Automation Project

## Summary of Repo

This repository contains automated **web UI tests** for the [Automation Exercise website](https://automationexercise.com) using **Playwright + Pytest**. The project follows the **Page Object Model (POM)** design pattern, uses **random value generation**, integrates **Allure Report** with screenshots and step descriptions, and includes **parallel test execution** across multiple browsers. The CI/CD pipeline is implemented with **GitHub Actions**, which deploys reports to **GitHub Pages** and sends **Slack notifications** with test results.

## 📄 Latest [Allure Report](https://anna-ruban-ua.github.io/Playwright-Pytest/).

## Requirements

* Python 3.11+
* Playwright
* Pytest
* Allure Commandline
* GitHub (for CI/CD and version control)
* Slack Webhook URL (for notifications)

## Setup Instructions

1. **Clone the repository:**

```sh
git clone https://github.com/Anna-Ruban-ua/Playwright-Pytest
```

2. **Navigate into the project directory:**

```sh
cd Playwright-Pytest
```

3. **Install dependencies:**

```sh
pipenv install
pipenv shell
playwright install
```

4. **Set environment variables:**

Add your Slack Webhook URL as a GitHub Secret:

* `SLACK_WEBHOOK_URL`

## Run Tests

### Run tests in Chromium:

```sh
pytest --browser=chromium --alluredir=allure-results
```

### Run tests in Firefox:

```sh
pytest --browser=firefox --alluredir=allure-results
```

### Run in parallel:

```sh
pytest -n auto --browser=chromium --alluredir=allure-results
```

## Generate Report

### Generate Allure Report:

```sh
allure generate allure-results -o allure-report --clean
```

### Open Allure Report:

```sh
allure open allure-report
```

## CI/CD with GitHub Actions

* `.github/workflows/playwright.yml` contains the pipeline configuration.
* Runs tests on push to `main` branch.
* Publishes Allure Report to GitHub Pages.
* Sends Slack notification with test result and link to the report.

---