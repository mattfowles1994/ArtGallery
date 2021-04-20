
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

    Scenario: Amend an User entry
        When I select "News"
        When I select "Scream"
        When I enter amended details
        Then I see the "new" is in the list