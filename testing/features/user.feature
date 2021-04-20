
Feature: Manage User

    Background:
        Given an admin user is logged in

    Scenario: Add User
        When I select add user
        When I enter details of an item with the name "John"
        Then I see the "John" is in the list

    Scenario: Delete a User
        When I select "Users"
        When I select "mattCMS"
        When I select "Delete"
        When I select "Delete"
        When I confirm
        Then I see the confirmation

    Scenario: Amend an User entry
        When I select "Users"
        When I select "mattCMS"
        When I enter amended details
        Then I see the confirmation

   Scenario: Add User with password and username the same
        When I select add user
        When I enter same details for username and password
        Then I see the error  