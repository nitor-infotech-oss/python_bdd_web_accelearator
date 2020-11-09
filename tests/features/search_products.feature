@search_smoke @smoke
Feature: Search Product

  Scenario Outline: Search Product and add to cart

    Given I navigate to 'home' page
    When I search for the '<product>'
    Then I verify the '<product>' search result

    Examples: Search item
      | product            |
      | t shirt            |
      | beanie             |
      | v neck             |
      | album              |
      | beanie with logo   |
      | hoodie             |
      | belt               |
      | hoodie with logo   |
      | hoodie with zipper |
      | cap                |
