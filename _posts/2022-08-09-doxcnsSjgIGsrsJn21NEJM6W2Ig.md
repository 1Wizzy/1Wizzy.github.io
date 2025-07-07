---
title: "DataStructure Learning Note"
date: 2022-08-09 00:00
categories: ['Note', 'DataStructure']
tags: ['Note', 'DataStructure']
---



## DataStructure

## **图**

### **一、概念**

图是由顶点集合和顶点之间边的集合组成，通常表示为$G-V-E(G(V,E))$，其中$G$表示图$(Graph)$，$V$是$G$中顶点的集合，$E$是$G$中边的集合。

### **二、分类**

![](static/boxcnK2169IrQH2w5WXXZT2g82g.png)

### **三、存储**

#### **选择**

如果边的条数$E << 顶点数量V^2$ ，这种图称为系稀疏图，反之称为稠密图。

一般来说，用**邻接表** 来表示 **稀疏图** ，用**邻接矩阵** 来表示 **稠密图**

#### **邻接矩阵（二维数组）**

例如：

![](static/boxcnj9MYN98AyqjeCgSnNysM8e.png)

对于$G1$，有                                               对于$G3$，有

![](static/boxcnwNFBMWHUOyhVklftyQN4ih.png)
![](static/boxcn1VPJsunF5xn0AivnY4M3nd.png)

#### **邻接表**

![](static/boxcnf2HeVjTT52M0TJVhqNKWqf.png)

实例代码：

```cpp
const int N=52647;
int h[N];//链表头        h[a]中索引存放的是(a->b)a点的编号
int e[N];//值        e[idx]的结果存放的是(a->b)中b点的编号,表示新建一个结点
int ne[N];//next pointer
int idx;//索引
/*
首先，我们开三个数组:
h[i]表示以i为起点的第一条边的存储位置。说是第一条边，其实是最后读入（编号最大）的边，只是便于从头扫边。
ne[i]表示与第i条边同起点的下一条边的存储位置。下一条边，反而是前一个由起点扩展的边，只是便于跳边。
e[i]表示第i条边的终点。（即当前边连向的点）
v[i]表示第i条边的权值（视情况决定是否使用）
*/
int add(int a ,int b )//a is head , b is value a--->b
{
    e[idx]=b;//第idx条边的终点为b//为下标为idx的指针开辟一个数据域空间，存入x//e的idx索引值为b
    ne[idx]=h[a];//第idx条边的下一条边的索引，初始为-1//为下标为idx的指针开辟一个指针域空间，存入头结点的指向（目前是-1）//下一个idx索引的索引        
    h[a]=idx;//idx索引更新//头结点指向idx
    idx++;//idx索引增加//准备开辟下一个节点空间
}

int main()
{
    memset(h,-1,sizeof h);//1--->-1
    add(1,2);//1--->2--->-1
    add(1,3);//1--->3--->2--->-1 
    add(1,4);//1--->4--->3--->2--->-1
    for(int i = h[1]; i!= -1 ; i=ne[i]) //打印以 1 为 根 的树             
    {
        cout << e[i] << endl;   
    }
}
//analyze by steps
//Add Steps
add(1,2)<=>{e[0]=2;ne[0]=h[1];h[1]=0;idx=1;}
add(1,3)<=>{e[1]=3;ne[1]=h[1];h[1]=1;idx=2;}
add(1,4)<=>{e[2]=4;ne[2]=h[1];h[1]=2;idx=3;}
//in the end 
e[0]=2,e[1]=3,e[2]=4;
ne[0]=-1,ne[1]=0,ne[2]=1;
h[1]=0,h[1]=1,h[1]=2;
//Print Steps
1:i=h[1];                cout << e[h[1]] << endl;        <=>        e[2]        <=>         4 
2:i=ne[h[1]];        cout << e[ne[h[1]]] << endl;        <=>         e[1]        <=>        3
3.i=ne[ne[h[1]]];        cout << e[ne[ne[h[1]]]] << endl;<=>        e[0]        <=>        2
4.i=ne[ne[ne[h[1]]]];        i=ne[0]=-1        EndTheForLoop
<=>e[2]--e[1]--e[0];        <=>        e[2--ne[2]--ne[ne[2]]]
```

理解失败！！！

模板代码：

Mode details in AcWing826.单链表

