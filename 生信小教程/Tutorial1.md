# 1 所有编程的始发点

> 导说：『要有码』，于是就有了服务器。

## 1.1 登入服务器

一个萌新想要登录服务器，需要服务器的<font color =red>ip地址</font>，以及由管理员创建的<font color =red>账号</font>和<font color =red>密码</font>。

在获得以上三个信息后，还需要准备用于和服务器连接的软件。可以将服务器理解为另外一台电脑，你需要<font color =red>终端软件</font>进行远程操作，<font color =red>传输软件</font>在电脑和服务器间传送文件。我个人目前使用MobaXterm终端和Xftp传输，此外组内也有很多人使用putty，根据自己的喜好选择即可。

~~<font color =grey>MobaXterm的可视化路径显示，是被迫离开windows摇篮的新人对图形界面最后的眷恋。</font>~~

这里以MobaXterm为例进行演示。启动软件，点击左上角Session，连接类型选择SSH，在设置界面分别填入ip地址和用户名（图），点OK，之后在弹出的窗口输入密码。注意，<font color =red>linux系统中的密码不会显示为\*\*\*\*\*\*</font>，所以看上去就像没输进去一样，输入完毕后直接登录即可。首次登录后MobaXterm即可记住密码，之后在主界面点击服务器ip地址号就能自动登入。

![图寄啦！](https://github.com/Vivien-Liu98/Git-images/blob/main/1login.png)

登录成功后，会进入个人home目录，例如<font color =red>/public/home/Zhangsan</font>。这个以自己的用户名来命名的目录，就是以后工作的空间。如果回到上级目录/public/home，就可以看到大家都在。

> [!TIP]
>
> **路径缩写的含义**
>
> cd命令：进入指定位置，配合缩写可以实现快速跳转。
>
> cd . 进入当前目录，即不跳转
>
> cd .. 进入上一级目录，即/public/home
>
> cd / 进入根目录，即public上层的那个/，基本上不会去的地方
>
> cd ~ 进入用户home目录，即/public/home/Zhangsan，一键回城（只输入cd也是这个效果）
>
> 如果迷路，可以输入pwd命令查看当前所在路径。



## 1.2 安装conda

进入服务器，在开始敲代码前，还需要配置工作环境。

conda是一个被广泛使用的环境和软件管理系统。生信分析需要同时使用多个软件，但有些软件并非公司推出的成熟作品，而是研究组自行开发的程序，直接混用可能会导致不可预知的问题。此外，部分多年未更新的程序不再适配最新的环境，无法和新软件在同一环境共存。conda如同一个橱柜，可以将不用的软件放在不同的环境中，从而避免单一环境下运行的冲突。此外，它还可以方便的下载各种常用生信软件。

**①下载安装包**

```shell
wget -c https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh
# 前有#的代码是注释，不会被执行
# wegt是下载命令，-c表示断点续传，防止网络波动导致白给
```

由于我组服务器上已有下载好的安装包，直接进入步骤②。出于节约服务器空间的需求，如无特殊需求，使用简约版的miniconda即可。

**②安装程序**

```shell
bash /public/home/Zhangsan/Miniconda3-py39_4.12.0-Linux-x86_64.sh
# 即安装包所在的路径
```

MobaXterm可以在左侧可视化栏里，右键点击文件，选复制路径（copy file path)。粘贴的路径两端带有“ ”，记得删掉。注意，<font color =red>linux中ctrl+C是强制终止命令</font>，因此请使用鼠标右键来复制粘贴。

安装中根据提示按回车、输入yes、y即可完成conda的安装。

**③激活环境**

```shell
source ~/.bashrc
# .bashrc是个人目录下的配置文件，如果对它进行了修改，可以通过source命令刷新使其生效
# ~/.bashrc等效于/public/home/Zhangsan/.bashrc
```

激活成功后，光标处多了一个(base)题头，这是最基础的base环境，之后每次登录都会默认进入该环境。

```shell
(base) [Zhangsan@huge01 ~]$
# （）为当前环境名，huge01是我组服务器主机的名字，~是当前目录
# 所以如果更改环境和目录，对应的内容也会随之改变，例如↓
(123) [Zhangsan@huge01 home]$ 
```

**④环境配置**

将软件安装在不同的环境即可实现隔离，使用对应的软件需要进入对应的环境。由于个人课题较为简单，base环境已足够，本部分仅分享代码。

```shell
conda create -n 123
# 新建名为123的环境
conda create -n 456 python=2.7 r=2.6
# 可以在建立环境时指定其使用的语言版本，从而满足时代眼泪的运行条件
conda remove -n 123 -all 
# 删除名为123的环境，内部安装的软件包也会被一起删除
conda env list
# 查看现有的所有环境
conda activate 123
# 进入名为123的环境，成功后命令题头变为(123)
conda deactivate
# 退出当前环境，成功后命令题头变回(base)
```

> [!CAUTION]
>
> 更新到最新版conda后，<font color =red>(base) [Zhangsan@huge01 ~]$</font>变为<font color =red>(base)</font>，不方便查看所在目录，可以输入conda init bash，运行后重新连接服务器即可恢复。



<font color =blue>未完待续……</font>