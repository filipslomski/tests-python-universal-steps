@google
Feature: Google

  @search
  Scenario: Search in google
    Given I am on google page
    When I fill field search_field with text dota
    And I click element search_suggestion with argument dota
    Then I should see element result_stats contains value bigger then 50000

  @login
  Scenario: Login to google A
    Given I am on google page
    When I click element sign_in
    And I fill field email_name with text filip.slomski@gmail.com
    And I fill field email_password with text my_pass
    And I click element account_icon
    Then I should see element logged_user contains value filip.slomski

  @login
  Scenario: Login to google B
    Given I am on google page
    When I click element sign_in
    And I fill field email_name with text karol.slomski@gmail.com
    And I fill field email_password with text my_pass2
    And I click element account_icon
    Then I should see element logged_user contains value karol.slomski
