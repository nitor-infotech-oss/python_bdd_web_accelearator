@wrong_login @account_smoke
Feature:Incorrect Login Smoke Test

  Scenario Outline: User Login with invalid data
    Given user log in with '<user>' data
    Then Error Message displayed

    Examples: Credentials
      | user       |
      | wrong_user |
      | test_user  |



