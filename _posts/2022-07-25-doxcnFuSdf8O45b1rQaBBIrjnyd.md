---
title: "BashShell Learning Note"
date: 2022-07-25 00:00
categories: ['Note', 'BashShell']
tags: ['Note', 'BashShell']
---



## Shell Programming

## Shell 脚本的执行方式

### 脚本的格式要求

1. 脚本以 `#!/bin/bash` 开头
2. 脚本需要有可执行权限

### 脚本的常用执行方式

#### 方式 1：输入脚本的路径

说明：首先需赋予脚本的 +x 权限，再执行脚本

提示：`chmod u+x FILENAME` `chmod 777 FILENAME`

#### 方式 2：sh+ 脚本

说明：不用赋予脚本 `+x` 权限，直接执行即可

### 实例

```bash
#!/bin/bash
echo "Hello World!"
```

## Shell 的变量

### Shell 变量介绍

1. Linux Shell 中的变量分为，**系统变量**和**用户自定义变量**。
2. 系统变量：$HOME、$PWD、$SHELL、$USER and so on
3. 显示当前 shell 中所有变量: `set`

### Shell 变量的定义

#### 基本语法

1. 定义变量： `变量名=值` 注意之间不能有**空格**
2. 撤销变量：`unset 变量`
3. 声明静态变量: `readonly 变量` 注意静态变量不可 **unset**

### Shell 变量的定义

#### 定义变量的规则

1. 变量名称可以由字母、数字和下划线组成，但是不能以数字开头。
2. 等号两侧不能有空格
3. 变量名称一般规范习惯为大写

#### 将命令的返回值赋给变量

1. 例如 `A='data'` 单引号，运行里面的命令并把结果返回给变量
2. `A=$(data)` 等价于 1.

### 实例

```bash
#!/bin/bash
#定义A
A=100
#不要有空格要有$
echo A=$A
#撤销A
unset A
echo A=$A
#定义静态变量
readonly B=2
echo B=$B
echo $(date)
:<<!
这是多行注释
!
```

## 设置环境变量

### 基本语法

1. `export 变量名=值`(功能描述:将 shell 变量输出为环境变量/全局变量)
2. source 配置文件(功能描述:让修改后的配置信息立即生效，配置文件一般为 `/etc/profile`)注意更改后需要 `source /etc/profile` 同步设置
3. echo $ 变量名(功能描述:查询环境变量的值)

## 位置参数变量

### 介绍

当我们执行一个 shell 脚本时，如果希望获取到命令行的参数信息，就可以使用到位置参数变量，简言之就是一个可以传参的脚本

### 基本语法

1. `$n`(功能描述:`n` 为数字，`$0` 代表命令本身，`$1-$9` 代表第一到第九个参数，十以上的参数，十以上的参数需要用大括号包含，如 `${10}`)
2. `$*`(功能描述:这个变量代表命令行中所有的参数，`$*` 把所有的参数看成**一个整体**)
3. `$@`(功能描述:这个变量也代表命令行中所有的参数，不过 `$@` 把每个参数**区分对待**)
4. `$#`(功能描述:这个变量代表命令行中所有参数的个数)

```bash
#!/bin/bash
echo "0=$0 1=$1 2=$2"
echo "所有的参数$*"
echo "$@"
echo "参数的个数$#"
```

```bash
sh position.sh 100 200
0=position.sh 1=100 2=200
所有的参数100 200
100 200
参数的个数2
```

## 预定义变量

### 基本介绍

就是 shell 设计者事先已经定义好的变量，可以直接在 shell 脚本中使用

### 基本语法

1. `$$`(功能描述:当前进程的进程号(PID) )
2. `$!`(功能描述:后台运行的最后一个进程的进程号(PID))
3. `$?`(功能描述:最后一次执行命令的返回状态，如果这个变量的值为 0，证明上一个命令正确执行；如果这个变量的值为非 0(具体是哪个数，由命令自己来决定)，则证明上一个命令执行不正确)

### 实例

```bash
#!/bin/bash
echo "当前执行的进程id为$$"
#以后台的方式运行一个脚本，并获取其进程号
./hello.sh &
# &表示以后台的方式运行
echo "最后一个后台方式运行的进程id为$!"

echo "执行的结果为$?"
echo "0则代表无问题"
```

## 运算符

### 基本语法

1. `$((运算式))` or `$[运算式]` or `expr x + y` //expr->expression
2. `expr` 中间必须有空格，如果要把 `expr` 的结果赋给某个变量需要 ``` 反引号（位于 `esc` 键下）
3. `expr` `\*``,/,%  ``乘``，除，取余`

### 实例

```bash
#!/bin/bash
# calculate(2+3)x4
# The First Way
RES1=$(((2+3)*4))
echo "RES1=$RES1"
#The Second Way
RES2=$[(2+3)*4]
echo "RES2=$RES2"
#The Third Way
SUM=`expr 2 + 3`
RES3=`expr $SUM \* 4`
echo "RES3=$RES3"
# Make A Function to cal a + b
RES=$[$1+$2]
echo "RES=$RES"
```

> 这语法真变态！！！

## 流程控制

### if 判断

#### 基本语法

```bash
#cond 是条件condition的缩写
if [ cond ]
then
Code
elif [ cond ]
then
Code
else
#else没有then
Code
```

#### 实例

```bash
#!/bin/bash
if [ $1 -ge 60 ]
then
        echo "及格"
