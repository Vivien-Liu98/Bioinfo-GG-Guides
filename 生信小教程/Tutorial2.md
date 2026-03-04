# 2 软件安装与使用

> 软件岂是如此不便之物。

不同的生信分析流程需要不同的软件，需要查阅文献或教程，无法给出通解。这里以序列比对常用的BLAST为例进行讲解。

## 1.1 配置源

所谓的『源』，是存储了众多软件的仓库。由于conda的默认源在国外，国内下载速度感人，因此我们同时使用国内的镜像源以提速。源只需要配置一次，之后直接进入1.2下载安装软件即可。

```shell
# 添加官方源
conda config --add channels r
conda config --add channels conda-forge
conda config --add channels bioconda
# 三个分别是R软件包，非默认通道软件和生信工具
# 添加清华镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --set show_channel_urls yes
# 检查是否配置成功
conda config --get channels
# 成功后会显示以下内容
--add channels 'defaults'   # lowest priority
--add channels 'r'
--add channels 'conda-forge'
--add channels 'bioconda'
--add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'
--add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/'
--add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/'   # highest priority
```

## 1.2 软件下载与安装

我组服务器在/public/software中已经安装了一些常用生信软件，所有人都可以直接使用。不过由于大家做的课题不尽相同，所以还是有根据个人需求安装软件的时候。管理员外的普通用户没有在/public/操作的权限，软件只能安装在个人目录。

对于conda/bioconda源中已经包含的软件，可以直接下载，否则需要自行寻找软件配布的官网下载。

**①自动安装**

```shell
conda install software=1.1.4
# 直接使用conda安装，软件后可指定想要下载的版本，不指定则默认为新版本
conda install -c bioconda software
# 使用bioconda安装
```

software处填写软件名，可以在源的网站中查询。如果安装的conda不是最新版，在使用该功能时会自动更新，根据提示操作即可。

**②手动安装**

```shell
wget -c https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz
# 从ncbi官网下载BLAST
tar -zxvf ncbi-blast-2.13.0+-x64-linux.tar.gz
# 解压压缩包，完成后目录里会出现一个名为ncbi-blast-2.13.0+的目录，即为软件
# 安装完成后.tar.gz安装包就可以删掉了
```

部分软件需要编译等复杂的安装过程，请参照官网或说明文档操作。

安装完毕后，输入<font color =red>blastn -h</font>测试软件，发现没有输出预期的blastn说明文档，直接报错。这是因为在服务器输入命令时，默认只读取当前所在目录的文件，而blastn却位于~/ncbi-blast-2.13.0+/bin/blastn。如果每次使用软件都要输入这一大串路径太过麻烦，有两种解决方案。

**③软链接**

软链接可以理解为windows系统中的快捷方式，导向其他目录的文件。称其为『软』是因为软链接文件仅包含一个链接，并非引用的文件本体，可以节约存储空间。

```shell
ln -s /public/home/Zhangsan/ncbi-blast-2.13.0+/bin/blastn blastn
# ln创建链接，-s软链接，后面跟着路径，最后加上链接的名字（建议和软件名一致方便使用）
```

这时再测试，就能正常运行BLAST了。

注意，软链接仅对其所在的目录生效，如果需要在多个目录中运行软件，则每个都需要创建软链接。

注意2，由于BLAST内部包含多个软件，而软链接只链接了blastn，因此这里只是演示软链接，实际调用BLAST请使用下面的环境变量法。软链接更适用于只有一个本体的软件或基因组等大文件。

**④环境变量**

环境变量将软件的路径烙印于系统设置本身，不论位于哪里都可以自由调用。~~好吧，范围限制在你自己的个人目录里。~~

```shell
vi ~/.bashrc
# 打开环境配置文件，在末尾新开一行，输入以下内容↓
export PATH=/home/Zhangsan/ncbi-blast-2.13.0+/bin:$PATH
# 添加BLAST的环境变量
source ~/.bashrc
# 刷新环境配置让新添加的内容生效
```

这时再测试，也能正常运行BLAST。

注意，对于包含bin目录的软件，环境变量就设置为<font color =red>bin目录</font>；而对于只有一个本体的软件，环境变量则设置为这个本体所在的<font color =red>目录</font>。环境变量是跳过了输入路径的过程直达软件所在的目录，因此在使用软件时要输入<font color =red>所在目录里软件本身的名字</font>。举个例子，MFEprimer软件安装后只有一个mfeprimer-3.1.0-linux-amd64文件，设置好环境变量后，需要输入mfeprimer-3.1.0-linux-amd64的完整名字才能运行。不过软件文件其实是可以改名的，可以删掉后面多余的版本后缀。

## 1.3 BLAST比对

~~为什么不直接去ncbi上用在线BLAST呢？~~

这里示范使用一段序列与下载的基因组进行比对。在开始前，需要在当前目录里准备好要比对的序列test.fasta和参考基因组genome.fna。

```shell
makeblastdb -in genome.fna -out library -dbtype nucl -parse_seqids -hash_index
# 首先需要对基因组文件建库，-in输入基因组名，-out输出参考库名，-dbtype选择数据类型是核酸nucl还是蛋白prot
blastn -query test.fasta -db library -out result.txt -outfmt=6
# 进行比对，-query输入序列名，-db使用的参考库，-out输出结果文件名，-outfmt输出结果格式
```

每个软件使用的参数和命令都不尽相同，请参考--help命令的提示和官网的说明，善用百度和google搜索。加油！



<font color =blue>未完待续……</font>