```cpp
#include<isotream>
#include<cstring>
const int N=52647;
int h[N],e[N],ne[N],idx=0;
void add(int a,int b)
{
    e[idx]=b;
    ne[idx]=h[a];
    h[a]=idx++;
}
int main()
{
    memset(h,-1,sizeof h);//初始化 很关键！！！
    for(int i = h[root] ; i!=-1 ;i=ne[i]) //遍历以root为根的所有连接的点
    {
        /*Code*/    
    }
}
```

必背模板代码

#### **链式前向星**

链式前向星主要用于边比较多，顶点比较少的情况。

链式前向星的优点：比邻接表还省空间，可以解决某些卡空间的问题，删除边也很方便，只需要更改$next$指针的指向即可。

总结：根据图的疏密选择存储方式，一般情况下用邻接表，卡空间时间这些要求比较高的题目或者需要删除边操作的用链式前向星。

```cpp
int head[MaxV];//表示以i为起点的最后一个顶点的编号，初始为-1
int cnt;//全局变量，cnt为边的编号
struct Node
{
    int v;//终点
    int w;//边权
    int next;//与这条边起点相同的上一条边的编号
}
void addedge(u,v,w)
{
    edge[cnt].v=v;
    edge[cnt].w=w;
    edge[cnt].next=head[u];//表示以u为起点的最后一个顶点的编号
    head[u]=cnt++;//当前编号
}
```

### **四、图论**

#### **负权回路**

例如

![](static/boxcn9DElB3TplUm2XCpY6SH2sf.png)

#### **自环**

一条边的起点终点是一个点

#### **重边**

就是在两点之间有多条边连接(大于或等于 2)

### **五、More detalis in Video BV1D5411c71o**

## **树**

### **一、概念**

树可以被认为是没有**回路**的**无向连通**图

Trees are **connected acyclic ****undirected** graphs.

### **二、性质**

If a tree has $n$ vertices, then it has $n-1$ edges

if less than $n-1$ edges -> Disconnected

if more than $n-1$ edges ->There is a cycle

No cycles

Connected

### 三、存储

#### 单独存左右父节点

##### 模板

```cpp
const int N = 1010;
int l[N], r[N], p[N];
```

##### 例题

###### Question:AcWing 3555.二叉树

Question Link:acwing.com/problem/content/3558

Question Difficulty Level:★☆☆☆☆

Question Analysis:

对于树上两个结点的最短路径长度，最简单暴力的是存成图，用最短路径算法，但由于是在树上，且父节点与子节点的距离是一，所以此题可转换为 LCA 问题

![](static/boxcndlKkQs1g988OxDEPaUT6hS.png)

若求节点$A$与节点$B$之间的最短路径长度，则为$dist[A] + dist[B] - 2 × dist[C]$

Code:

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int N = 1010;
int l[N], r[N], p[N], dist[N];
void dfs(int u, int d)
{
    if(l[u] != -1) dfs(l[u], d + 1);
    if(r[u] != -1) dfs(r[u], d + 1);
    dist[u] = d;
}
int get_lca(int x, int y)// dist[x] > dist[y]
{
    if(dist[x] < dist[y]) return get_lca(y, x);
    while (dist[x] > dist[y]) x = p[x];//长度相同则深度相同
    while (x != y) x = p[x], y = p[y];
    return x;
    
}
int main()
{
    int T;
    cin >> T;
    while (T -- )
    {
        int n, m;
        cin >> n >> m;
        for (int i = 1; i <= n; i ++ )
        {
            int a, b;
            cin >> a >> b;
            l[i] = a, r[i] = b;
            if(a != -1) p[a] = i;
            if(b != -1) p[b] = i;
        }
        dfs(1,0);
        while (m -- )
        {
            int x, y;
            cin >> x >> y; 
            int z = get_lca(x, y);
            cout << dist[x] + dist[y] - 2 * dist[z] << endl;
        }
    }
    return 0;
}
```

## **树状数组（二叉索引树）（Binary Indexed Tree）**

### **一、概念**

树状数组或二叉索引树（英语：`Binary Indexed Tree`），又以其发明者命名为$Fenwick$树，最早由$Peter M. Fenwick$于 1994 年以 A New Data Structure for Cumulative Frequency Tables 为题发表在 SOFTWARE PRACTICE AND EXPERIENCE。

### **二、运用场景**

解决数据压缩里的累积频率（Cumulative Frequency）的计算问题，现多用于高效计算数列的前缀和， 区间和。

对于任意区间 能够在较小的时间复杂度内 得到 区间和。

在数组中添加一个数 能够在较小的时间复杂度内 更新 区间和。

### **三、模板代码**

#### **LowBit Calculate**

```cpp
int lowbit(int x)
{
    return (x & (-x));
}
```

#### **Making The Tree**

Law:

- t[x]保存以 x 为根的子树中叶节点值的和
- t[x]节点的长度等于 lowbit(x)
- t[x]节点的父节点为 t[x+lowbit(x)]
- 整棵树的深度为 log n + 1

![](static/boxcnxGVFSapiYP6ucI7RTiWzdg.png)

![](static/boxcnODFdaaeLnOaeUpIttBJtCe.png)

**O(n)初始化方法：**

$a[N]$ 为原数组 $s[N]$为前缀和数组, $tr[N]$为树状数组

$$
tr[x] = s[x] - s[x-lowbit(x)]
$$

#### **add(x,k):原数组 a[x]=a[x]+k**

```cpp
void add(int x,int k)//a[x]=a[x]+k to update the t[x]
{
    for(;x<=n;x=x+lowbit(x)) t[x]=t[x]+k;//n是边界即最大到a[n]
}
```

![](static/boxcnJmXn1Uo2rf8kjXDjZRmdKd.png)

#### **GetSum(int x):x 的前缀和（即 a[1]+a[2]+...+a[x]）**

```cpp
int GetSum(int x)//Calculate a[1]+a[2]+...+a[x] by t[x] 
{
    int ans=0;
    for(;x;x=x-lowbit(x)) ans=ans+t[x];
    return ans;
}
```

![](static/boxcncWerAKTCoUy7xGsQPbcnCd.png)

**More details in Video BV1pE41197Qj**

Code from Y

```cpp
int lowbit(int x)
{
    return x & -x;
}

