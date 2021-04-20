
Feature: Manage Enquiry
    Background:
        Given an admin user is logged in

    Scenario: Asign a user to an Enquiry
        When I select "Enquirys"
        When I select "matt"
        When I enter amended details
        Then I see the confirmation

    Scenario: Delete a User
        When I select "Enquirys"
        When I select "matt"
        When I select "Delete"
        When I confirm
        Then I see the confirmation

 