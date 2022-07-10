*** Settings ***
Library           SeleniumLibrary
Library           RequestsLibrary
Library           Collections


*** Test Cases ***
robot_login
    #POST Response : url=http://192.168.80.1:9527/admin/auth/login
    #status=200, reason=OK
    #headers={'X-Powered-By': 'Express', 'set-cookie': 'JSESSIONID=cdc17710-36a9-4613-bd8d-11495293f045; Path=/; HttpOnly; SameSite=lax, rememberMe=deleteMe; Path=/; Max-Age=0; Expires=Tue, 14-Jun-2022 06:12:02 GMT', 'vary': 'accept-encoding', 'content-encoding': 'gzip', 'content-type': 'application/json;charset=UTF-8', 'transfer-encoding': 'chunked', 'date': 'Wed, 15 Jun 2022 06:12:02 GMT', 'connection': 'close'}
    #body={"errno":0,"data":{"adminInfo":{"nickName":"admin123","avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"},"token":"cdc17710-36a9-4613-bd8d-11495293f045"},"errmsg":"成功"}
    #登录接口
    &{headers}=    Create Dictionary    Content-Type=application/json    #设置请求头
    Create Session    api    http://192.168.80.1:9527    headers=${headers}    #创建会话
    ${body}    Create Dictionary    username=admin123    password=admin123    code=    #定义传参
    ${resp}    POST On Session    api    /admin/auth/login    json=${body}    #发起post请求，并将响应赋值到${resp}
    Should Be Equal As Strings    ${resp.status_code}    200    #判断返回结果是不是200
    should not be empty    ${resp.json()["data"]}
    Set suite Variable    ${token}    ${resp.json()["data"]["token"]}    #使用范围：使用此关键字设置的变量在当前执行的测试套件的范围内随处可用
    log    ${resp}    #打印响应
    log    ${resp.status_code}    #打印响应状态码
    log    ${resp.content}    #打印响应内容
    log    ${resp.json()["data"]}    #打印data
    log    ${resp.json()["data"]["token"]}    #打印token
    log    ${resp.json()["data"]["adminInfo"]["nickName"]}    #打印nickName
    log    "打印响应头："${resp.headers}
    log    "打印响应体："${resp.json()}    #将响应转换为json
    log    "打印token："${token}

robot_list
    log    "商品管理 > 商品列表：查询"
    log    "获取token "${token}
    &{headers}=    Create Dictionary    Cookie=JSESSIONID=${token}    X-Litemall-Admin-Token=${token}
    Create Session    api    http://192.168.80.1:9527    #创建会话
    ${resp}    GET On Session    api    /admin/category/list    headers=${headers}    #发起get请求，并将响应赋值到${resp}
    log    ${resp.json()}
    Delete All Sessions    #删除所有与服务器连接

robot_create
    log    "推广管理 > 优惠券管理：新增"
    log    "获取token "${token}
    &{headers}=    Create Dictionary    Cookie=JSESSIONID=${token}    X-Litemall-Admin-Token=${token}    content-type=application/json;charset=UTF-8
    ${data}    Set Variable    {"name":"robot","desc":"hah","tag":"1","total":0,"discount":0,"min":0,"limit":1,"type":0,"status":0,"goodsType":0,"goodsValue":[],"timeType":0,"days":0,"startTime":null,"endTime":null}
    Create Session    api    http://192.168.80.1:9527    #创建会话
    ${resp}    POST On Session    api    /admin/coupon/create    data=${data}    headers=${headers}
    log    "打印响应体"${resp.json()}


