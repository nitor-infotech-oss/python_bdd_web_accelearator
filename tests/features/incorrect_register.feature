@wrong_register @smoke
Feature: My Account Smoke Tests

  Scenario Outline: User Registration with invalid data

    Given I register the '<user>' with invalid data
    Then Error Message displayed

    Examples: Credentials
      | user       |
      | wrong_user |

    @incorrect_login_inline
    Scenario: User Registration with invalid data
      Given I register 'test_user' with invalid data
      Then Error Message displayed

