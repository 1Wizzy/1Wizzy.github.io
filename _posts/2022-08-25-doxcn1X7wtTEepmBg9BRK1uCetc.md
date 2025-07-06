---
title: "SQL Learning Note"
date: 2022-08-25 00:00
categories: ['Note', 'SQL']
tags: ['Note', 'SQL', 'MySQL']
---



## SQL Learning Note

## SQL、DB、DBMS 分别是什么，他们之间的关系？

### DB

DataBase（数据库，数据库实际上在硬盘上以文件的形式存在）

### DBMS

DataBase Management System（数据库管理系统，常见的有：MySQL Oracle DB2 Sybase SqlServer...）

### SQL

结构化查询语言，是一门标准通用的语言。标准的 sql 适合于所有的数据库产品。

SQL 属于高级语言。只要能看懂英语单词的，写出来的 sql 语句，可以读懂什么意思。

SQL 语句在执行的时候，实际上内部也会先进行编译，然后再执行 sql。（sql 语句的编译由 DBMS 完成。）

DBMS 负责执行 sql 语句，通过执行 sql 语句来操作 DB 当中的数据。

DBMS -(执行)-> SQL -(操作)-> DB

## 常用命令

<table>
<tr>
<td>查看数据库<br/></td><td>`show databases;`<br/></td></tr>
<tr>
<td>使用数据库<br/></td><td>`use [databasename];`<br/></td></tr>
<tr>
<td>查看当前使用的数据库<br/></td><td>`select database();`<br/></td></tr>
<tr>
<td>查看当前数据库中的表<br/></td><td>`show tables;`<br/></td></tr>
<tr>
<td>查看其他数据库中的表<br/></td><td>`show tables from [databasename];`<br/></td></tr>
<tr>
<td>查看表的结构<br/></td><td>`desc [tablename]`<br/></td></tr>
<tr>
<td>查看表的创建语句<br/></td><td>`show create table [tablename];`<br/></td></tr>
</table>

> `[ ]` 无需写出

## SQL 语句的分类

1. DQL（Data Query Language，数据查询语言）: 查询语句，凡是 select 语句都是 DQL。
2. DML（Data Manipulation Language，数据操作语言）：insert delete update，对表当中的数据进行增删改。
3. DDL（Data Defination Language，数据定义语言）：create drop alter，对表结构的增删改。
4. TCL（Transaction Control Language，事务控制语言）：commit 提交事务，rollback 回滚事务。(TCL 中的 T 是 Transaction)
5. DCL（Data Control Language，数据控制语言）: grant 授权、revoke 撤销权限等。

## DQL

### 简单查询

#### 语法格式：

`select 字段名1,字段名2,字段名3,.... from 表名;`

#### 提示：

1. 任何一条 sql 语句以“;”结尾。
2. sql 语句不区分大小写。
3. 字段可以参与数学运算。

#### 给查询结果的列重命名

例如：

`select 月薪 * 12 as 年薪 from 薪资表`

> `as` 可省略

注意：标准 sql 语句中要求字符串使用单引号括起来。虽然 mysql 支持双引号，尽量别用。

#### 查询所有字段

`select * from emp; --  实际开发中不建议使用*，效率较低。EVEN 手动列出所有字段 BETTER。`

### 条件查询

#### 语法格式

`select 字段名1,字段名2,字段名3,... from 表名 where 条件;`

条件查询需要用到 where 语句，where 必须放到 from 语句表的后面

支持如下运算符

> and 的优先级 > or
> null 无论进行何种计算结果都为 null 计算时可用 ifnull(字段，val)如果字段值为 null 则用 val 替代

#### 表达式的优先级

- 查询薪水大于 1800，并且部门代码为 20 或 30 的员工（错误的写法）

```sql
select * from emp where sal > 1800 and deptno = 20 or deptno = 30;
```

- 查询薪水大于 1800，并且部门代码为 20 或 30 的（正确的写法）

```sql
select * from emp where sal > 1800 and (deptno = 20 or deptno = 30);
```

#### in

in 表示包含的意思，完全可以采用 or 来表示，采用 in 会更简洁一些

- 查询出 job 为 manager 或者 job 为 salesman 的员工

```sql
select * from emp where job in ('manager','salesman');
```

#### like

- Like 可以实现模糊查询，like 支持 % 和_匹配

> % 代表任意多个字符 _代表任意一个字符

### distinct

distinct 用于查询结果集的去重

例如

```sql
select distinct job from emp; 
-- +-----------+
-- | job       |
-- +-----------+
-- | CLERK     |
-- | SALESMAN  |
-- | MANAGER   |
-- | ANALYST   |
-- | PRESIDENT |
-- +-----------+
```

