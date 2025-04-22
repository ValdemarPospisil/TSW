*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://localhost:5000

*** Test Cases ***
Add New Task
    Open Browser    ${URL}    firefox
    Input Text    name=task    Napsat test
    Click Button    xpath=//input[@type="submit"]
    Page Should Contain    Odesláno
    Close Browser

Zobrazit Úvodní Text
    Open Browser    ${URL}    firefox
    Page Should Contain    TODO Formulář
    Close Browser
