*** Settings ***
Suite Setup
Suite Teardown
Library           SeleniumLibrary
Library           ../../../../../PycharmProjects/MyProj/programs/conditonalcommands.py

*** Variables ***
${URL}            https://opensource-demo.orangehrmlive.com/login
@{CREDENTIAL}     Admin    admin123
&{LOGIN}          Username=Admin    Password=admin123

*** Test Cases ***
Test1
    [Tags]    Test1
    Open Browser    https://www.youtube.com/    Chrome
    close browser

Test2
    [Tags]    Test2
    open browser    ${URL}    chrome
    Input Text    id=txtUsername    @{CREDENTIAL}[0]
    Input Password    id=txtPassword    &{LOGIN}[Password]
    Click Button    id=btnLogin
    Close Browser

Test3
    [Tags]    Test3
    [Setup]
    open browser    ${URL}    chrome
    Login
    Close Browser
    [Teardown]

Test4
    [Tags]    Test4
    Log To Console    test4 started
    Open Browser    https://facebook.com    chrome
    Close All Browsers
    Log To Console    test4 Completed

Test5
    [Tags]    Test5
    Log To Console    test5 started

SeleniumTest
    [Tags]    Test5
    ${driverobj}=    Conditional Cmds
    log    ${driverobj}
    Close All Browser    ${driverobj}

*** Keywords ***
Login
    Input Text    id=txtUsername    Admin
    Input Password    id=txtPassword    admin123
    Click Button    id=btnLogin

GoToHomePage
    Open Browser    ${URL}    chrome