而

```sql
select ename,distinct job from emp;
```

以上的 sql 语句是错误的。

记住：distinct 只能出现在所有字段的最前面。

例

```sql
select distinct deptno,job from emp;
-- +--------+-----------+
-- | deptno | job       |
-- +--------+-----------+
-- |     20 | CLERK     |
-- |     30 | SALESMAN  |
-- |     20 | MANAGER   |
-- |     30 | MANAGER   |
-- |     10 | MANAGER   |
-- |     20 | ANALYST   |
-- |     10 | PRESIDENT |
-- |     30 | CLERK     |
-- |     10 | CLERK     |
-- +--------+-----------+
```

则是按 `deptno+job` 来去重

### 排序

#### 基本语法

`select ... from ... where ... order by 字段1 desc(降序)/asc(升序);`

> 默认为升序 无需写出 `asc`

### 分组函数/聚合函数/多行处理函数

> 所有的分组函数都是对“某一组”数据进行操作的

> **注意：分组函数自动忽略空值(null)，不需要手动的加 where 条件排除空值。**
> **select count(*) from emp where xxx;符合条件的所有记录总数(和某个字段无关)。**
> **select count(comm) from emp;comm 这个字段中不为空的元素总数。**

分组函数/聚合函数/多行处理函数 不是直接使用在 `where` 子句中；

```sql
select * from emp where sal > avg(sal); -- ×
select * from emp where sal > (select avg(sal) from emp); -- √
```

Reason:

分组函数必须在分组后才能使用，`group by` 是在 `where` 执行之后才会执行的

### 分组查询

分组查询主要涉及到两个子句，分别是：group by 和 having

- group by ： 按照某个字段或者某些字段进行分组。
- having : 对分组之后的数据进行再次过滤。

#### group by

找到每个工作岗位的平均薪资

```sql
select job,max(sal) from emp group by job;
```

注意：

1. 分组函数一般都会和 group by 联合使用，这也是为什么它被称为分组函数的原因。
2. 并且任何一个分组函数（count sum avg max min）都是在 group by 语句执行结束之后才会执行的。
3. 当一条 sql 语句没有 group by 的话，整张表的数据会自成一组。
4. 当一条语句中有 group by 的话，select **后面只能跟分组函数和参与分组的字段**。

#### having

找出每个部门的最高薪资，要求显示薪资大于 2900 的数据。

```sql
select max(sal),deptno from emp group by deptno having max(sal) > 2900; -- 这种方式效率低。
select max(sal),deptno from emp where sal > 2900 group by deptno;  -- 效率较高，建议能够使用where过滤的尽量使用where。
```

找出每个部门的平均薪资，要求显示薪资大于 2000 的数据。

此时只能用 `having`

```sql
select deptno,avg(sal) from emp group by deptno having avg(sal) > 2000;
```

### 总结

基本关键字位置

`select ... from ... where ... group by ... having ... order by ...`

<table>
<tr>
<td>关键字<br/></td><td>摆放顺序<br/></td><td>运行顺序<br/></td><td>Do what<br/></td></tr>
<tr>
<td>Select<br/></td><td>1<br/></td><td>5<br/></td><td>查询出<br/></td></tr>
<tr>
<td>from<br/></td><td>2<br/></td><td>1<br/></td><td>查询表<br/></td></tr>
<tr>
<td>where<br/></td><td>3<br/></td><td>2<br/></td><td>条件过滤<br/></td></tr>
<tr>
<td>Group by<br/></td><td>4<br/></td><td>3<br/></td><td>分组<br/></td></tr>
<tr>
<td>having<br/></td><td>5<br/></td><td>4<br/></td><td>筛选<br/></td></tr>
<tr>
<td>Order by<br/></td><td>6<br/></td><td>6<br/></td><td>排序<br/></td></tr>
</table>

### 连接查询

#### 笛卡尔积现象

案例：找出每一个员工的部门名称，要求显示员工名和部门名。

```sql
select ename,dname from emp,dept;
-- +--------+------------+
-- | ename  | dname      |
-- +--------+------------+
-- | SMITH  | ACCOUNTING |
-- | SMITH  | RESEARCH   |
-- | SMITH  | SALES      |
-- | SMITH  | OPERATIONS |
-- | ALLEN  | ACCOUNTING |
-- | ALLEN  | RESEARCH   |
-- | ALLEN  | SALES      |
-- | ALLEN  | OPERATIONS |
-- ............
-- 56 rows in set (0.00 sec)
-- 明显不符合题意
```

