Feature: Flights

Scenario: Search
    Given I am on "Flights" tab
    When I search for flights from "Melbourne" to "Gold Coast"
    Then I can see multiple listings