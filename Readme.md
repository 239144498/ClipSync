ClipSync
--------

### 📃 引言

这个项目是为了解决不同平台同步剪贴板数据过于繁琐的问题，很多人应该都深有体会。

### 🍭剪贴板同步-传统与自动化对比

> *从下文中可以看出使用 ClipSync在办公等场景中，效率上得到质的提升！*

#### 🐢传统剪贴板传输方式（10个步骤）：

设备A：

1. 复制内容 🕑
2. 找到聊天软件 👇
3. 登录账号    👇
4. 选择联系人  👇
5. 粘贴       👇
6. 发送内容给设备B ✔

设备B：

1. 找到聊天软件 👇
2. 登录账号 👇
3. 选择联系人 👇
4. 复制内容 ✔

传统传输方式，如果设备A需要发送给n个设备那么上面步骤需要重复n次。

#### ✨ClipSync传输方式（仅需1步）：

设备A：

1. 复制内容🕑

设备B：

1. 自动同步✔

采用ClipSync传输，设备A需要发送给n个设备只需要1次。

🌿简介
------

剪贴板全平台同步服务采用MQTT通信协议，可以很好做到多设备连接并且同步剪贴板内容。
ClipSync服务主打无感同步，不需要用户手动操作，操作配置界面在Web端进行。

🎁ClipSync优势
--------------

```text
免费开源
兼容全平台：
    Windows、Linux、MacOS
    Android、IOS
多设备快速连接
无感同步
支持非局域网同步（不需要连接同一个wifi）
可扩展性强（提供API调度）
```

📰使用教程
----------

### ✈️安装剪贴板依赖

#### IOS

越狱后直接使用，不越狱可以通过快捷指令等途径完成

#### Android

安装python第三方库

```cmd
pip install pyjnius kivy
```

#### Windows

安装python第三方库

```cmd
pip install pywin32
```

#### Linux

*sudo install和 pip install都是二选一*

`sudo apt-get install xsel`来安装xsel工具。  
`sudo apt-get install xclip`来安装xclip工具。  
`pip install gtk`来安装gtk Python模块。  
`pip install PyQt5`来安装PyQt5 Python模块。  

### MacOS

直接使用

### 🚀安装ClipSync服务

```cmd
git clone https://github.com/239144498/xxx.git

pip install -r requests

python main.py

# 后台运行：根据使用的操作系统，搜索关键字 python程序+后台运行。
```

### 📢注意事项

* 项目免费通过我搭建的Eclipse Mosquitto提供通信服务（申明：服务器不会转存消息）
* 在src/config/config.ini 修改服务配置
* 把config.ini文件中的[MQTT_CLIENT]subscribe和publish修改成唯一名称，例如：[MQTT_CLIENT]subscribe=ClipSync-xxxxx，不改名称会导致其他人也可以接收到你的剪贴板内容。只在需要同步的设备中设置相同的名称。
* 测试环境有限，遇到问题可以发起Issues
* 期待更多人加入其中，可以PR或者写教程文档等不限

### 🧊感言

在这个后疫情的大环境中，想做好一件令人满意的事变得更加困难。我知道一个人的力量是渺小的，尽管如此，但我依旧选择去努力实现。希望能在前进的道路上有你相助，可以是任何方式❤

---

### 📋赞助名单 Donation List

非常感谢「 [这些用户](https://github.com/239144498/ClipSync/wiki/Donation-List) 」对本项目的赞助支持！

---

### ❤ 赞助 Donation

---

如果你觉得本项目对你有帮助，请考虑赞助本项目，以激励我投入更多的时间进行维护与开发。 If you find this project helpful, please consider supporting the project going forward. Your support is greatly appreciated.

> Every time you spend money, you're casting a vote for the kind of world you want. -- Anna Lappe

<a href="https://ik.imagekit.io/naihe/pay/hbm.jpg"><img src="https://ik.imagekit.io/naihe/pay/hbm.jpg" alt="stream.png" border="0" width="400px" height="220px" /></a>
<a href="http://typora.datastream.tebi.io/68747470733a2f2f73322e617831782e636f6d2f323032302f30312f33312f3133503863462e6a7067.jpg"><img src="http://typora.datastream.tebi.io/68747470733a2f2f73322e617831782e636f6d2f323032302f30312f33312f3133503863462e6a7067.jpg" alt="stream.png" border="0" width="400px" height="220px" /></a>
题外话：赞助的时候可以留言，留言内容将被展示在 [赞助列表画面](https://github.com/239144498/ClipSync/wiki/Donation-List) 。如果赞助图片未能正常显示，请访问： [https://ik.imagekit.io/naihe/pay/hbm.jpg](https://ik.imagekit.io/naihe/pay/hbm.jpg)
**你的`star`或者`赞助`是我长期维护此项目的动力所在，由衷感谢每一位支持者，“每一次你花的钱都是在为你想要的世界投票”。 另外，将本项目推荐给更多的人，也是一种支持的方式，用的人越多更新的动力越足。**

### 🌚 作者

* 主程序以及框架：[@naihe](https://github.com/239144498)

### 💖 所有贡献者

这个项目需要更多的贡献者来参与和推动发展

📝项目完成进度
--------------

### 已完成

* [x] 全平台兼容
* [x] 多设备同步
* [x] 项目解耦
* [x] 解决通信闭环传递
* [x] API接口扩展
* [x] 优化多设备通信连接

### 待完成

* [ ] 完善Web网页
* [ ] 更多同步格式
* [ ] 端到端加密
* [ ] 离线信息同步
* [ ] 历史记录
* [ ] 待定...

### 🥝 开源协议

[GNU3.0](https://opensource.org/license/gpl-3-0/)

