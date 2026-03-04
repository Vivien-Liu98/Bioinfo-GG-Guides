# 3 语言与脚本

> 作为生信半吊子，之后的路就要你们自己走了。

编程有很多『语言』，python，C艹，perl，java等等……我们在服务器日常使用的也是被称为shell的linux系统自带语言。通过语言可以将我们的需求告知服务器，实现对目录和文件的各种操作。一个完整的分析流程包含由编程语言写的指令和生信软件运行的命令，而将流程所需的多条代码合并在一起，就是『脚本』。这样在进行重复分析时，不用再逐步输入代码，仅需要运行一次脚本就可以完成一遍流程。

语言在使用前，也需要像软件那样安装和配置，conda已经包含了一部分环境。由于本组服务器早已配置好了各语言，加之本人并非计算机专业，仅提供一个教程：https://m.runoob.com/perl/perl-environment.html

以perl为例，使用linux自带的vim编辑器即可编写脚本。

```shell
vi test.pl
# 创建并打开一个perl脚本文件，按i进入输入模式，输入以下内容：
#!/usr/bin/perl
# perl本体安装的路径，脚本的标准起手式
print "啊?\n"
# print命令可输出指定内容，\n为回车。perl默认不换行,不加\n输出内容后会和下一个题头接在一起……
# 当然也可以用祖传问候Hello world
# 按esc，输入:wq保存并退出编辑器界面
perl test.pl
# 直接用语言名+脚本文件名即可运行，其他语言同理
啊?
# 成功运行会输出上述内容
```

如果终端软件和服务器断开连接，正在执行的脚本也会<font color=red>随之终止</font>。因此，在运行需要较长时间的程序时，一般会使用nohup将其挂在后台自动运行，避免网络波动导致白给的悲剧。

```shell
nohup bash test.sh
# 挂机版，运行完成后才可以输入新的代码。可通过Ctrl+C终止
nohup bash test.sh TEST &
# 如果想继续运行其他程序则添加&。TEST为进程名，开始运行后会获得一个pid便于查询运行情况
# 注意，在使用&后，仅能通过kill pid来终止脚本
```

在nohup的程序运行完成后，会在当前目录生成nohup.out文件，可以通过cat或vi命令查看。该文件包含了所有本来输出到屏幕的信息，不含过程和结果文件。因此，该命令也可以用来避免软件运行中高速刷屏。

## 实例

**①perl语言的四则运算**

```perl
#!/usr/bin/perl

print "\n输入两个数字后的四则运算\n";

print "请输入第一个数字:\n";
$x=<STDIN>;
# <STDIN>为读取用户输入的内容，所有内容都需要先定义变量作为它的代号
print "请输入第二个数字:\n";
$y=<STDIN>;
# 变量不可重名，否则后面的会覆盖掉前面的值
# perl直接对变量进行加减乘除↓
print "和\n";
$z=$x+$y;
print "$z\n";

print "乘积\n";
$v=$x*$y;
print "$v\n";

print "差\n";
$w=$x-$y;
print "$w\n";

print "商\n";
$u=$x/$y;
print "$u\n";

print "计算完毕\n\n"
```

运行效果如下：

![图寄啦！](https://github.com/Vivien-Liu98/Git-images/blob/main/perl.png)

**②综合脚本**

综合shell语言和软件示范。~~由于这段代码是我为了示范随便搓的，不保证能跑通。~~

```shell
#!/usr/bin/bash

# 检测基因组是否已经建立索引,如没有，则建立索引
if [ ! -e "library*" ]; then
  makeblastdb -in genome.fna -out library -dbtype nucl -parse_seqids -hash_index 
fi

#对目录下的所有fasta文件执行以下命令
for file in *.fasta # 逐个读取所有fasta文件，变量$file即为文件名
do bash sequence.sh # 假装有一个脚本，脚本是可以嵌套脚本的
   blastn -query $file -db library -out "$file.txt" -outfmt=6 # BlAST比对
done

# 循环结束后
echo "比对完成！" # shell的echo命令同perl的print命令，均为输出指定内容
```



<font color =blue>完结撒花~</font>