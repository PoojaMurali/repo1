*** Settings ***
Library           Student.py    Pooja    M    pooja@gmail.com

*** Test Cases ***
StudentClass
    [Template]
    [Timeout]
    ${frist_name}    ${last_name}    ${email_id}=    Student.Get Student Details
    ${marks}=    Student.Get Marks    90    80    80
    ${total}=    Student.Get Total
    ${average}=    Student.Get Average
