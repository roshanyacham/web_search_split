Feature: Specific Website Search

As a user, I want to search a specific website so that I can find relevant information

Scenario: Entering a website URL
    Given I have opened the app 
    When I enter the URL of a website
    Then the app should be ready to search within that website

Scenario: Performing a search query
    Given I have specified a website to search 
    When I enter a search query
    Then the app should return results from the specified website
 