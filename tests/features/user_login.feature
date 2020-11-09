@user_login @web
Feature: My Account Smoke Tests

  @user_login
  Scenario Outline: User Login with valid data

    Given user log in with '<user>' data
    Then I verify user logged in successfully

    Examples: Credentials
      | user            |
      | super_admin     |
      | dishant         |
      | test_user_nitor |

