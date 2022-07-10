*** Settings ***
Library           SeleniumLibrary
Library           RequestsLibrary
Library           DatabaseLibrary
Library           Dialogs
Library           String
Library           D:\\software\\\PythonProjects\\\Learn-Python\\autotest\\robotframework\\robotproject\\robot_base.py


*** Variables ***
${LOGIN_URL}      https://gitee.com/

*** Keywords ***
Open Brower To Home Page
    log    "自定义关键字"
    OPEN BROWSER    ${LOGIN_URL}    Chrome
    MAXIMIZE BROWSER WINDOW
    Sleep    5s
    Close Browser

robot_keyword
    log    "执行自定义关键字"
    Open Brower To Home Page

*** Test Cases ***
robot_variable
    ${var1}     Set Variable    变量1
    log     "变量"${var1}
    ${var2}     Set Variable If    'a'=='a'     变量true      变量false
    log     "变量"${var2}

robot_setup_teardown
    log    "执行用例前后"
    [Setup]    log    "用例执行前"
    ${time}    Get Time
    log    "获取时间" ${time}
    [Teardown]    log    "用例执行后"

robot_mysql
    log    "操作数据库"
    Connect To Database Using Custom Params    pymysql    database='dbname', user='root', password='root', host='127.0.0.1', port=3306    #创建数据库链接
    ${result}    query    select * from dbname.demo    #Query查询语句返回查询语句的查询结果
    log    "查询结果"${result}
    log    "查询第一行第二个字段值"${result}[0][1]
    ${result1}    Row Count    select * from dbname.demo    #Row Count查询语句返回查询语句的查询结果行总数
    log    "查询结果行总数"${result1}
    Disconnect From Database    #断开数据库链接

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
    Sleep    3s
    Maximize Browser Window
    Input Text    id=kw    robot教程
    Sleep    2s
    Click Button    id=su
    Sleep    5s
    Close Browser

robot_py
    ${test}  test_method    1   2
    log     ${test}

