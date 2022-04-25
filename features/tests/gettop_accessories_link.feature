# Created by trand at 4/24/2022
Feature: Test for Accessories page
  # Enter feature description here

  Scenario:  User can view Cases&protections product page
    Given Open Gettop home page
    When Hover over Accessories
    Then Click on Cases&protections link
    And Verify 404 message is present