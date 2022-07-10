*** Settings ***
Library           SeleniumLibrary
Library           RequestsLibrary

*** Test Cases ***
robot_interface
    log    "接口测试demo"
    Create Session    api    http://www.baidu.com
    ${data}    GET On Session    api    /
    log    ${data}

robot_ui
    log    "ui测试demo"
    Open Browser    https://www.baidu.com    Chrome
    ${title}    Get Title
    log    "获取标题"${title}
    Sleep    1s
    Maximize Browser Window
    Input Text    id=kw    robot教程
    Sleep    1s
    Click Button    id=su
    Sleep    1s
    Close Browser