*** Keywords ***
Addition
    [Arguments]    ${arg1}    ${arg2}
    ${Addition}=    Evaluate    ${arg1}+${arg2}
    Log    ${Addition}

Substraction
    [Arguments]    ${arg1}    ${arg2}
    ${Substraction}=    Evaluate    ${arg1}-${arg2}
    log    ${Substraction}

Multiplication
    [Arguments]    ${arg1}    ${arg2}
    ${Multiplication}=    Evaluate    ${arg1}*${arg2}
    Log    ${Multiplication}

Division
    [Arguments]    ${arg1}    ${arg2}
    ${Division}=    Evaluate    ${arg1}/${arg2}
    log    ${Division}