**笛卡尔积现象**：当两张表进行连接查询的时候，没有任何条件进行限制，最终的查询结果条数是两张表记录条数的乘积。

关于表的别名：

```
    `select e.ename,d.dname from emp e,dept d;`
```

表的别名有什么好处？

1. 执行效率高。-- 不起别名的话系统会从 `emp` 和 `dept` 中两张表寻找 `ename`
2. 可读性好。

**加条件进行过滤避免笛卡尔积现象**

思考：避免了笛卡尔积现象，会减少记录的匹配次数吗？

```
    不会，次数还是56次。只不过显示的是有效记录。
```

案例：找出每一个员工的部门名称，要求显示员工名和部门名。

```sql
select e.ename,d.dname from emp e , dept d where e.deptno = d.deptno; -- SQL92，以后不用。
-- +--------+------------+
-- | ename  | dname      |
-- +--------+------------+
-- | SMITH  | RESEARCH   |
-- | ALLEN  | SALES      |
-- | WARD   | SALES      |
-- | JONES  | RESEARCH   |
-- | MARTIN | SALES      |
-- | BLAKE  | SALES      |
-- | CLARK  | ACCOUNTING |
-- | SCOTT  | RESEARCH   |
-- | KING   | ACCOUNTING |
-- | TURNER | SALES      |
-- | ADAMS  | RESEARCH   |
-- | JAMES  | SALES      |
-- | FORD   | RESEARCH   |
-- | MILLER | ACCOUNTING |
-- +--------+------------+
```

#### 内连接查询

假设 A 和 B 表进行连接，使用内连接的话，凡是 A 表和 B 表能够匹配上的记录查询出来，这就是内连接。

AB 两张表没有主副之分，两张表是平等的。

##### 等值连接

等值连接的 `where` 筛选条件是 `A.xx=B.yy`

例题：

找到每个员工及其上司的名字

SQL92:

```sql
select e1.ename 员工 ,e2.ename 上司 from emp e1, emp e2 where e2.empno = e1.mgr;
```

SQL99:

```sql
select e1.ename 员工 ,e2.ename 上司 from emp e1 join emp e2 on e2.empno = e1.mgr;
-- +--------+--------+
-- | 员工   | 上司   |
-- +--------+--------+
-- | SMITH  | FORD   |
-- | ALLEN  | BLAKE  |
-- | WARD   | BLAKE  |
-- | JONES  | KING   |
-- | MARTIN | BLAKE  |
-- | BLAKE  | KING   |
-- | CLARK  | KING   |
-- | SCOTT  | JONES  |
-- | TURNER | BLAKE  |
-- | ADAMS  | SCOTT  |
-- | JAMES  | BLAKE  |
-- | FORD   | JONES  |
-- | MILLER | CLARK  |
-- +--------+--------+
```

SQL92 和 SQL 99 在此的差别： `on` 使得内连接条件更加明显

##### 非等值连接

主要 `where` 筛选条件是 `A.xx > B.yy` 等等

例题 求出每个员工的薪资等级

```sql
select e.ename, e.sal, s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;
-- +--------+---------+-------+
-- | ename  | sal     | grade |
-- +--------+---------+-------+
-- | SMITH  |  800.00 |     1 |
-- | ALLEN  | 1600.00 |     3 |
-- | WARD   | 1250.00 |     2 |
-- | JONES  | 2975.00 |     4 |
-- | MARTIN | 1250.00 |     2 |
-- | BLAKE  | 2850.00 |     4 |
-- | CLARK  | 2450.00 |     4 |
-- | SCOTT  | 3000.00 |     4 |
-- | KING   | 5000.00 |     5 |
-- | TURNER | 1500.00 |     3 |
-- | ADAMS  | 1100.00 |     1 |
-- | JAMES  |  950.00 |     1 |
-- | FORD   | 3000.00 |     4 |
-- | MILLER | 1300.00 |     2 |
-- +--------+---------+-------+
```

#### 外连接查询

假设 A 和 B 表进行连接，使用外连接的话，AB 两张表中有一张表是主表，一张表是副表，主要查询主表中的数据，捎带着查询副表，当副表中的数据没有和主表中的数据匹配上，**副表自动模拟出 NULL 与之匹配**。

外连接最重要的特点是：主表的数据无条件的全部查询出来。

外连接分为左连接和右连接

左外连接（左连接）：表示左边的这张表是主表。

右外连接（右连接）：表示右边的这张表是主表。

左连接有右连接的写法，右连接也会有对应的左连接的写法。

例题：找出每个员工的上级领导？（所有员工必须全部查询出来。）

