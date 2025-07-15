
import subprocess
import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('../features/user_profiles.feature')


@given('the user_profiles model is run')
def run_dbt_model():
    result = subprocess.run(['dbt', 'run', '--select', 'user_profiles'], capture_output=True, text=True)
    assert result.returncode == 0, f"DBT run failed: {result.stderr}"


@when('the contract tests execute successfully')
def run_contract_tests():
    result = subprocess.run(['dbt', 'test', '--select', 'user_profiles'], capture_output=True, text=True)
    assert result.returncode == 0, f"DBT tests failed: {result.stderr}"


@then('the row count should be greater than or equal to 1000')
def test_row_count():
    # Custom SQL test result
    result = subprocess.run(
        ['dbt', 'test', '--select', 'test_row_count'],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"Row count test failed: {result.stderr}"
