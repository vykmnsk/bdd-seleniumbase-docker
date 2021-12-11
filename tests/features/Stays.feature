Feature: Stays

Scenario: Search
    Given I am on "Stays" tab
    When I search for "Gold Coast"
    Then I can see multiple listings
    Then I can pick 1st listing