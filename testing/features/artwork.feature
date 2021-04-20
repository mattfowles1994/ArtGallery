Feature: Manage Artwork

    Background:
        Given an admin user is logged in

    Scenario: Add Artwork
        When I select add artwork
        When I enter details of an item with the name "The Last Supper"
        Then I see the "The Last Supper" is in the list

    Scenario: Delete an Artwork entry
        When I select "Artworks"
        When I select "Mona Lisa"
        When I select "Delete"
        When I confirm
        Then I see the confirmation

    Scenario: Amend an Artwork entry
        When I select "Artworks"
        When I select "Starry Night"
        When I enter details of an item with the name "Starry Night"
        Then I see the confirmation
        
    Scenario: Add duplicate Artwork
        When I select add artwork
        When I enter details of an item with the name "Starry Night"
        Then I see the error  