void update(int x, int c)  // 位置x加c
{
    for (int i = x; i <= n; i += lowbit(i)) tr[i] += c;
}

int query(int x)  // 返回前x个数的和
{
    int res = 0;
    for (int i = x; i; i -= lowbit(i)) res += tr[i];
    return res;
}
```

### **四、实例代码**

```cpp
/*
标题：小朋友排队
n 个小朋友站成一排。现在要把他们按身高从低到高的顺序排列，但是每次只能交换位置相邻的两个小朋友。
每个小朋友都有一个不高兴的程度。开始的时候，所有小朋友的不高兴程度都是0。
如果某个小朋友第一次被要求交换，则他的不高兴程度增加1，如果第二次要求他交换，则他的不高兴程度增加2（即不高兴程度为3），依次类推。当要求某个小朋友第k次交换时，他的不高兴程度增加k。
请问，要让所有小朋友按从低到高排队，他们的不高兴程度之和最小是多少。
如果有两个小朋友身高一样，则他们谁站在谁前面是没有关系的。
【数据格式】
输入的第一行包含一个整数n，表示小朋友的个数。
第二行包含 n 个整数 H1 H2 … Hn，分别表示每个小朋友的身高。
输出一行，包含一个整数，表示小朋友的不高兴程度和的最小值。
例如，输入：
3
3 2 1
程序应该输出：
9
【样例说明】
首先交换身高为3和2的小朋友，再交换身高为3和1的小朋友，再交换身高为2和1的小朋友，每个小朋友的不高兴程度都是3，总和为9。
【数据规模与约定】
对于10%的数据， 1<=n<=10；
对于30%的数据， 1<=n<=1000；
对于50%的数据， 1<=n<=10000；
对于100%的数据，1<=n<=100000，0<=Hi<=1000000。
资源约定：
峰值内存消耗 < 256M
CPU消耗  < 1000ms
请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。
所有代码放在同一个源文件中，调试通过后，拷贝提交该源码。
注意: main函数需要返回0
注意: 只使用ANSI C/ANSI C++ 标准，不要调用依赖于编译环境或操作系统的特殊函数。
注意: 所有依赖的函数必须明确地在源文件中 #include <xxx>， 不能通过工程设置而省略常用头文件。
提交时，注意选择所期望的编译器类型。
*/
#include<iostream>
#include<cstring>
using namespace std;
const int N = 1e6 + 10;
typedef long long ll;
int n;
int c[N], a[N];
int sum[N];//sum数组存储每个小朋友的不高兴度
int lowbit(int x) {
    return x & -x;
}
void add(int x, int v) {
    for (; x < N; x += lowbit(x)) {
        c[x] += v;
    }
}
int ask(int x) {
    int ans = 0;
    for (; x; x -= lowbit(x)) {
        ans += c[x];
    }
    return ans;
}
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        a[i]++;//身高是从0开始,所以++ 从1开始
    }
    // 求每个数前面有多少个数比它大
    for (int i = 0; i < n; i++) {
        sum[i] = ask(N - 1) - ask(a[i]);
        add(a[i], 1);
    }
    //清空树状数组
    memset(c, 0, sizeof c);
    //找出比这个数小的数有多少个
    //注意这里必须倒着更新，否则无法算出高的层的数值
    for (int i = n - 1; i >= 0; i--) {
        sum[i] += ask(a[i] - 1);
        add(a[i], 1);
    }
    ll res = 0;
    for (int i = 0; i < n; i++) {
        //等差数列求和 不高兴度的总和为从1+2+..+sum[i]
        res += (ll) sum[i] * (sum[i] + 1) / 2;
    }
    cout << res << endl;
    return 0;
}
```

### 五、其他应用

#### 树状数组求逆序对

```cpp
int res = 0;
for(int i=1;i<=n;i++)
{
    int val;
    cin >> val;
    insert(val,1);
    res += i - query(val);//统计当前序列中大于a的元素的个数        
}
return res;
```

Example: [AcWing 107. 超快速排序](https://www.acwing.com/problem/content/109/)

#### 区间加，单点和

将差分数组做成树状数组即可

Example: [AcWing 242. 一个简单的整数问题 1](https://www.acwing.com/problem/content/248/)

#### 区间加，区间和

1. 原数组 a 变差分数组 b
   ```cpp
   ```

if(a[l~r]) + c
b[l] += c b[r + 1] -= c

```

