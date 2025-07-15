
Feature: User Profiles Data Product

  Scenario: Validate user_profiles table and data quality
    Given the user_profiles model is run
    When the contract tests execute successfully
    Then the row count should be greater than or equal to 1000
