[TOC]

<h1 align="center">PageObject 设计模式</h1>

> By：weimenghua
> Date：2022.07.10
> Description：



### PageObject 原理
Page Object是一种程序设计模式，将面向过程转变为面向对象(页面对象)，将测试对象（按钮、输入框、标题等）及单个的测试步骤封装在每个Page对象中，以page为单位进行管理。  
类的属性：元素定位。  
类的行为：元素的操作。  
测试用例：调用所需页面中对象的行为组成测试用例。  