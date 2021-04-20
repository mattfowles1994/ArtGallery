
Feature: Manage News

    Background:
        Given an admin user is logged in

    Scenario: Add News
        When I select add news
        When I enter details of an item with the name "new"
        Then I see the "new" is in the list

    Scenario: Delete News
        When I select "News"
        When I select "Scream"
        When I select "Delete"
        When I confirm
        Then I see the confirmation

    Scenario: Amend a News entry
        When I select "News"
        When I select "Scream"
        When I enter amended details
        Then I see the "new" is in the list

    Scenario: Add News with no name
        When I select add news
        When I enter some details of an item
        Then I see the error