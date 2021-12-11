Feature: Flights

Scenario: Search
    Given I am on "Flights" tab
    When I search for flights from "MEL" to "Gold Coast"
    Then I can see multiple flights
    Then I can choose 1st flight