2. Sum = a_1+...+a_x
	```cpp
for (int i = 1; i <= x; i ++)
    for (int j = 1; j <= i; j ++)
        Sum += b[i][j];
```

Example: [AcWing 243. 一个简单的整数问题 2](https://www.acwing.com/problem/content/244/)

# **并查集**

**一、概念**

**二、模板代码**

```cpp
const int N=1005;//Nodes count
int p[N];
int find(int x)//找到x节点的父节点p[x]
{
    return p[x]==x ? x : p[x]=find(p[x]);
    /*
    if(p[x]==x)//如果其父节点是其本身(它就是最nb的节点)
            return x；
    else 
        p[x]=find(p[x]);//令x的父节点p[x]去寻找其父节点并赋值(路径压缩)       
    return find(p[x]);                        
    */
}
void merge(int x,int y)//将两个不同元素所在的集合合并为一个集合
{
    p[find(x)]=find(p[y]);//找到x的祖宗，令其等于y的祖宗
}
```

**三、示例代码**

Question:AcWing 4304.字符串归类

Question Link:acwing.com/problem/content/4307

Question Algorithm:None

Question Difficulty Level:★★★☆☆

Question Analysis:

本题最终要输出种类数目，即输出符合 p[i]=i 的数目，

id[N]

Code:

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int N = 2e5+5;
int p[N];
int id[30];//第一个出现字母的字符串id
char str[55];
int n;
int find(int x)  // 并查集
{
    if (p[x] != x) p[x] = find(p[x]);
    return p[x];
}
void merge(int x,int y)
{
    p[find(x)]=find(y);
}
int main()
{
    cin >> n;
    int res=n;
    for (int i = 0; i <= n; i ++ ) p[i]=i;
    
    
    for (int i = 1; i <= n; i ++ )
    {
        cin >> str;
        for (int j = 0; str[j]; j ++ )
        {
            int c=str[j]-'a';
            if(id[c])//如果这个字母已经出现过
            {
                if(find(i)!=find(id[c])) 
                {
                    merge(i,id[c]);
                    res--;
                    
                }
            }
            else id[c]=i;
        }
    }
    int ans=0;
    for(int i=1;i<=n;i++) if(i==find(i)) ans++;
    cout << ans << endl;
    //cout << res << endl;
}
```

# **ST (Sparse Table)**

**一、概念**

ST 表（稀疏表）是一种用于处理可重复贡献问题的数据结构，可以处理解决静态 RMQ(Range Minimum/Maximum Query)(区间最大/最小值查询)问题。

它主要应用倍增的思想，可以实现 O(nlogn)预处理，O(1)查询。

**二、运用场景**

区间最大/最小值查询

**三、模板代码**

**0.声明**

```
            //以下"^"代表幂符号而非异或符号
```

//无特殊说明 log 均以 2 为底
int a[N];//原数组
int st[i][j];
//st[i][j]表示数组 a 的第 i 项到第 i+2^j-1 项(即[i,i+2^j-1])的极值,即 st[i][j]=st[i][i+2^j-1]

**1.预处理阶段**

```
            st[i][0]=max/min([a[i],a[i+2^j-1]])=a[i]//经分析可知
```

Analysis:
Because of 2^j=2*2^(j-1), we can divide [i,i+2^j-1] into two same legth intervals,
Then the finalresult is the max/min of the two intervals max/min
The first intervals be divided bring the st[i][j-1]=[i,i+2^(j-1)-1]
The last intervals be divided biring the [i+2^(j-1),i+2^j-1]=st[i+2^(j-1)][j-1]
Such as st[5][2]=[5,8] can be divided [5,6] and [7,8]
i=5        j=2
[i,i+2^(j-1)-1]=[5,5+2-1]=[5,6]        [i+2^(j-1),i+2^j-1]=[5+2,5+4-1]=[7,8]
2 的幂的优化后 Code:
for (int i = 1; i <= n; ++i) st[i][0] = a[i];
//Care The Range!!!
for (int j = 1; (1 << j) <= n; ++j)
{
for (int i = 1; i + (1 << j) - 1 <= n; ++i)
{
st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
}
}

**2.查询[l,r]的最值**

```
            由于区间长度 r-l+1 不一定为2的整数幂(即不一定满足log(r-l+1)∈N),所以只能分步求
```

设 k=log(r-l+1) 然后将区间分为 [l,l + 2^k - 1](%5Bl,r%5D%E7%BB%8F%E5%8E%BB%E6%95%B4) and [r - 2^k + 1,r](%5Bl,r%5D%E7%BB%8F%E5%8E%BB%E6%95%B4),显然这两段是必然有重复区域[r-2^k+1,l+2^k-1]
但是我们处理的是区间最值问题，因此有重复不会影响我们的结果。
对于区间[l,l+2^k-1],其长度为 2^k,其最值可表示为 st[l][k]
对于区间[r-2^k+1,r],其长度为 2^k,其最值可表示为 st[r - 2^k + 1][k]
Code:
int search(int l,int r)
{
int k=log2(r-l+1);
return max(st[l][k],st[r-(1<<k)+1][k]);
}

**Note cited from luogu.com.cn/blog/Jaanai/solution-p3865;**

**四、实例代码**

```cpp
//Question Link:https://www.luogu.com.cn/problem/P3865
#include <bits/stdc++.h>
using namespace std;
#define MAX_N 100010
int st[MAX_N][20];
inline int Query(int l, int r) {
  int k = log2(r - l + 1);
  return max(st[l][k], st[r - (1 << k) + 1][k]);
}
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i)
    scanf("%d", &st[i][0]);
  for (int k = 1; (1 << k) <= n; ++k)
    for (int i = 1; i + (1 << k) - 1 <= n; ++i)
      st[i][k] = max(st[i][k - 1], st[i + (1 << (k - 1))][k - 1]);
  for (int i = 1; i <= m; ++i) {
    int l, r;
    scanf("%d%d", &l, &r);
    printf("%d\n", Query(l, r));
  }
  return 0;
}
```

# 链表

此处不给出过多定义仅给出思路及模板

## 数组模拟单链表

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int N = 100010;
int head = -1, e[N], ne[N], idx = 1;
/*
 * head代表头节点的idx
 * e[i]表示节点i的值是多少 
 * ne[i]表示节点i的next指针
 * 
 */
 
void PushFront(int val)
{
    e[idx] = val;//新建一个索引值为idx、值为val的点
    ne[idx] = head;//新建点的下一个点为原来的头节点
    head = idx ++;//更新头节点并且idx自增
}

void del(int k)//删除第 k 个插入的数后面的数
{
    //第一个插入的数的索引值是 1 ,那么第 k 个插入的数的索引值就是 k
    if(k) ne[k] = ne[ne[k]];
    else head = ne[head];
}

void ins(int k, int x)//在第 k 个插入的数后面插入一个数 x
{
    //新建点
    e[idx] = x;
    ne[idx] = ne[k];
    ne[k] = idx ++;
}

int main()
{
    int m;
    cin >> m;
    while (m -- )
    {
        char op;
        int k, x;
        cin >> op;
        if(op == 'H')
        {
            cin >> x;
            PushFront(x);
        }
        else if(op == 'D')
        {
            cin >> k;
            del(k);
        }
        else
        {
            cin >> k >> x;
            ins(k, x);
        }
    }
    for (int i = head; ~i; i = ne[i] )
        cout << e[i] << ' ';
    return 0;
}
```