else
#else 后面没有then
        echo "不及格"
fi
```

### case 语句

#### 语法

```bash
#val 为 value(值)的缩写
case $变量名 in
"Val1")
Code
;;
"Val2")
Code
;;
*)
# 都不是的话执行
Code
;;
esac
#case 反过来写
```

#### 实例

```bash
#!/bin/bash
case $1 in
"1")
echo "Monday"
;;
"2")
echo "Tuesday"
;;
*)
echo "other"
;;
esac
```

### for 循环

#### 基本语法

##### Grammar One

```bash
for 循环变量 in val1 val2 val3
do
Code
done
```

##### 实例

```bash
#!/bin/bash
#Grammar One
#$*是把输入的参数当做一个整体
#例如
#sh ForDemo.sh 5 2 647 
#then $*=5 2 647
#如果用双引号括住则是一个整体
#不用双引号括住的话则原封不动地保留空格
#形成for i in 5 2 647
#即for 循环变量 in val1 val2 val3
#所以可分开输出
for i in "$*"
do
        echo "Num is $i"
done
echo "==============================="
for j in $*
do
        echo "Num is $j"
done
echo "==============================="
for k in "$@"
do
        echo "Num is $k"
done
```

##### Grammar Two

```bash
#基本同 C 语法
#循环控制条件不用 []
for((初始值;循环控制条件;变量变化))
do
Code
done
```

##### 实例

```bash
#!/bin/bash
#Grammar Two
SUM=0
for ((u=1; u<= $1; u ++))
do
        SUM=$[$SUM+$u]
        #赋值无需$
        #$SUM=$[$SUM+$u]则错
done
echo "∑1~$1=$SUM"
```

### while 循环

#### 基本语法

```bash
while [ cond ]
do
    Code
done
```

#### 实例

```bash
#!/bin/bash
SUM=0
i=0
while [ $i -le $1 ]
do
        SUM=$[$SUM+$i]
        i=$[$i+1]
done
echo "∑1~$1=$SUM"
```

## read 读取控制台输入

### 基本语法

`read ``option`` ``params`

#### option:

`-p 指定读取值时的提示符`

`-t 指定读取值时等待的时间(秒)，若超时则结束`

#### Params:

`变量：指定读取值的变量名`

### 实例

```bash
#!/bin/bash
read -p "Please Input x, y = " X Y
echo "The Sum is $[$X+$Y]"
read -t 10 -p "Please Input Sth in Ten Seconds " STH
echo "Something is $STH
```

## 函数

### 系统函数

1. `basename`

实例：

```bash
basename /root/Desktop/Test.cpp
#The Will Output
Test.cpp
```

1. `dirname`

实例：

```bash
dirname /root/Desktop/Test.cpp
#The Will Output
/root/桌面
```

### 自定义函数

#### 基本语法

```bash
#Define
function funname()
{
    Code
}
#Call
funname val1 val2
```

### 实例

```bash
#!/bin/bash
#$(Command) Run Command And Return it
#系统自带函数
echo $(basename /root/桌面/Test.cpp)
echo $(dirname /root/桌面/Test.cpp)
#自定义函数
#Define
function GetSum()
{
SUM=$[$1+$2]
echo "Sum is $SUM,Powered By $0"
#return SUM 无法Return！！！
}
#Input Value
#read -p "Please input n1 and n2 " n1 n2
#Call
echo $(GetSum 1 2)
#此处的 1 和 2 是GetSum的 $1 和 $2 , 不是整个函数的 , 但貌似 $0 是不变的
echo "函数外的dollar1=$1,dollar2=$2"
```

> 这章讲的好水！！！

## 实例

### 备份 MySql 数据库

```bash
#!/bin/bash
echo "开始备份"
BACKUPDIRECTORY=/data/backup/db
DATETIME=$(date +%Y-%m-%d_%H%M%S)
echo $DATETIME
#数据库地址
HOST=localhost
USER=root
PASSWD=Yang0212
DATABASE=?????
#创建备份目录
[ ! -d "$BACKUPDIRECTORY/$DATETIME" ] && mkdir -p "$BACKUPDIRECTORY/$DATETIME"
#备份 备份到当前设置目录名为DATETIME的文件
myspldump -u$USER -p$PASSWD --host=$HOST -q -R --databases $DATABASE | gzip > $BACKUPDIRCTORY/$DATETIME/$DATETIME.sql.gz
#删除十天前的备份文件
find $BACKUPDIRECTORY -atime +10 -name "*.gz" -exec rm -rf {} \;
echo "备份完成"
```
