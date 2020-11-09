@account_smoke @smoke
Feature: My Account Smoke Tests

  @correct_register
  Scenario: User Registration with valid data

    Given I register the user with valid data
    Then I verify user registered successfully




