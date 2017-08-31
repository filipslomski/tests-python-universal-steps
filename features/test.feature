Feature: google search
  @google
  Scenario: Search in google
    Given I am on google page
    When I search for dota
    And I select dota 2 from search suggestions
    Then I should see over 50000 results

  Scenario: Search in google
    Given I am on google page
    When I fill field with text
    And I click search button
    And I click element with argument
    Then I should see element contains value