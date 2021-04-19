
Feature: Manage Artwork

    Background:
        Given an admin user is logged in

    Scenario: Add Artwork
        When I select add artwork
        When I add a piece of artwork with the name "The Last Supper"
        Then I see the "The Last Supper" is in the list

