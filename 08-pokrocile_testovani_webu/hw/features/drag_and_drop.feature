Feature: Drag and Drop functionality

Scenario: Dragging element to target
    Given I open the drag and drop demo page
    When I switch to the iframe
    And I drag the source element to the target
    Then the target should show "Dropped!"
