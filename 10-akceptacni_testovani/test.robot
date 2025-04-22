
*** Test Cases ***

# 1. Test na porovnání čísel

Check That Five Is Greater Than Three

    Should Be True    ${5} > ${3}

# 2. Test rovnosti čísel

Check That Sum Is Correct

    ${result}=    Evaluate    2 + 2

    Should Be Equal As Numbers    ${result}    4

# 3. Test na text – kontrola obsahu

Text Contains Keyword

    Should Contain    This is a test string    test

# 4. Test na text – přesná rovnost

Check Exact Match

    Should Be Equal    Hello    Hello

# 5. Test na text – není obsaženo

Text Does Not Contain

    Should Not Contain    Hello world    goodbye

# 6. Test na délku seznamu

Check List Length

    ${mylist}=    Create List    apple    banana    orange

    Length Should Be    ${mylist}    3

# 7. Test, zda je hodnota v seznamu

Check Item In List

    ${mylist}=    Create List    apple    banana    orange

    List Should Contain Value    ${mylist}    banana

# 8. Test na přetypování a výpočet

Convert To Int And Multiply

    ${val}=    Convert To Integer    7

    ${result}=    Evaluate    ${val} * 3

    Should Be Equal As Numbers    ${result}    21

# 9. Test logické hodnoty

Boolean Test

    ${val}=    Set Variable    ${True}

    Should Be True    ${val}

# 10. Test s proměnnými

Check Concatenation

    ${first}=    Set Variable    Hello

    ${second}=   Set Variable    World

    ${joined}=   Catenate    SEPARATOR=    ${first}    ${second}

    Should Be Equal    ${joined}    HelloWorld