```sql
select e1.ename 员工, e2.ename 上司 from emp e1 left join emp e2 on e1.mgr = e2.empno;
-- +--------+--------+
-- | 员工   | 上司   |
-- +--------+--------+
-- | SMITH  | FORD   |
-- | ALLEN  | BLAKE  |
-- | WARD   | BLAKE  |
-- | JONES  | KING   |
-- | MARTIN | BLAKE  |
-- | BLAKE  | KING   |
-- | CLARK  | KING   |
-- | SCOTT  | JONES  |
-- | KING   | NULL   |
-- | TURNER | BLAKE  |
-- | ADAMS  | SCOTT  |
-- | JAMES  | BLAKE  |
-- | FORD   | JONES  |
-- | MILLER | CLARK  |
-- +--------+--------+
```

#### 三张以上表的连接查询

例题：找出每一个员工的部门名称以及工资等级。

```sql
select e.ename,d.dname,s.grade from emp e join dept d on e.deptno = d.deptno join salgrade s on e.sal between s.losal and s.hisal;
-- +--------+------------+-------+
-- | ename  | dname      | grade |
-- +--------+------------+-------+
-- | SMITH  | RESEARCH   |     1 |
-- | ALLEN  | SALES      |     3 |
-- | WARD   | SALES      |     2 |
-- | JONES  | RESEARCH   |     4 |
-- | MARTIN | SALES      |     2 |
-- | BLAKE  | SALES      |     4 |
-- | CLARK  | ACCOUNTING |     4 |
-- | SCOTT  | RESEARCH   |     4 |
-- | KING   | ACCOUNTING |     5 |
-- | TURNER | SALES      |     3 |
-- | ADAMS  | RESEARCH   |     1 |
-- | JAMES  | SALES      |     1 |
-- | FORD   | RESEARCH   |     4 |
-- | MILLER | ACCOUNTING |     2 |
-- +--------+------------+-------+
```

例题：找出每一个员工的部门名称、工资等级、以及上级领导。（内 + 外连接）

```sql
select e.ename,d.dname,s.grade,ee.ename 上司  from emp e join dept d on e.deptno = d.deptno join salgrade s on e.sal between s.losal and s.hisal left join emp ee on e.mgr = ee.empno;
-- +--------+------------+-------+--------+
-- | ename  | dname      | grade | 上司   |
-- +--------+------------+-------+--------+
-- | SMITH  | RESEARCH   |     1 | FORD   |
-- | ALLEN  | SALES      |     3 | BLAKE  |
-- | WARD   | SALES      |     2 | BLAKE  |
-- | JONES  | RESEARCH   |     4 | KING   |
-- | MARTIN | SALES      |     2 | BLAKE  |
-- | BLAKE  | SALES      |     4 | KING   |
-- | CLARK  | ACCOUNTING |     4 | KING   |
-- | SCOTT  | RESEARCH   |     4 | JONES  |
-- | KING   | ACCOUNTING |     5 | NULL   |
-- | TURNER | SALES      |     3 | BLAKE  |
-- | ADAMS  | RESEARCH   |     1 | SCOTT  |
-- | JAMES  | SALES      |     1 | BLAKE  |
-- | FORD   | RESEARCH   |     4 | JONES  |
-- | MILLER | ACCOUNTING |     2 | CLARK  |
-- +--------+------------+-------+--------+
```

### 子查询

子查询就是嵌套的 `select` 语句，可以理解为子查询是一张表

#### 在 where 子句中使用子查询

例题：找出高于平均工资的员工信息

```sql
select * from emp where sal > (select avg(sal) from emp);
-- +-------+-------+-----------+------+------------+---------+------+--------+
-- | EMPNO | ENAME | JOB       | MGR  | HIREDATE   | SAL     | COMM | DEPTNO |
-- +-------+-------+-----------+------+------------+---------+------+--------+
-- |  7566 | JONES | MANAGER   | 7839 | 1981-04-02 | 2975.00 | NULL |     20 |
-- |  7698 | BLAKE | MANAGER   | 7839 | 1981-05-01 | 2850.00 | NULL |     30 |
-- |  7782 | CLARK | MANAGER   | 7839 | 1981-06-09 | 2450.00 | NULL |     10 |
-- |  7788 | SCOTT | ANALYST   | 7566 | 1987-04-19 | 3000.00 | NULL |     20 |
-- |  7839 | KING  | PRESIDENT | NULL | 1981-11-17 | 5000.00 | NULL |     10 |
-- |  7902 | FORD  | ANALYST   | 7566 | 1981-12-03 | 3000.00 | NULL |     20 |
-- +-------+-------+-----------+------+------------+---------+------+--------+
```

