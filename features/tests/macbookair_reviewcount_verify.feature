# Created by trand at 4/26/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Review count should reflect the current number of reviews.
    Given Open Gettop home page
    When Hover over MAC
    Then Click on Mabook Air
    Then verify review count to match with number of reviews