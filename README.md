# FuckTWTB
## 自动体温填报小助手
A small python script for auto reporting body temperature of SUES :P
<br>
向形式主义说“不”
<br>
已更新验证码识别功能
<br>
## 本地部署方法：
<br>
1、安装好Python3.x环境<br>
2、pip install selenium, numpy<br>
3、下载<a href="https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/", target="_blank">chrome driver</a>并解压到python的根目录（或者自行添加安装地址到环境变量PATH）<br>
4、去此电脑 右键->管理->左边的“计划任务程序”->点击右边的创建基本任务，按照导引创建每天定时的任务，并指定程序为autorun.bat，需要创建两个定时任务，一个在上午，一个在下午，间隔时间都是一天<br>
5、将要自动填报的账号和密码，分别每行一个地填入程序同目录下的“acc.txt”和“pwd.txt”（没有就自己创建）
<br>
## 针对滚动验证码的更新： 
<br>
目前已解决问题：<br>
1、模拟鼠标操作点击和拖动 <br>
2、对验证码界面实现模板匹配（模板见trial.png），找到同一行中的两个最佳匹配，计算水平距离差值，然后设定为拖动的offset值<br>
仍有问题：<br>
1、对验证码界面会出现偏差（不知道是不是显示器比例的问题）<br>
2、模板匹配容易漏检<br>
3、对于模板的处理不是很好，不知道有什么更好的边缘检测算法可以扣出那个图像边缘，而不只是边缘家呢<br>
跪求各位大手子出手相助救救孩子，傻逼学校体温填报真他吗恶心人，这种体温都是编一个的，搞得还煞有其事，什么不填报得扣分。<br>
另：示例验证码界面见Test1.png，示例验证码背景（target_img）见target.png，示例模板见trial.png<br>
