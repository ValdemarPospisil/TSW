*** Test Cases ***

Should Be Equal Example

    ${a}=    Set Variable    42

    ${b}=    Evaluate    6 * 7

    Should Be Equal As Numbers    ${a}    ${b}


*** Settings ***

Library    String

*** Test Cases ***

Replace Substring Example

    ${text}=    Set Variable    Hello student

    ${new}=     Replace String    ${text}    student    teacher

    Should Be Equal    ${new}    Hello teacher


*** Settings ***

Library    Collections

*** Test Cases ***

List Contains Value Example

    ${fruits}=    Create List    apple    banana    cherry

    List Should Contain Value    ${fruits}    banana


*** Settings ***

Library    Dialogs

*** Test Cases ***

Ask User For Name

    ${name}=    Get Value From User    Please enter your name:

    Log    You entered: ${name}


*** Settings ***

Library    JSONLibrary

Library    Collections

*** Test Cases ***

Get Value From JSON Example

    ${json}=         Convert String To Json    {"name": "Alice", "age": 30}

    ${age_list}=     Get Value From Json       ${json}    $.age

    ${age}=          Get From List             ${age_list}    0

    Should Be Equal As Numbers    ${age}    30
