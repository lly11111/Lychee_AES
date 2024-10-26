# 开发手册&用户指南

该系统是我们“荔枝”团队为用户设计的一款简单、开源的AES算法加解密系统，能够满足用户简单的加解密需要（二进制加解密、ASCII码字符串加解密、多重加解密、文件加解密），同时可以向用户展示对于双重加密AES算法的有效破解方案——中间相遇攻击问题。

同时，也欢迎广大程序设计与编码工作者继续完善该加密系统。如有任何疑问和建议，欢迎联系我们团队（Email：[1635487611@qq.com](mailto:1635487611@qq.com)）。


## **开发者团队**

* **开发者队名：** 荔枝

* **开发者姓名：** 张芷芮、刘俐莹

* **联系信息：**[1635487611@qq.com](mailto:1635487611@qq.com)

## **开发环境**

3.1.1 开发工具

* 集成开发化境（IDE）：PyCharm 2023.3

* 版本控制：Github

3.1.2 技术栈

* 前端语言&框架：HTML5，CSS3，JavaScript，jQuery

* 后端技术：语言：Python

* 框架：Flask框架

* Web浏览器：Microsoft Edge

## **运行**

```bash
main.py
```

## **网址与端口号**

该系统在[http://127.0.0.1:6606](http://127.0.0.1:6606)上运行


## **基础功能及界面**

* **二进制加密页面**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b1372e4b9d2c481ba320b756d926bd6a.png#pic_center)
* **ASCII码加密页面**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8eb4d80620864311bdc920d703e02d87.png#pic_center)
* **二重加密页面**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1522ca252bb34f08a84d36a35f93b615.png#pic_center)
* **三重加密页面**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b707c1fe33134532b67c3a5356f8d012.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a9b9d09a1af445328f4511732a1664d7.png#pic_center)
* **中间相遇攻击页面**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/bd5e447777234054adbc118f58f3bbdc.png#pic_center)
*  **文件加密页面**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7de095b5d5d0488db32dc6022dd0585a.png#pic_center)
* **CBC模式加密页面**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/9f16da6e36ca493a9341908d531cd6f9.png#pic_center)

## **文件结构**
* 测试结果.pdf：存放1-5关的通关结果
* 开发手册与用户指南：存放具体开发环境、代码逻辑、系统功能介绍等
* static文件夹：存放图片、js文件和css样式表等
* templates文件夹：存放html文件

* data.py文件：存放标准加解密数据和几个基础函数（密钥扩展函数、轮密钥加函数、半字节代替函数、行移位函数、列混淆函数）

* main.py文件：存放连接前后端的路由

* bit_encryption.py文件：存放二进制加密算法

* bit_decryption.py文件：存放二进制解密算法

* ascii_encryption.py文件：存放ASCII码的加密算法

* ascii_decryption.py文件：存放ASCII码的解密算法

* double_method.py文件：存放两种双重加密算法和普通破解方式的解密算法

* triple_method1.py文件：存放三重加解密算法（其中密钥长度为32 bit）

* triple_method2.py文件：存放两种三重加解密算法（其中密钥长度为48 bit）

* meetInTheMiddleAttack.py文件：存放中间相遇攻击算法

* fileEncryption.py文件：存放文件加密算法

* cipherBlockChaining.py文件：存放CBC模式加密算法
