@cms
Feature: Manage Artwork


  Scenario: Add Artwork
    When I select add artwork
    And I add a piece of artwork with the name "Girl With a Pearl Earring"
    Then I see "the artwork "Girl With a Pearl Earring" was added successfully." message