#### from 后面嵌套子查询

例题：找出每个部门平均薪水的等级并打印出其部门名称。

```sql
select new.*,grade 薪资等级  from salgrade s join (select e.deptno 部 门编号 ,d.dname 部门名称 ,avg(e.sal) 平均薪资 from emp e join dept d on d.deptno = e.deptno group by e.deptno) new on new.平均薪资 between s.losal and s.hisal;
-- +--------------+--------------+--------------+--------------+
-- | 部门编号     | 部门名称     | 平均薪资     | 薪资等级     |
-- +--------------+--------------+--------------+--------------+
-- |           20 | RESEARCH     |  2175.000000 |            4 |
-- |           30 | SALES        |  1566.666667 |            3 |
-- |           10 | ACCOUNTING   |  2916.666667 |            4 |
-- +--------------+--------------+--------------+--------------+
```

例题：找出每个部门的平均的薪水等级。

```sql
select new.deptno,avg(new.grade) from (select e.*,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal) new group by new.deptno;
-- +--------+----------------+
-- | DEPTNO | avg(new.grade) |
-- +--------+----------------+
-- |     20 |         2.8000 |
-- |     30 |         2.5000 |
-- |     10 |         3.6667 |
-- +--------+----------------+
```

#### 在 select 后面嵌套子查询

例题：找出每个员工所在的部门名称，要求显示员工名和部门名。

```sql
select e.ename, (select d.dname from dept d where d.deptno = e.deptno) from emp e;
-- +--------+--------------------------------------------------------+
-- | ename  | (select d.dname from dept d where d.deptno = e.deptno) |
-- +--------+--------------------------------------------------------+
-- | SMITH  | RESEARCH                                               |
-- | ALLEN  | SALES                                                  |
-- | WARD   | SALES                                                  |
-- | JONES  | RESEARCH                                               |
-- | MARTIN | SALES                                                  |
-- | BLAKE  | SALES                                                  |
-- | CLARK  | ACCOUNTING                                             |
-- | SCOTT  | RESEARCH                                               |
-- | KING   | ACCOUNTING                                             |
-- | TURNER | SALES                                                  |
-- | ADAMS  | RESEARCH                                               |
-- | JAMES  | SALES                                                  |
-- | FORD   | RESEARCH                                               |
-- | MILLER | ACCOUNTING                                             |
-- +--------+--------------------------------------------------------+
```

### union（可以将查询结果集相加）

主要用于互不相干的表中数据拼接显示

例题：找出工作岗位是 SALESMAN 和 MANAGER 的员工。

```sql
select ename,job from emp where job = 'MANAGER' or job = 'SALESMAN'; -- Way One
select ename,job from emp where job in('MANAGER','SALESMAN'); -- Way Two
-- Way Three By Union
select ename,job from emp where job = 'SALESMAN'
union
select ename,job from emp where job = 'MANAGER';
-- +--------+----------+
-- | ename  | job      |
-- +--------+----------+
-- | ALLEN  | SALESMAN |
-- | WARD   | SALESMAN |
-- | MARTIN | SALESMAN |
-- | TURNER | SALESMAN |
-- | JONES  | MANAGER  |
-- | BLAKE  | MANAGER  |
-- | CLARK  | MANAGER  |
-- +--------+----------+
```

### Limit

1. `limit` 是 `Mysql` 特有的
2. `limit` 取结果集中的部分数据
3. `limit` 是 sql 语句执行最后环节
4. 语法：

```sql
limit startIndex, length
startIndex:起始位置(从 0 开始，表示第一条数据，缺省为 0 )
length:取前几个
```

案例：取出工资前 5 名的员工（思路：降序取前 5 个）

```sql
select ename,sal from emp order by sal desc;
-- 取前5个：
select ename,sal from emp order by sal desc limit 0, 5;
select ename,sal from emp order by sal desc limit 5;
```

通用的标准分页 sql

## 表

- 表：table 是数据库的基本组成单元，所有的数据都以表格的形式组织，目的是可读性强。
  一个表包括行和列：
- 行：被称为数据/记录($data$)
- 列：被称为字段($column$)
- 每一个字段应该包括的属性：字段名、数据类型、相关的约束。

### 建表

#### 语法格式

```sql
create table 表名(
    字段名1 数据类型,
    字段名2 数据类型,
    字段名3 数据类型,
 );
```

#### 加入约束

在创建表的时候，可以给表的字段添加相应的约束，添加约束的目的是为了保证表中数据的合法性、有效性、完整性。

