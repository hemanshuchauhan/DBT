
# DBT + Pytest-BDD Automation Framework for Data Pipeline Testing

## Overview
This is a boilerplate project demonstrating how to implement a **BDD-style automated test framework** using **dbt** and **pytest-bdd** for data pipelines on **BigQuery/GCP**.

It covers:
- dbt model + source schema and contract tests
- Custom SQL test (row count)
- BDD feature file and step definitions
- GitHub Actions CI workflow example

## Setup Instructions

### Prerequisites
- Python 3.7+
- dbt-bigquery adapter installed
- Access to Google Cloud BigQuery with permissions
- Google Application Credentials set via `GOOGLE_APPLICATION_CREDENTIALS` env var

### Install Dependencies
```bash
pip install dbt-bigquery pytest pytest-bdd
```

### Run Tests Locally
```bash
pytest tests/test_user_profiles.py
```

### Notes
- Make sure your `dbt_project.yml` is configured to point to your BigQuery project/dataset
- Define your source table `raw.user_profiles` in `dbt_project.yml` or via `sources` config
- You can extend tests and features for other models following this pattern

## CI Integration

A sample GitHub Actions workflow is provided in `.github/workflows/dbt-tests.yml`

---
