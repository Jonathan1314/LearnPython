
#### 字符编码 

1. 字符编码：

补充：
编译型语言：代码统一编译成二进制字节码 -> 执行  
优点：执行速度快  
缺点：每次修改代码，需重新编译


解释型语言：代码一行一行翻译成二进制字节码 -> 执行  
缺点：执行速度慢  
优点：方便调试，随时调试，随时执行

代码主要经历存储介质： **内存**、**CPU**、**硬盘**，以此为切入点来研究字符编码

Python解释器执行py文件的原理，例如 python test.py

- 第一阶段：python解释器启动，此时就相当于启动了一个文本编辑器
- 第二阶段：python解释器相当于文本编辑器，去打开test.py文件，从硬盘上将test.py的文件内容读入到内存中
- 第三阶段：python解释器解释执行刚刚加载到内存中test.py的代码


字符编码: 把人认识的字符 转换 成计算机识别的数字

2. 字符编码发展史  

阶段一：现代计算机起源于美国，最早诞生也是基于英文考虑的ASCII

阶段二：为了满足中文，中国人定制了GBK

阶段三：万国码 Unicode


总结强调：

- unicode，统一编码，至少2个字节。优点：字符 -> 数字的转换速度快；缺点：占用空间大
- utf-8，不同的字符用不同的长度表示，优点：节省空间；缺点：需要计算多长Bytes表示字符，字符 -> 数字的转换速度慢
- 内存中使用的编码是unicode，用空间换时间(程序都需要加载到内存才能运行，因而内存应该是尽可能的保证快)
- 硬盘中或者网络传输用utf-8，网络I/O延迟或磁盘I/O延迟要远大与utf-8的转换延迟，而且I/O应该是尽可能地节省带宽，保证数据传输的稳定性


3. 编码的使用

![image](http://images.cnblogs.com/cnblogs_com/jonathan1314/1022859/o_code.png)


文件从内存刷到硬盘的操作简称存文件

文件从硬盘读到内存的操作简称读文件

乱码一：存文件时就已经乱码

存文件时，由于文件内有各个国家的文字，我们单以shift-jis去存,日文可以正常存储，其他国家文件打开时就会乱码

或者 以任何编码打开文件a.txt都会出现其余两个无法正常显示的问题


```
f=open('a.txt','wb')
f.write('何を見て\n'.encode('shift_jis'))
f.write('你愁啥\n'.encode('gbk'))
f.write('你愁啥\n'.encode('utf-8'))
f.close()
```

乱码二：存文件时不乱码而读文件时乱码


总结强调：

核心法则就是，文件以什么编码保存的，就以什么编码方式打开



存的过程编码  # PyCharm编辑器自动根据开头编码写

读的过程编码  # -*- coding:utf-8 -*-


4. 程序的执行

Python3中两种形式的字符串：

str(即unicode, u'林')  
bytes(即 str.encode()的结果，b'\xe6\x9e\x97')


Python2中也有两种形式的字符串：

str == bytes  
unicode
见代码详解

####  文件处理

1. 文件处理流程
- 打开文件，得到文件对象并赋值给一个变量  <_io.TextIOWrapper name='' mode='' encoding=''>
- 通过对象对文件进行操作  
- 关闭文件

CPU的两种运行状态：内核态、用户态 (寄存器 0和1切换)

内核态：操作系统有效，可以任意操作硬件
用户态：应用程序，不能直接操作硬件

应用程序不能直接调用硬件，但是有需求：网卡传输数据，硬盘读写数据等，发系统调用切换到内核态，操作系统调用硬件

联系：套接字编程，进程线程，IO多路复用(epoll)

```
f = open('a.txt')  # 发系统调用，中文Windows默认GBK
f = open('a.txt', encoding='utf-8')

```

文件是来自操作系统的概念，有修改一说，抽象概念