常见的约束

- 非空约束(not null)：约束的字段不能为 NULL
- 唯一约束(unique)：约束的字段不能重复
- 主键约束(primary key)：约束的字段既不能为 NULL，也不能重复（简称 PK）
- 外键约束(foreign key)：...（简称 FK）
- 检查约束(check)：注意 Oracle 数据库有 check 约束，但是 mysql 没有，目前 mysql 不支持该约束。

#### 唯一性约束（unique）

唯一约束修饰的字段具有唯一性，不能重复。但可以为 NULL。

例题：

给某一列添加 unique

```sql
create table t_user(
    id int,
    username varchar(255) unique  -- 列级约束
);
insert into t_user values(1,'zhangsan');
insert into t_user values(2,'zhangsan');
ERROR 1062 (23000): Duplicate entry 'zhangsan' for key 'username'

insert into t_user(id) values(2);
insert into t_user(id) values(3);
insert into t_user(id) values(4);
```

给两个列或者多个列添加 unique

```sql
create table t_user(
                        id int, 
                        usercode varchar(255),
                        username varchar(255),
                        unique(usercode,username) --  多个字段联合起来添加1个约束unique 【表级约束】
                );

insert into t_user values(1,'111','zs');
insert into t_user values(2,'111','ls');
insert into t_user values(3,'222','zs');
select * from t_user;
insert into t_user values(4,'111','zs');
ERROR 1062 (23000): Duplicate entry '111-zs' for key 'usercode'

drop table if exists t_user;
create table t_user(
        id int, 
        usercode varchar(255) unique,
        username varchar(255) unique
        );
insert into t_user values(1,'111','zs');
insert into t_user values(2,'111','ls');
ERROR 1062 (23000): Duplicate entry '111' for key 'usercode'
```

#### 非空约束（not null）

与 unique 类似只不过**只有列级约束。没有表级约束。**

#### 主键约束（primary key）

引入：

```sql
create table t_user(
                        id int primary key,  --  列级约束
                        username varchar(255),
                        email varchar(255)
                );
insert into t_user(id,username,email) values(1,'zs','zs@123.com');
insert into t_user(id,username,email) values(2,'ls','ls@123.com');
insert into t_user(id,username,email) values(3,'ww','ww@123.com');
select * from t_user;
+----+----------+------------+
| id | username | email      |
+----+----------+------------+
|  1 | zs       | zs@123.com |
|  2 | ls       | ls@123.com |
|  3 | ww       | ww@123.com |
+----+----------+------------+

insert into t_user(id,username,email) values(1,'jack','jack@123.com');
ERROR 1062 (23000): Duplicate entry '1' for key 'PRIMARY'

insert into t_user(username,email) values('jack','jack@123.com');
ERROR 1364 (HY000): Field 'id' doesn't have a default value
```

根据以上得出：$id$是主键，因为添加了**主键约束**，**主键字段**中的数据不能为 **NULL**，也不能**重复**。

- **主键的特点**：不能为 **NULL**，也不能**重复**。
- **主键约束** : primary key
- **主键字段** : id 字段添加 primary key 之后，id 叫做主键字段
- **主键值** : id 字段中的每一个值都是主键值。
- **主键的作用**：主键值是这行记录在这张表当中的唯一标识，是表的设计三范式的第一范式
- **主键的分类**

根据主键字段的字段数量来划分：

1. 单一主键（推荐的，常用的）
2. 复合主键(多个字段联合起来添加一个主键约束)（复合主键不建议使用，因为复合主键违背三范式。）

根据主键性质来划分：

1. 自然主键：主键值最好就是一个和业务没有任何关系的自然数。（这种方式是推荐的）
2. 业务主键：主键值和系统的业务挂钩，例如：拿着银行卡的卡号做主键，拿着身份证号码作为主键。（不推荐用）最好不要拿着和业务挂钩的字段作为主键。因为以后的业务一旦发生改变的时候，主键值可能也需要随着发生变化，但有的时候没有办法变化，因为变化可能会导致主键值重复。

- **一张表的主键约束只能有 1 个。**

例题：使用表级约束方式定义主键

```sql
create table t_user(
                        id int,
                        username varchar(255),
                        primary key(id)
                );
insert into t_user(id,username) values(1,'zs');
insert into t_user(id,username) values(2,'ls');
insert into t_user(id,username) values(3,'ws');
insert into t_user(id,username) values(4,'cs');
select * from t_user;

insert into t_user(id,username) values(4,'cx');
ERROR 1062 (23000): Duplicate entry '4' for key 'PRIMARY'
```

以下内容是演示以下复合主键，不需要掌握：

