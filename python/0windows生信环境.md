# 0 windows生信环境

> 步入流放者的乐园。



## 0.1 本地部署linux

没有实验室服务器时，可以在windows本地搭建linux环境，获得基本上等同于服务器的学习体验。本文使用windows自己的wsl（Windows Subsystem for Linux）。

> [!CAUTION]
> 
> 由于个人电脑的性能远逊于服务器，不能用来进行大数据分析！在之后的笔记中，使用大肠杆菌（原核）和酵母（真核）数据来练习。

首先，win+X，选择终端管理员，即PowerShell（管理员模式），进入命令行窗口。

```powershell
# 安装WSL
wsl --install
# 重启电脑，之后重新打开终端管理员窗口

# 安装Ubuntu(linux)
wsl --list --online  # 列出所有可下载版本
wsl --install -d Ubuntu-22.04  # 选择稳定的版本
# 根据安装提示，设置用户名和密码，注意linux密码输入后不显示*号

# 进行更新
sudo apt update
sudo apt upgrade -y
# 测试双系统文件互通
cd /mnt/c  # 进入c盘
ls  # 列出所有文件，如和c盘文件一致，则安装成功
```

由于本地部署不同于之前的远程连接，我们使用Visual Studio Code作为操作终端。该软件同时支持各类拓展插件和AI辅助。

官网下载安装Visual Studio Code，之后从左侧边栏点击拓展，在商店搜索Chinese（汉化补丁，可选），WSL（用于连接子系统），Python（以及其他需要的语言）。
安装完毕后，启动WSL拓展，左下角选择开启新窗口（第一次需要等待加载，之后启动则默认连接至WSL，和服务器体验一致）。

```bash
# 测试连接
pwd  # 当前位置
ls   # 列出所有文件
whoami  # 个人信息
# 以vivien为例
vivien@localhost:~$ pwd 
/home/vivien  # 这里就是家目录~,每次登录的主页

# 安装miniconda（节约空间）
# 下载安装脚本
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
# 运行脚本，自动安装
bash ~/miniconda.sh  # 过程中根据提示按回车和输yes
# 激活conda
source ~/.bashrc   # 这时题头显示(base)证明进入基础环境成功
# 查看版本
conda --version
# 之后可以删除安装脚本，rm miniconda.sh
```

# 0.2 VSC基本操作

介于本人之前一直使用MobaXterm，对于VSC还在摸索中，以下仅为记录。

①基本操作

- 右上角的四个小图标，可以操作不同功能分区的开启和关闭。

- 新建终端：上方-终端-新建（可能藏在...里）；下方-图标-拆分（同时显示俩，比较挤）

②文件操作

- 欢迎界面-打开文件夹，找到~目录（/home/vivien），即可在左侧显示文件分区。第一次手动，之后默认打开。

- 文件分区可以直接拖拽上传文件，但是不能拖拽下载。

- 此电脑，左边栏，Linux\Ubuntu-22.04\home\vivien，即可进入~目录下载/上传文件。

- 通过命令explorer.exe .可以一键在文件管理器中打开当前所在位置。

- 可以在~目录工作，也可以进入windows文件夹，例如D盘的cd '/mnt/d/Scientific research'。前者运行速度更快，后者可通过软链接实现快速跳转。

③文件编辑

- 点击文件名即可查看和编辑文件，无需vi。

- ctrl+S保存或关闭文件时提示保存，可以在设置里选择各种方便的自动保存。

- 使用文件分区的新建按钮或touch命令新建文件。

- 使用code命令可将文件在编辑分区打开，不存在的文件自动新建。
