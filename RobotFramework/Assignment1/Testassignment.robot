*** Settings ***
Library           AssignmentClass.py    Pooja    Murali    hpooja751@gmail.com

*** Test Cases ***
testcase
    AssignmentClass.Get Marks    ${50}    ${80}    ${80}
    AssignmentClass.Total
    AssignmentClass.Average