```sql
create table t_user(
                    id int,
                    username varchar(255),
                    password varchar(255),
                    primary key(id,username)
                    );
-- insert .......
```

$mysql$提供**主键值自增**

```sql
create table t_user(
                        id int primary key auto_increment, --  id字段自动维护一个自增的数字，从1开始，以1递增。
                        username varchar(255)
                );
insert into t_user(username) values('a');
insert into t_user(username) values('b');
insert into t_user(username) values('c');
insert into t_user(username) values('d');
insert into t_user(username) values('e');
insert into t_user(username) values('f');
select * from t_user;
```

提示:$Oracle$当中也提供了一个自增机制，叫做：序列$（sequence）$对象。

#### 外键约束（foreign key）

- 外键约束: foreign key
- 外键字段：添加有外键约束的字段
- 外键值：外键字段中的每一个值
- 外键值可以为 **NULL**
- 外键字段引用其他表的某个字段的时候，被引用的字段**不一定是主键，但至少具有**$unique$**约束。**

例题：请设计数据库表，用来维护学生和班级的信息

第一种方案：一张表存储所有数据

no(pk)                        name                        classno                        classname

---

1                        zs1                        101                北京大兴区经济技术开发区亦庄二中高三 1 班

2                        zs2                        101                北京大兴区经济技术开发区亦庄二中高三 1 班

3                        zs3                        102                北京大兴区经济技术开发区亦庄二中高三 2 班

4                        zs4                        102                北京大兴区经济技术开发区亦庄二中高三 2 班

5                        zs5                        102                北京大兴区经济技术开发区亦庄二中高三 2 班

**缺点**：冗余。【不推荐】

第二种方案：两张表（班级表和学生表）

t_class 班级表

cno(pk)                cname

---

101                北京大兴区经济技术开发区亦庄二中高三 1 班

102                北京大兴区经济技术开发区亦庄二中高三 2 班

t_student 学生表

sno(pk)                sname                                classno(该字段添加外键约束 fk)

---

1                              zs1                                101

2                              zs2                                101

3                              zs3                                102

4                              zs4                                102

5                              zs5                                102

t_student 中的 classno 字段引用 t_class 表中的 cno 字段，此时 t_student 表叫做子表。t_class 表叫做父表。

顺序要求：

删除数据的时候，先删除子表，再删除父表。

添加数据的时候，先添加父表，再添加子表。

创建表的时候，先创建父表，再创建子表。

删除表的时候，先删除子表，再删除父表。

```sql
drop table if exists t_student;
drop table if exists t_class;

create table t_class(
        cno int,
        cname varchar(255),
        primary key(cno)
);

create table t_student(
        sno int,
        sname varchar(255),
        classno int,
        primary key(sno),
        foreign key(classno) references t_class(cno)
);

insert into t_class values(101,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx');
insert into t_class values(102,'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy');

insert into t_student values(1,'zs1',101);
insert into t_student values(2,'zs2',101);
insert into t_student values(3,'zs3',102);
insert into t_student values(4,'zs4',102);
insert into t_student values(5,'zs5',102);
insert into t_student values(6,'zs6',102);
select * from t_class;
select * from t_student;

insert into t_student values(7,'lisi',103);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`bjpowernode`.INT `t_student_ibfk_1` FOREIGN KEY (`classno`) REFERENCES `t_class` (`cno`))
```

### MySql 常用数据类型

char 和 varchar 怎么选择？
在实际的开发中，当某个字段中的数据长度不发生改变的时候，是定长的，例如：性别、生日等都是采用 char。
当一个字段的数据长度不确定，例如：简介、姓名等都是采用 varchar。

### 表的复制

```sql
create table 表名 as DQL语句
```

## 事务

### 概述

一个事务是一个完整的业务逻辑单元，不可再分。

比如：银行账户转账，从 A 账户向 B 账户转账 10000.需要执行两条 update 语句：

```sql
update t_act set balance = balance - 10000 where actno = 'act-001';
update t_act set balance = balance + 10000 where actno = 'act-002';
```

以上两条 DML 语句必须同时成功，或者同时失败，不允许出现一条成功，一条失败。

要想保证以上的两条 DML 语句同时成功或者同时失败，那么就需要使用数据库的“事务机制”。

事务可以保证多个操作原子性，要么全成功，要么全失败。对于数据库来说事务保证批量的 DML 要么全成功，要么全失败。事务具有四个特征 ACID：

1. 原子性（Atomicity）

   - 整个事务中的所有操作，必须作为一个单元全部完成（或全部取消）。
