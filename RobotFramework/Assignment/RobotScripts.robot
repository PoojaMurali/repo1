*** Settings ***
Resource          resource_file.robot
Library           func_process.py
Library           string
Library           ReverseString.py

*** Variables ***
@{Numbers}        one    two    three    four    five
&{DictStud}       name=abc    place=xyz    degree=be
${string}         danfoss

*** Test Cases ***
RobotTestCase
    Addition    ${10}    ${10}
    Substraction    ${20}    ${10}
    Multiplication    ${10}    ${10}
    Division    ${10}    ${2}

FunctionOperation
    ${function add}=    func_process.Add    5    3
    log    sum of two numbers ${function add}
    ${function sub}=    func_process.Sub    ${3}    ${1}
    log    Difference ${function sub}
    ${function mul}=    func_process.Mul    ${9}    ${3}
    log    multiplication ${function mul}
    ${function div}=    func_process.Div    ${1103}    ${2}
    log    Division ${function div}

Slicing&Conversion
    [Timeout]
    log    ${Numbers}[0:1]
    log    ${Numbers}[::-1]
    log    ${Numbers}[1:3]
    ${length}=    Get Length    ${Numbers}
    Run Keyword If    '${length}'>='3'    log    Length is greater than 3
    Run Keyword If    '${length}'<'3'    log    length is less than 3
    ${converttostring}=    Evaluate    "".join(${Numbers})

forloopusinglist
    Comment    ${check}=    Set Variable    False
    FOR    ${i}    IN    @{Numbers}
        Log    ${i}
        ${check}=    Set Variable If    '${i}'=='five'    True    False
        Exit For Loop If    '${check}'=='True'
    END
    log    checkoutput ${check}
    Run Keyword If    '${check}'=='True'    log    Five is Present
    Run Keyword If    '${check}'=='False'    Fail    five not present

Reverse of string
    log    ${string}[::-1]
    log    ${string}[0]
    ${stringrev}=    ReverseString.Strrev    Danfoss
    log    ${stringrev}

Dictionary
    FOR    ${key}    ${value}    IN    &{DictStud}
        Log    Key is '${key}' and value is '${value}'.
    END
