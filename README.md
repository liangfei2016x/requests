这个文件主要是用来练习requests和BeautifilSoup实现一些简单的爬虫程序


study_requests.py 主要写了一些requests的一些主要用法。参考：http://docs.python-requests.org/en/master/


BeautifulSoup 参考:https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html


wheather_test.py,fanyi_test.py使用requests访问他们各自的API 实现查看天气和翻译功能

zhihu.py 利用requests实现用cookie登录知乎，如果有验证码，取出验证码实现登录。

tripadvisor.py 用requests和BeautifulSoup 解析猫途鹰网站 纽约的所有景点 和 一些基本信息。

douban_250.py 解析出豆瓣排名前250的电影的名字。并写入movie.text文件
mtime.py 解析出时光网上票房前100的电影的基本信息。并下载相关图片，存入 picture文件夹中

baidu.py 用urllib解析百度，并用cookie方式登录。