2. 一致性（Consistency）

   - 在事务开始之前与结束之后，数据库都保持一致状态。
3. 隔离性(Isolation)

   - 一个事务不会影响其他事务的运行。
4. 持久性(Durability)

   - 在事务完成以后，该事务对数据库所作的更改将持久地保存在数据库之中，并不会被回滚。

事务中存在一些概念：

1. 事务（Transaction）：一批操作（一组 DML）
2. 开启事务（Start Transaction）
3. 回滚事务（rollback）
4. 提交事务（commit）
5. SET AUTOCOMMIT：禁用或启用事务的自动提交模式

当执行 DML 语句是其实就是开启一个事务，和事务相关的语句只有 DML 语句（ｉｎｓｅｒｔ　ｄｅｌｅｔｅ　ｕｐｄａｔａ）

因为这三个语句都是数据库表当中的“数据”相关的。

事务的存在是为了保证数据的完整性，安全性。

如果一个业务只需一条 ＤＭＬ 即可完成那么则无需事务

关于事务的回滚需要注意：只能回滚 insert、delete 和 update 语句，不能回滚 select（回滚 select 没有任何意义），对于 create、drop、alter 这些无法回滚.

事务只对 DML 有效果。

注意：rollback，或者 commit 后事务就结束了。

### 隔离级别

**InnoDB** 实现了四个隔离级别，用以控制事务所做的修改，并将修改通告至其它并发的事务

#### 第一级别：读未提交（read uncommitted）

对方事务还没有提交，我们当前事务可以读取到对方未提交的数据。

即允许一个事务可以看到其他事务未提交的修改。

读未提交存在**脏读（Dirty Read）**现象：表示读到了**脏的数据**。

#### 第二级别：读已提交（read committed）

对方事务提交之后的数据我方可以读取到。

即允许一个事务只能看到其他事务已经提交的修改，未提交的修改是不可见的。

这种隔离级别**解决**了: 脏读现象没有了。

读已提交存在的**问题**是：不可重复读。

#### 第三级别：可重复读（repeatable read）

这种隔离级别**解决**了：不可重复读问题。

这种隔离级别存在的**问题**是：读取到的数据是幻象。

#### 第四级别：序列化读/串行化读（serializable）

**解决**了所有问题。

这种隔离级别存在的**问题**是：效率低。需要事务排队。

oracle 数据库默认的隔离级别是：**读已提交**。

mysql 数据库默认的隔离级别是：**可重复读**。

## 索引

### 概述

索引就相当于一本书的目录，通过目录可以快速的找到对应的资源。

索引被用来快速找出在一个列上用一特定值的行。没有索引，MySQL 不得不首先以第一条记录开始，然后读完整个表直到它找出相关的行。表越大，花费时间越多。对于一个有序字段，可以运用二分查找（Binary Search），这就是为什么性能能得到本质上的提高。MYISAM 和 INNODB 都是用 B+Tree 作为索引结构

索引可以提高检索效率最根本的原理是缩小了扫描的范围。

索引虽然可以提高检索效率，但是不能随意的添加索引，因为索引也是数据库当中的对象，也需要数据库不断的维护。是有维护成本的。比如，表中的数据经常被修改这样就不适合添加索引，因为数据一旦修改，索引需要重新排序，进行维护。

添加索引是给某一个字段，或者说某些字段添加索引。

```sql
select ename,sal from emp where ename = 'SMITH';
```

当 ename 字段上没有添加索引的时候，以上 sql 语句会进行全表扫描，扫描 ename 字段中所有的值。

当 ename 字段上添加索引的时候，以上 sql 语句会根据索引扫描，快速定位。

### 查看/创建/删除索引对象

查看索引对象：show index from 表名;

创建索引对象：create index 索引名称 on 表名(字段名);

删除索引对象：drop index 索引名称 on 表名;

### 适合给字段添加索引的情景

1. 表中该字段中的数据量庞大
2. 经常被检索，经常出现在 where 子句中的字段
3. 经常被 DML 操作的字段不建议添加索引

索引等同于一本书的目录。

主键会自动添加索引，所以尽量根据主键查询效率较高。

### 索引的分类

- 单一索引：给单个字段添加索引
- 复合索引: 给多个字段联合起来添加 1 个索引
- 主键索引：主键上会自动添加索引
- 唯一索引：有 unique 约束的字段上会自动添加索引

### 索引的失效

`select ename from emp where ename like '%A%';`

模糊查询的时候，第一个通配符使用的是 %，这个时候索引是失效的。

### 查看 sql 语句的执行计划

只需在 sql 语句前面加上一个 `explain` 即可
