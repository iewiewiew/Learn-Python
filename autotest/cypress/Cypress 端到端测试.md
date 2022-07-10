[TOC]

<h1 align="center">Cypress 端到端测试</h1>

> By：weimenghua
> Date：2022.07.10
> Description:

**参考资料**  
[Cypress 官网](https://docs.cypress.io/)    
[Cypress 演示网站](https://example.cypress.io/)


### 一、Cypress 简介
Cypress 是基于 JavaScript 的前端测试工具，它是自集成的，提供了一套完整的端到端测试，无须借助其他外部工具，安装后即可快速地创建、编写、运行测试用例，可以对浏览器中运行的任何内容进行快速、简单、可靠的测试，且对每一步操作都支持回看，不同于其他职能测试 UI 层的前端测试工具，Cypress 允许编写所有类型的测试，覆盖了测试金字塔模型的所有测试类型【界面测试，集成测试，单元测试】。
E2E（end to end）端到端测试是最直观可以理解的测试类型。



### 二、Cypress 搭建
1、生成package.json：创建cypressdemo（自定义）文件夹，进入该文件夹执行命令： npm init -y。将在创建的cypress文件夹下，生成package.json文件，该文件包含了项目所需要的各种模块及项目的各项配置信息（如：名称、版本、依赖、脚本命令等）。进入package.json文件，将name的值cypress改为cypress-dev（可选）。  
2、安装cypress：npm install cypress --save-dev。  
3、安装xpath库：npm install -D cypress-xpath，在cypress/support/index.js文件中增加：require('cypress-xpath')。  
4、在package.json文件中添加:  
```
"scripts": {
    "cypress": "cypress open"
  }
```
scripts字段用来定义脚本命令。  
5、运行cypress：  
方式一：npm run cypress  
方式二：npx cypress open  
方式三：./node_modules/.bin/cypress open  
6、单独执行用例：npm run cypress --spec "cypress/e2e/baidu.cy.js"


### 三、项目结构
- /cypress
  - /fixtures（mock 数据）
    - example.json
  - /integration（测试文件）
    - /examples
      - example.spec.js （一般格式为 *.spec.js,可支持.jsx/.coffee/.cjsx）
  - /plugins（用于配置安装的 插件，task 系统）
    - index.js
  - /support（用于调整 自定义选项）
    - commands.js
    - index.js
  - /screenshots（默认截屏文件夹）
