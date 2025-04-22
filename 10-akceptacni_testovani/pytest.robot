*** Settings ***

Library    Process

*** Test Cases ***

Run Pytest Test

    ${result}=    Run Process    pytest    test_calc.py    stdout=stdout    stderr=stderr

    Log           ${result.stdout}

    Should Contain    ${result.stdout}    5 passed
