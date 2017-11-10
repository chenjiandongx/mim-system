
# mim-system 简介
### (Medical information management system) 医疗信息管理系统
本系统为本学期数据库课程设计作业，主要模拟系统后台对数据进行管理的操作。数据库使用的是 sqlite，网站总体使用的是 [Flask](http://flask.pocoo.org/Flask) + [Bootstrap](http://getbootstrap.com)，并部署在 [Heroku](https://www.heroku.com)

#### 网站预览

![网站预览](https://github.com/chenjiandongx/mim-system/blob/master/images/screenshot.gif)

#### 管理员账户

* 账号：Admin
* 密码：default

#### 系统关系数据表

![关系图](https://github.com/chenjiandongx/mim-system/blob/master/app/static/relationship.png)

#### 系统具备的功能模块

* 信息查询功能模块：查询顾客、经办人、药品信息（支持按编号或名称查询，或者使用 `#all` 查询全部）
* 信息录入功能模块：录入顾客、经办人、药品信息
* 信息删除功能模块：删除顾客、经办人、药品信息（存在主外键限制）
* 信息修改功能模块：修改顾客、经办人、药品信息
* 信息浏览功能模块：浏览顾客、经办人、药品信息
* 数据报表功能模块：查看顾客、经办人、药品报表信息（使用图形表示）
* 用户管理与用户登陆功能模块
