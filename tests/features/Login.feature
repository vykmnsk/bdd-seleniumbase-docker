Feature: Login

Scenario: Unsuccessful Login
    Given I don't have valid username and password
    When I try to sign in
    Then I get error "Email and password don't match. Try again."