# Trie

## 定义

Trie 树用来高效地存储和查找字符串

# 堆

堆多为树结构

具体定义等此处不再多写

## 手写堆

此处拿小根堆举例

这个手写堆可以实现：

1. 插入一个数

`heap[++ size]; up(size)`

1. 求集合当中的最小值
   `heap[1];`
2. 删除最小值

`heap[1] = heap[size];size --; down(1)`

1. 删除任意一个元素

`heap[k] = heap[size]; size --;down(k),up(k);`

> 因为在数组不易在删除前面的元素故此将最后的元素覆盖在被删除的元素，然后进行维护即可。

1. 修改任意一个元素

`heap[k] = x; down(k), up(k);`

> 为了使得模板代码精炼，故在此不判断是 up 还是 down，但是实际执行结果只会执行一个

有两个基础操作：

- `down(int u)` 操作：即向下维护 `heap[u]` 在堆中的位置，将 `u` 与 `u` 的左右儿子的最小值交换，然后递归执行下去

```cpp

```

- `up(int u)` 操作：即向上维护 `heap[u]` 在堆中的位置，如果**u****的 父节点的值 > ****heap[u]**** **则交换他们，直至不能交换为止

此处用一维数组作为堆的存储结构，下标索引从 1 开始。

我们令 `x` 的左儿子为 `2x` 右儿子为 `2x+1` ，堆的大小为 `size`

