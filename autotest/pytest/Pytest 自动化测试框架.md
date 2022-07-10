[TOC]

<h1 align="center">Pytest 自动化测试框架</h1>

> By：weimenghua
> Date：2022.07.10
> Description：


**参考资料**
[pytest 官方文档](https://docs.pytest.org/en/latest/contents.html)



## 一、pytest 简介
pytest 是 Python的测试框架，类似于 unittest，但比 unittest 更简洁，直接，易上手，功能更强大，且可兼容 unittest 的代码。
它可以实现，执行用例时跳过某些用例、用例执行失败后可重新执行、对执行失败的用例进行标记等。
pytest 有丰富的第三方插件，比较好用的如 pytest-selenium（集成selenium）、pytest-html（完美html测试报告生成）、pytest-rerunfailures（失败case重复执行）、pytest-xdist（多CPU分发）等。



## 二、环境搭建
```
1、安装pytest
pip install pytest
   
2、查看pytest版本
pytest --version
```



## 三、目录结构
1. config：配置文件
2. enums：枚举类
3. logs：日志文件
4. report：测试报告
5. testcase：测试用例
6. testdata：测试数据
7. utils：工具类
8. run.py：启动脚本



## 四、测试用例
### 编写规则
**文件、类及函数命名及书写规则**
1. 使用pytest，文件、类、函数不能随意命名，必须按照其规则进行命名，否则pytest无法识别
2. 测试文件以test_开头（以_test结尾也可）
3. 测试类以Test开头，注意，Test首字母要大写
4. 测试类名称后面直接跟冒号，而不能有()
5. 测试类不能带有 __init__ 方法
6. 测试类里的每个函数都必须有参数(self)
7. 测试函数以test_开头，注意，这时首字母要小写
8. 断言使用基本的assert即可


### 执行测试
```
1、pytest.main(args,plugins)
pytest.main(['-v','-s'])
参数 -v : 显示测试的详细参数信息
参数 -s: 显示测试执行的输出信息

2、指定执行的测试目录  
pytest 测试目录路径：pytest testcase/，pytest 会执行指定目录路径下所有的测试用例

3、指定执行的测试文件  
pytest 测试文件路径：pytest testcase/test_demo.py，pytest 会执行指定测试文件中下所有的测试用例

4、指定执行的测试类  
pytest 测试文件::测试类：pytest testcase/test_demo.py::TestClass，pytest 会执行指定测试类里面所有的测试用例

5、指定执行的测试用例  
pytest 测试文件::测试类::测试方法：pytest testcase/test_demo.py::TestClass::test_method，pytest 会执行指定的测试方法
```

### 测试报告

```
3. win安装allure  
[allure下载地址](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/)   
下载allure-commandline-2.9.0.zip  
解压后将allure/bin添加到系统变量中，在cmd中输入allure验证是否安装成功。

4. mac安装allure
brew install allure
allure --version
pip install allure-pytest

5. 生成allure测试报告
在测试文件的当前路径执行如下命令执行测试用例：pytest test_allure.py --alluredir ./allure
执行如下命令生成测试报告（自动打开浏览器）：allure serve allure
清除allure历史数据：pytest --alluredir allure --clean-alluredir
在控制台执行pytest文件：pytest pytest_allure.py

6. 生成pytest-html测试报告
pip install pytest-html
pytest --html=./report.html
```

### 命令行参数

在命令行中使用pytest来运行测试时，它会自动查找符合规则的测试文件并运行测试。
常用的pytest命令行选项和参数：
-v：详细输出测试结果，包括每个测试用例的名称和状态。
-s：输出标准输出流和标准错误流，通常用于调试测试用例。
-k：选择要运行的测试用例，可以使用表达式来过滤测试用例名称。
-m：使用标记来选择要运行的测试用例，可以使用表达式来过滤测试用例的标记。
-x：在第一个失败的测试用例后停止测试运行。
-f：在失败的测试用例后停止测试运行。
--fixtures：显示可用的测试固件。
--cov：计算代码覆盖率，并生成报告。
--pdb：在测试失败时启动Python调试器（pdb）。
--capture：控制标准输出流和标准错误流的捕获方式，可以设置为no、sys或fd。

### 前置后置
[setup_teardown](./testdemo/test_setup_teardown.py)

### 配置文件

pytest.ini文件是pytest的主配置文件，可以改变pytest的默认行为。

pytest.ini的放置位置：一般放在项目工程的根目录（即当前项目的顶级文件夹下）。

pytest.ini的作用：指定pytest的运行方式。（在cmd输入pytest后，会读取pytest.ini中的配置信息，按指定的方式去运行）



## 五、零散记录（待调整）

```
在第一次（或N次）失败后停止
pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures

Python 调试器
pytest --pdb

查看活跃的插件
pytest --trace-config

获取最慢的10个用例的执行耗时
pytest --durations=10

多进程运行case
pip install -U pytest-xdist
pytest test_se.py -n <num>

重试运行case
pip install -U pytest-rerunfailures
pytest test_se.py --reruns <num>

输出覆盖率的html报告
pip install pytest-cov
pytest -vv --cov=./ --cov-report=html
open htmlcov/index.html 
```

### Pytest Exit Code 含义清单

Exit code 0 所有用例执行完毕，全部通过
Exit code 1 所有用例执行完毕，存在Failed的测试用例
Exit code 2 用户中断了测试的执行
Exit code 3 测试执行过程发生了内部错误
Exit code 4 pytest 命令行使用错误
Exit code 5 未采集到可用测试用例文件

### 核心思想
1. 发起http请求
2. 拿到响应做断言
