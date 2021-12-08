# FuckTWTB
## 自动体温填报小助手
A small python script for auto reporting body temperature of SUES :P
<br>
向形式主义说“不”
<br>
已更新验证码识别功能
<br>
# 本地部署方法：
<br>
1、安装好Python3.x环境<br>
2、pip install selenium, numpy<br>
3、下载<a href="https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/", target="_blank">chrome driver</a>并解压到python的根目录（或者自行添加安装地址到环境变量PATH）<br>
4、去此电脑 右键->管理->左边的“计划任务程序”->点击右边的创建基本任务，按照导引创建每天定时的任务，并指定程序为autorun.bat，需要创建两个定时任务，一个在上午，一个在下午，间隔时间都是一天<br>
5、将要自动填报的账号和密码，分别每行一个地填入程序同目录下的“acc.txt”和“pwd.txt”（没有就自己创建）