### 模板

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int N = 100010;
int h[N], cnt, n;
int idxh[N], hidx[N], idx;//idx:插入的第几个元素
//idxh[i] 表示第 i 个 插入的元素在heap中的下标 idx->heapidx
//hidx[i] 表示heap[i] 是第 几 个被插入的 heapidx->idx
void heap_swap(int a, int b)//a and b is the heap index
{
    
    swap(idxh[hidx[a]], idxh[hidx[b]]);
    swap(hidx[a], hidx[b]);
    swap(h[a], h[b]);
}
void down(int u)//input heap index
{
    int t = u;
    if(2 * u <= cnt && h[2 * u] < h[t]) t = 2 * u;
    if(2 * u + 1<= cnt && h[2 * u + 1] < h[t]) t = 2 * u + 1;
    if(t != u)
    {
        heap_swap(t, u);
        down(t);
    }
}

void up(int u)//input heap index
{
    while(u / 2 && h[u] < h[u / 2])
    {
        heap_swap(u, u / 2);
        u /= 2;
    }
}

int main()
{
    cin >> n;
    while (n -- )
    {
        string op;
        int loc, val;
        cin >> op;
        if(op == "I")
        {
            cin >> loc;
            cnt ++;
            idx ++;
            hidx[cnt] = idx;
            idxh[idx] = cnt;
            h[cnt] = loc;
            up(cnt);
        }
        else if(op == "PM") cout << h[1] << endl;
        else if(op == "DM")
        {
            heap_swap(1, cnt);
            cnt --;
            down(1);
        }
        else if(op == "D")
        {
           cin >> loc;
           int k = idxh[loc];
           heap_swap(k, cnt);
           cnt --;
           up(k), down(k);
        }
        else
        {
            cin >> loc >> val;
            int k = idxh[loc];
            h[k] = val;
            up(k), down(k);
        }
    }
    return 0;
}
```

### 应用

#### 堆排序

先构建堆，输出且删除 `heap[1]` 继续维护删除即可

Question:AcWing 838.堆排序

Question Link:acwing.com/problem/content/840

Question Algorithm:Heap Sort

Question Difficulty Level:☆☆☆☆☆

Question Analysis:

Code:

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int N = 100010;
int h[N], n, m, cnt;
//x's left child is 2x the right one is 2x + 1
void down(int u)
{
    //u是原始位置，t是即将交换到的位置
    int t = u;
    if(2 * u <= cnt && h[2 * u] < h[t]) t = 2 * u;
    if(2 * u + 1 <= cnt && h[2 * u + 1] < h[t]) t = 2 * u + 1;
    if(u != t)
    {
        swap(h[u], h[t]);
        down(t);
    }
}

int main()
{
    cin >> n >> m;
    for (int i = 1; i <= n; i ++ ) cin >> h[i];
    cnt = n;
    for (int i = n / 2; i ; i --) down(i);
    while (m -- )
    {
        cout << h[1] << ' ';
        h[1] = h[cnt];
        cnt --;
        down(1);
    }
    return 0;
}
```

# Question=>Datastructure

## 维护二维矩阵中指定大小的矩阵其中元素的最大值和最小值
