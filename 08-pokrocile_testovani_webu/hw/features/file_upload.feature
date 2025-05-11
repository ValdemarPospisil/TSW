Feature: File Upload functionality

Scenario: Uploading a text file
    Given I open the file upload page
    When I select the file "/home/valdemar/Documents/4.Semestr/SWI/CodeReviews/coderabbit_haskell.txt"
    And I click the upload button
    Then I should see the "File Uploaded!" message
