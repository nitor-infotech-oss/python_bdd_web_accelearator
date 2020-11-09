@order_place @smoke
Feature: Order Placement

  Scenario: New user place order without an existing account

    Given I navigate to 'home' page
    When I add products to the cart
    And I checkout the cart list page
    Then I verify the details on order confirmation page




