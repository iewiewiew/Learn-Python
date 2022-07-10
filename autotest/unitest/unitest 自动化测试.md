[TOC]

<h1 align="center">unitest 自动化测试</h1>

> By：weimenghua
> Date：2022.07.10
> Description：

### 一、unitest核心组件
1. TestCase：一个测试用例；
2. TestSuite：多个测试用例集合；
3. TestRunner：执行test case/test suite；
4. TestFixture：测试脚手架，test fixture表示为了开展一项或多项测试所需要进行的准备工作，以及所有相关的清理操作。举个例子，这可能包含创建临时或代理的数据库、目录，再或者启动一个服务器进程。



### 二、unittest语法
用import unittest 导入unittest模块  
继承unittest.TestCase类，如class xxx（unittest.TestCase）  
每个测试用例执行前执行  
前置：setUp或setUpclass方法  
后置：tearDown或tearDownClass方法  
用例名以test开头，否则unittest不能识别 调用unittest.main()，执行全部测试用例  



### 三、setUp()、tearDown()与setUpClass()、tearDownClass()的区别
setUp()：准备环境，执行每个测试用例的前置条件；
tearDown()：环境还原，执行每个测试用例的后置条件；
setUpClass()：必须使用@classmethod装饰器，所有case执行的前置条件，只运行一次；
tearDownClass()：必须使用@classmethod装饰器，所有case运行完后只运行一次；