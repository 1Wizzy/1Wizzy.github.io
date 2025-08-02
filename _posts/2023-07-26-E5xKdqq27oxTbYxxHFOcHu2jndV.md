---
title: "2023暑假ByteDance青训营笔记"
date: 2023-07-26 00:00
categories: ['Note']
tags: ['Note', 'FrontEnd']
---



## 2023 暑假 ByteDance 青训营

## Lesson 1 前端语言串讲

VideoLink: [前端语言串讲 - 掘金](https://juejin.cn/course/bytetech/7219155491984212024/section/7221509542458097725)

### 前端语言的基本能力

![](static/KuxubYfGPoOWhrxXrUNc3ef0nud.png)

#### Browser

Browser 通常包含两种引擎：渲染引擎 和 JavaScript 引擎

渲染引擎的工作如下：

![](static/BJ4abiGTgoY89mxfjfUcQfcgnLf.png)

JavaScript 引擎的工作如下：（以 V8 为例）

![](static/KyY5b9LUrodGrLx5GaccomIwn3c.png)

### 前端语言的协作配合

#### Trending

![](static/U5iIbXe5jo4iW3xYvXGcg2vanoc.png)

#### CSS in HTML

- Inline CSS

```css
<p style="color: blue;"> This is a paragraph. </p>
```

- Internal CSS

```css
<head>
    <style type = text/css>
        body {background-color: blue;}
        p {color: yellow;}
    </style>
</head>
```

- External CSS

```css
<head>
    <link rel="stylesheet" type="text/css" herf="style.css">
</head>
```

#### JavaScript in HTML

JavaScript in HTML 有个很重要的内容——DOM：它把页面上 HTML 转化为 Javascript 对象，例如：

![](static/MMsUbNOkxo2nACxiGt1cCg9dnub.png)

事件机制：

![](static/NsIsblCTkobucmxKeLlclTh1n8b.png)

任务机制：

![](static/ASD8bkRquocsqPxLVPfcDnV0nGf.png)

> MICROTASK First

#### HTML in Javascript

通过 Javascript 修改 HTML

![](static/PwBBbtLdEo0i4WxRbYocrvZAnth.png)

#### CSS in Javascript

通过 Javascript 修改 CSS

![](static/B4bzbKXYlot0oGxGa3ic4hnQnYC.png)

### HTML

![](static/ZUXbbHkT2oibYsxhZvWcl4XXnGf.png)

#### HTML DTD

HTML 并非图灵完备，它只是一门标记语言，基本语法如下

![](static/L3a8bLViyovj91xB2FDcHJkmnof.png)

#### HTML 全部标签分类

![](static/NWH8bBV7BoUHytxjByTcppP0nrb.png)

#### HTML head Tag

![](static/GnIqbYHajoVryDxiqOQcHyO3nTf.png)

#### HTML body Tag

![](static/CULzbr4pFonLt7x4svScWMl1nKf.png)

#### HTML ARIA

了解 ARIA 并非只是为了供盲人阅读，它可以为我们设计 UI 系统提供指导意义。

![](static/L63gb9fWrobwv3xDBQYcbUiOnN8.png)

#### HTML5 语义化标签

![](static/UATwbPF7eoZhYsxppojcdSJjnye.png)

#### HTML5 表单增强

![](static/FaN7bMQyfomlKxx3FBucVEEinMd.png)

#### HTML 存储

![](static/I8dcbfIx3olXnpxox4Zcp8hdnZf.png)

#### HTML IndexedDB

![](static/TFCibE2GYo9ovexpueecEZrWnHb.png)

#### HTML5 PWA & AWP

![](static/PPiXbHNCgooLrkxtYg1cMmySnKL.png)
![](static/OActblHYHobi73x8mY9cSgmPnNh.png)

#### HTML5 Audio

![](static/TCFMbaGo7oPGogxyDX0c6ElsnMb.png)

#### HTML5 Video

![](static/Krd4bsmWDoLDBjxUnlScJEgMnAe.png)

#### HTML5 Binary

![](static/U0LfbARf0oh41mxQXRpc8duZnh9.png)

#### HTML5 API

![](static/ESH6bX1mqo9qS4xxYBNc8K4XnQh.png)

#### HTML5 Worker

![](static/XWbFbage0oCJSExM1fWchHTWn0f.png)

#### HTML5 Web Socket

![](static/Aa7Mb8duuoQ8dQxO4RZcou4EnWb.png)

```javascript
// Create WebSocket connection.
const socket = new WebSocket('ws://localhost:8080')
// Connection opened
socket.addEventListener('open'，(event) => {
    socket.send('Hello Server!');
});
// Listen for messages
socket.addEventListener('message'， (event) => {
    console.log('Message from server '，event.data);
});
```

#### HTML5 Shadow DOM

![](static/Wf4Zb0i5Toa5AfxVOBkc6s8knch.png)

#### HTML5 Web Component

自定义标签的能力

![](static/GH4jbhO2bo72mNxsIcqcXQlonZg.png)

#### HTML5 SVG & Canvas

![](static/My31b4TQvo5chvx02VScHe0knXe.png)
![](static/YVGKbPdmFo7hA2xAU45cFzq1nPd.png)

#### WebGL & WebGPU

![](static/Ff7DbcKtlopAEaxZ4vkcFZ3gnDd.png)

![](static/Ss0jbK51KoOt4JxSRrTcFuLlnld.png)

#### HTML5 WebAssembly

WebAssembly(WSAM) 是一种新的编码方式，可以直接在浏览器中运行

![](static/ZqTjbHQWCoAUgxxUEdTcddeGnbb.png)

![](static/SKrSbgN15oZq08x5cxxcQnmjnPd.png)

### 拓展交流

#### Web 的风靡

![](static/LShob7prGo6hkSxnBidc6s6Gntf.png)

#### 大前端

![](static/XeGfbhQd9oMPUAxNoBmcpTxEnQh.png)
![](static/AAipbsKCbo9ouhxhYNycQocDnFe.png)

![](static/IrqzbY1TSoTeM2xpLDMcXwOdnVe.png)

#### MVC & MVVM & MVP

![](static/RMiKbvXGeoBuWaxJzNucASHnnSg.png)

![](static/SjlCb4YMKo4IwUxkyaPcAvFXnte.png)
![](static/EvwKb5NfHo9xahx8uBLcb3hEnoG.png)
![](static/J12xbnZnvoSCk9xKEiocSKLonKd.png)

### 总结

![](static/UtkgbI21CoZOv0xuFk2cDnsfnCb.png)

## Lesson 3 深入 CSS

### CSS 是什么？

- Cascading Style Sheets
- 用来定义页面元素的样式

  - 设置字体和颜色
  - 设置位置和大小
  - 添加动画效果
- CSS 的基本

![](static/EPvXbqbLyozVgMxpPaAcP6JSnne.png)

### 在页面使用 CSS

- 外链(Recommend)

```html
<link rel="stylesheet" href="/assets/style/css">
```

- 嵌入

```html
<style>
    li { margin: 0; list-style: none; }
    p { margin: lem 0; }
</style>
```

- 内联

```html
<p style="margin: lem 0">Example Content</p>
```

Simple Example: [codepen.io](https://codepen.io/webzhao/embed/mdBGZMe?default-tab=html%2Cresult&editable=true&theme-id=40116)

### CSS 是如何工作的

![](static/YTZ8bbS6mo4fCRxr4ZWc4M23nzb.png)

### 选择器

- 找出页面中的元素，以便给他们设置样式
- 使用多种方式选择元素

  - 按照标签名、类名或 id
  - 按照属性
  - 按照 DOM 树中的位置

#### 一些常规的选择器:

- 通配选择器 *

```html
<h1>This is heading</h1>
<p>this is some paragraph.</p>

<style>
* {
  color: red;
  font-size: 20px;
}
</style>
```

- 标签选择器 h1

```html
<h1>This is heading</h1>
<p>this is some paragraph.</p>

<style>
h1 {
  color: orange;
}
p {
  color: gray;
  font-size: 20px;
}
</style>
```

- id 选择器 #id

```html
<h1 id="logo">
  <img src="https://assets.codepen.io/59477/h5-logo.svg" alt="HTML5 logo" width="48" />
  HTML5 文档
<h1>

<style>
  #logo {
    font-size: 60px;
    font-weight: 200;
  }
</style>
```

- 类选择器 .class

```html
<h2>Todo List</h2>
<ul>
  <li class="done">Learn HTML</li>
  <li class="done">Learn CSS</li>
  <li>Learn JavaScript</li>
</ul>
<style>
.done {
  color: gray;
  text-decoration: line-through;
}
</style>
```

- 属性选择器 [property] or label[property=value]

```html
<label>用户名：</label>
<input value="zhao" disabled />

<label>密码：</label>
<input value="123456" type="password" />

<style>
  [disabled] {
    background: #eee;
    color: #999;
  }
</style>
```

```html
<p>
  <label>密码：</label>
  <input type="password" value="123456" />
</p>

<style>
  input[type="password"] {
    border-color: red;
    color: red;
  }
</style>
```

```html
<p><a href="#top">回到顶部</a></p>
<p><a href="a.jpg">查看图片</a></p>

<style>
  a[href^="#"] {
    color: #f54767;
    background: 0 center/1em url(https://assets.codepen.io/59477/arrow-up.png) no-repeat;
    padding-left: 1.1em;
  }
 
  a[href$=".jpg"] {
    color: deepskyblue;
    background: 0 center/1em url(https://assets.codepen.io/59477/image3.png) no-repeat;
    padding-left: 1.2em;
  }
</style>
```

#### 伪类(pseudo-classes)选择器

伪类：父亲节点的相对位置

- 不基于标签和属性定位元素
- 几种伪类

  - 状态伪类：元素处于某种状态

```html
<a href="http://example.com">
  example.com
</a>

<label>
  用户名：
  <input type="text">
</label>

<style>
a:link {
  color: black;
}

a:visited {
  color: gray;
}

a:hover {
  color: orange;
}

a:active {
  color: red;
}

:focus {
  outline: 2px solid orange;
}
</style>
```

- 结构型伪类：通过 DOM 树

```html
<ol>
  <li>阿凡达</li>
  <li>泰坦尼克号</li>
  <li>星球大战：原力觉醒</li>
  <li>复仇者联盟 3</li>
  <li>侏罗纪世界</li>
</ol>

<style>
li {
  list-style-position: inside;
  border-bottom: 1px solid;
  padding: 0.5em
}

li:first-child {
  color: coral
}

li:last-child {
  border-bottom: none;
}
</style>
```

#### 组合(Combinators)选择器

<table>
<tr>
<td>名称<br/></td><td>语法<br/></td><td>说明<br/></td><td>示例<br/></td></tr>
<tr>
<td>直接组合<br/></td><td>AB<br/></td><td>满足 A 同时满足 B<br/></td><td>input: focus<br/></td></tr>
<tr>
<td>后代组合<br/></td><td>A B<br/></td><td>选中 B，如果它是 A 的子孙<br/></td><td>nav a<br/></td></tr>
<tr>
<td>亲自组合<br/></td><td>A > B<br/></td><td>选中 B，如果它是 A 的子元素<br/></td><td>section > p<br/></td></tr>
<tr>
<td>兄弟选择器<br/></td><td>A ~ B<br/></td><td>选中 B，如果它在 A 后且和 A 同级<br/></td><td>h2 ~p<br/></td></tr>
<tr>
<td>相邻选择器<br/></td><td>A + B<br/></td><td>选中 B，如果它紧跟在 A 后面<br/></td><td>h2 + p<br/></td></tr>
</table>

```html
<label>
  用户名：
  <input class="error" value="aa">
</label>
<span class="error">
  最少3个字符
</span>

<style>
  .error {
    color: red;
  }
  
  input.error {
    border-color: red;
  }
</style>
```

```html
<article>
  <h1>拉森火山国家公园</h1>
  <p>拉森火山国家公园是位于...</p>
  <section>
    <h2>气候</h2>
    <p>因为拉森火山国家公园...</p>
    <p>高于这个高度，气候非常寒冷...</p>
  </section>
</article>

<style>
  article p {
    color: black;
  }

  article > p {
    color: blue;
  }

  h2 + p {
    color: red; 
  }
</style>
```

#### 选择器组

```css
body, h1, h2, h3, h4, h5, h6, ul, ol, li {
    margin: 0;
    padding: 0;
}

[type="checkbox"], [type="radio"] {
    box-sizing: border-box;
    padding: 0;
}
```

### 颜色

#### 表示方式

- RGB

Example rgb(143, 172, 135) 或 #8fac87

缺点：不易表达

- HSL

![](static/Bf2obMGmaol6Ohx5pTNcJwWgnef.png)

Example：hsl(18, 66%, 55%)

- 关键字

![](static/RwNJbNXAto1REnxlKaccNlQMnjT.png)

#### alpha 透明度

Example:

新时代浏览器可能不需要 `a`

### 字体族 font-family

例如通常为

```css
h1 {
    /* 斜体 粗细 大小/行高 字体族 */
    font: bold 14px/1.7 Helvetica, sans-serif;
}
p {
    font: 14px serif;
}
```

字体族在遇到设备中不存在字体时会依次向下显示

```html
<h1>卡尔斯巴德洞窟（Carlsbad Caverns）</h1>
<p>卡尔斯巴德洞窟（Carlsbad Caverns）是美国的
一座国家公园，位于新墨西哥州东南部。游客可以通过天
然入口徒步进入，也可以通过电梯直接到达230米的洞穴
深处。</p>

<style>
  h1 {
    font-family: Optima, Georgia, serif;
  }
  body {
    font-family: Helvetica, sans-serif;
  }
</style>
```

一些通用字体族：

- Serif 衬线体：Georgia、宋体
- Sans-Serif 无衬线体：Arial、Helvetica、黑体、微软雅黑
- Cursive 手写体：Caflisch Script、楷体
- Fantasy：Comic Sans MS, Papyrus
- Monospace 等宽字体：Consolas，Courier、中文字体

> 如果字体都没有的话，会采用通用字体族
> 会先行渲染第一个字体有的字符，若没有依次向下渲染
> 建议：字体列表最后写上通用字体族
> 英文字体放在中文字体前面

#### 使用 Web-Font

```html
<h1>Web fonts are awesome!</h1>

<style>
  @font-face {
    font-family: "Megrim";
    src: url(https://fonts.gstatic.com/s/megrim/v11/46kulbz5WjvLqJZVam_hVUdI1w.woff2) format('woff2');
  }

  h1 {
    font-family: Megrim, Cursive;
  }
</style>
```

```html
<style>
  @font-face {
    font-family: f1;
    src: url("//s2.ssl.qhimg.com/static/ff00cb8151eeecd2.woff2") format("woff2");
  }

  @font-face {
    font-family: f2;
    src: url("//s3.ssl.qhimg.com/static/a59a90c9e8f21898.woff2") format("woff2");
  }

  @font-face {
    font-family: f3;
    src: url("//s2.ssl.qhimg.com/static/58324737c4cb53a5.woff2") format("woff2");
  }

  h1 {
    font-size: 50px;
  }
</style>

<h1 style="font-family: f1, serif">落霞与孤鹜齐飞，秋水共长天一色。</h1>
<h1 style="font-family: f2, serif">落霞与孤鹜齐飞，秋水共长天一色。</h1>
<h1 style="font-family: f3, serif">落霞与孤鹜齐飞，秋水共长天一色。</h1>
```

> 中文字体较大，建议先裁剪需要的字

#### 字体一些属性

- Font-size

  - 关键字： small、medium、large
  - 长度：px、em
  - 百分数：相对于父元素字体大小
  - -

    > 需要字体支持 font-weight
    >
- line-height
  -----------

### 选择器的特异度(Specificity)

![](static/NgtHbIes1oPqQFxzWJgcqHvmn2f.png)

越小越优先

Example：

```html
<button class="btn">普通按钮</button>
<button class="btn primary">主要按钮</button>
<style>
  .btn {
    display: inline-block;
    padding: .36em .8em;
    margin-right: .5em;
    line-height: 1.5;
    text-align: center;
    cursor: pointer;
    border-radius: .3em;
    border: none;
    background: #e6e6e6;
    color: #333;
  }
  .btn.primary {
    color: #fff;
    background: #218de6;
    /* 覆盖与继承 */
  }
</style>
```

### CSS 的继承

某些属性会自动继承其父元素的**计算值**，除非显式指定一个值

```html
<p>This is a <em>test</em> of <strong>inherit</strong></p>

<style>
  body {
    font-size: 20px;
  }
  p {
    color: blue;
  }
  em {
    color: red;
  }
</style>
```

显式继承

```css
* {
    box-sizing: inherit; /*默认不继承需要显式继承*/
}
html {
    box-sizing: border-box;
}
.some-widget {
    box-sizing: content-box;
}
```

### CSS 的初始值

- CSS 中，每个属性都有一个初始值

  - background-color 的初始值为 transparent
  - margin-left 的初始值为 0
- 可以使用 initial 关键字显式重置为初始值

  - background-color: initial

### CSS 求值过程

![](static/M9YhbT5FUoBxbrxo5Cvcd5jXnOg.png)
![](static/KwhNbv81po1qw7xOf7Ccrmrdn3e.png)
![](static/TH4nb7InNo5kvrxwlY7cFJD6nB4.png)

### 布局

![](static/Q69rbCeQmorsRRxIrw4cbP58ncd.png)

- 确定内容的大小和位置的算法
- 依据元素、容器、兄弟节点和内容等信息来计算

#### 布局相关技术

![](static/LNYxbnoKBoKk5Hx4AvtcufQVn6d.png)

盒模型

![](static/E8zOb5DpboDVdGx6dKUcIv5Vnhg.png)
![](static/PDSmbQRtqoQlq1xPy9lcaiaxn0g.png)

- width

  - 指定 content box 宽度
  - 取值为长度、百分数、auto
  - auto 由浏览器根据其它属性确定
  - 百分数相对于容器的 content box 宽度
- height

  - 指定 content box 高度
  - 取值为长度、百分数、auto
  - auto 取值由内容计算得来
  - 百分数相对于容器的 content box 高度
  - 容器有指定的高度时，百分数才生效
- padding

  - 指定元素四个方向的内边距
  - 百分数相对于容器宽度
- border

  - 指定容器边框样式、粗细和颜色
  - 三种属性：border-width border-style border-color
  - 四个方向：border-top boder-right border-bottom border-left
- margin

  - 指定元素四个方向的外边距
  - 取值可以是长度、百分数、auto
  - 百分数相对于容器宽度
  - 使用 margin: auto 水平居中

```html
<div></div>

<style>
  div {
    width: 200px;
    height: 200px;
    background: coral;
    margin-left: auto;
    margin-right: auto;
  }
  html {
  background: #333;
}
</style>
```

- margin collapse：当两个相邻元素的之间的边距只取 max（例，A 的下边距为 100， B 的上边距为 110，AB 上下边距为 110）
- box-sizing: border-box

![](static/Vn64bdy5dofna3xZlHycWyFMnhg.png)

- overflow 文本超出容器处理方式
  - Visible：可见
  - Hidden：隐藏
  - Scroll：可滚动

#### 块级 Versus 行级

CSS 中的概念

<table>
<tr>
<td>Block Level Box<br/></td><td>Inline Level Box<br/></td></tr>
<tr>
<td>不和其他盒子并列摆放<br/></td><td>和其他行级盒子一起放在一行或拆开成多行<br/></td></tr>
<tr>
<td>使用所有的盒模型属性<br/></td><td>盒模型中的width、height不可用<br/></td></tr>
</table>

HTML 中的概念

<table>
<tr>
<td>块级元素<br/></td><td>行级元素<br/></td></tr>
<tr>
<td>生成块级盒子<br/></td><td>- 生成行级盒子<br/>- 内容分散在多个行盒（Line Box）中<br/></td></tr>
<tr>
<td>body, article, div, main, section, h1-6, p, ul, li等<br/></td><td>span, em, strong, cite, code等<br/></td></tr>
<tr>
<td>display: block<br/></td><td>display: inline<br/></td></tr>
</table>

> display 属性
> block 块级盒子
> inline 行级盒子
> inline-block 本身是行级，可以放在行盒中;可以设置宽高;作为一个整体不会被拆散成多行
> none 排版时完全被忽略

#### 常规流 Normal Flow

- 根元素、浮动和绝对定位的元素会脱离常规流
- 其它元素都在常规流之内 (in-flow)
- 常规流中的盒子，在某种排版上下文中参与布局

##### 行级排版上下文

- Inline Formatting Context (IFC)
- **只包含行级盒子**的容器会创建一个 IFC
- IFC 内的排版规则

  - 盒子在一行内水平摆放
  - 一行放不下时，换行显示
  - text-align 决定一行内盒子的水平对齐
  - vertical-align 决定一个盒子在行内的垂直对齐
  - 避开浮动(float)元素*

##### 块级排版上下文

- Block Formatting Context (BFC)
- 某些容器会创建一个 BFC

  - 根元素
  - 浮动、绝对定位、inline-block
  - Flex 子项和 Grid 子项
  - overflow 值不是 visible 的块盒
  - display: flow-root;
- BFC 内的排版规则

  - 盒子从上到下摆放
  - 垂直 margin 合并
  - BFC 内盒子的 margin 不会与外面的含并
  - BFC 不会和浮动元素重叠

##### Flex Box

- 一种新的排版上下文
- 它可以控制子级盒子的:

  - 摆放的流向(↑↓←→)
  - 摆放顺序
  - 盒子宽度和高度
  - 水平和垂直方向的对齐
  - 是否允许折行
- flex-direction

![](static/M2xxbqQ0HoR3jOxP9uJccLA6nHJ.png)

- 主轴与侧轴

![](static/PmIEbTbQooRMB0xB20Jc2XPXn0g.png)

- justify-content

![](static/PjMDb3Ep2omvqixc8BNcuJYznxh.png)

- align-items

![](static/HrOIbnG3YoTJyExB5UJcptxGnGX.png)

- align-self

![](static/MT1rbLgiYoUrJCxn3gucdjFVn6g.png)

- order

![](static/X4QAbmay7oC105xWQ1Ncw1P5nLh.png)

- Flexibility

  - 可以设置子项的弹性: 当容器有剩余空间时，会伸展;容器空间不够时，会收缩。
  - flex-grow 有剩余空间时的伸展能力
  - flex-shrink 容器空间不足时收缩的能力
  - flex-basis 没有伸展或收缩时的基础长度
- flex-grow
- flex-shrink
- flex：缩写子属性

![](static/NRvibycmGokhnfxNehPcsQggnTf.png)

##### Grid 布局

![](static/WUptbGfb4oGuCkx6nBFcY6sJnWg.png)

- display:grid

  - display: grid 使元素生成一个块级的 Grid 容器
  - 使用 grid-template 相关属性将容器划分为网格
  - 设置每一个子项占哪些行/列
    ![](static/H1iQbFgFGoo6nJxz89ScjlnpnXe.png)
- grid line 网格线
  ![](static/PUjjbCV6corZvlxi1Kjc3TZLnEe.png)
- grid area 网格区域
  ![](static/IbEAbIhCWokIZixW6xTcuhu3nrb.png)

#### float

#### 绝对定位 position

- static：默认值，非定位元素
- relative：相对自身原本位置偏移，不脱离文档流

  - 在常规流里面布局
  - 相对于自己本应该在的位置进行偏移
  - 使用 top、left、bottom、right 设置偏移长度
  - 流内其它元素当它没有偏移一样布局

  > 好像紫色方块还存在一样
  >

![](static/JbcPbVr1Oo4BGExxUJfcWRqYnDf.png)

- absolute：绝对定位，相对非 static 祖先元素定位
  - 脱离常规流
  - 相对于**最近的非 static 祖先**定位
  - 不会对流内元素布局造成影响

![](static/RNCUbwXfaozBEzxvesDcbHXfnJd.png)

- fixed：相对于视口绝对定位

## Lesson 4 如何写好 JavaScript

### 各司其职

简单说就是

![](static/W1VnbrfcYojsMzxLShIcbPWXnZb.png)

**举例说明**：写一段 JS，控制一个网页，让它支持浅色和深色两种浏览模式

- Version One
  - Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>深夜食堂</title>
</head>
<body>
  <header>
    <button id="modeBtn">🌞</button>
    <h1>深夜食堂</h1>
  </header>
  <main>
    <div class="pic">
      <img src="https://p2.ssl.qhimg.com/t0120cc20854dc91c1e.jpg">
    </div>
    <div class="description">
      <p>
          这是一间营业时间从午夜十二点到早上七点的特殊食堂。这里的老板，不太爱说话，却总叫人吃得热泪盈
          眶。在这里，自卑的舞蹈演员偶遇隐退多年舞界前辈，前辈不惜讲述自己不堪回首的经历不断鼓舞年轻人，最终令其重拾自信；轻言绝交的闺蜜因为吃到共同喜爱的美食，回忆起从前的友谊，重归于好；乐观的绝症患者遇到同命相连的女孩，两人相爱并相互给予力量，陪伴彼此完美地走过了最后一程；一味追求事业成功的白领，在这里结交了真正暖心的朋友，发现真情比成功更有意义。食物、故事、真情，汇聚了整部剧的主题，教会人们坦然面对得失，对生活充满期许和热情。每一个故事背后都饱含深情，情节跌宕起伏，令人流连忘返 [6]  。
      </p>
    </div>
  </main>
</body>
</html>
```

```css
body, html {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  overflow: hidden;
}
body {
  padding: 10px;
  box-sizing: border-box;
}
div.pic img {
  width: 100%;
}
#modeBtn {
  font-size: 2rem;
  float: right;
  border: none;
  background: transparent;
}
```

```javascript
const btn = document.getElementById('modeBtn');
btn.addEventListener('click', (e) => {
  const body = document.body;
  if(e.target.innerHTML === '🌞') {
    body.style.backgroundColor = 'black';
    body.style.color = 'white';
    e.target.innerHTML = '🌜';
  } else {
    body.style.backgroundColor = 'white';
    body.style.color = 'black';
    e.target.innerHTML = '🌞';
  }
});
```

- 通过 Javascript 改变样式，不再是各司其职
- Version Two

  - Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>深夜食堂</title>
</head>
<body>
  <header>
    <button id="modeBtn"></button>
    <h1>深夜食堂</h1>
  </header>
  <main>
    <div class="pic">
      <img src="https://p2.ssl.qhimg.com/t0120cc20854dc91c1e.jpg">
    </div>
    <div class="description">
      <p>
          这是一间营业时间从午夜十二点到早上七点的特殊食堂。这里的老板，不太爱说话，却总叫人吃得热泪盈
          眶。在这里，自卑的舞蹈演员偶遇隐退多年舞界前辈，前辈不惜讲述自己不堪回首的经历不断鼓舞年轻人，最终令其重拾自信；轻言绝交的闺蜜因为吃到共同喜爱的美食，回忆起从前的友谊，重归于好；乐观的绝症患者遇到同命相连的女孩，两人相爱并相互给予力量，陪伴彼此完美地走过了最后一程；一味追求事业成功的白领，在这里结交了真正暖心的朋友，发现真情比成功更有意义。食物、故事、真情，汇聚了整部剧的主题，教会人们坦然面对得失，对生活充满期许和热情。每一个故事背后都饱含深情，情节跌宕起伏，令人流连忘返 [6]  。
      </p>
    </div>
  </main>
</body>
</html>
```

```css
body, html {
  width: 100%;
  height: 100%;
  max-width: 600px;
  padding: 0;
  margin: 0;
  overflow: hidden;
}
body {
  padding: 10px;
  box-sizing: border-box;
  transition: all 1s;
}
div.pic img {
  width: 100%;
}
#modeBtn {
  font-size: 2rem;
  float: right;
  border: none;
  outline: none;
  cursor: pointer;
  background: inherit;
}

body.night {
  background-color: black;
  color: white;
  transition: all 1s;
}

#modeBtn::after {
  content: '🌞';
}
body.night #modeBtn::after {
  content: '🌜';
}
```

```javascript
const btn = document.getElementById('modeBtn');
btn.addEventListener('click', (e) => {
  const body = document.body;
  if(body.className !== 'night') {
    body.className = 'night';
  } else {
    body.className = '';
  }
});
```

- 用 Javascript 控制元素类， 用类的样式来控制元素
- Version Three

  - Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>深夜食堂</title>
</head>
<body>
  <input id="modeCheckBox" type="checkbox">
  <div class="content">
    <header>
      <label id="modeBtn" for="modeCheckBox"></label>
      <h1>深夜食堂</h1>
    </header>
    <main>
      <div class="pic">
        <img src="https://p2.ssl.qhimg.com/t0120cc20854dc91c1e.jpg">
      </div>
      <div class="description">
        <p>
            这是一间营业时间从午夜十二点到早上七点的特殊食堂。这里的老板，不太爱说话，却总叫人吃得热泪盈
            眶。在这里，自卑的舞蹈演员偶遇隐退多年舞界前辈，前辈不惜讲述自己不堪回首的经历不断鼓舞年轻人，最终令其重拾自信；轻言绝交的闺蜜因为吃到共同喜爱的美食，回忆起从前的友谊，重归于好；乐观的绝症患者遇到同命相连的女孩，两人相爱并相互给予力量，陪伴彼此完美地走过了最后一程；一味追求事业成功的白领，在这里结交了真正暖心的朋友，发现真情比成功更有意义。食物、故事、真情，汇聚了整部剧的主题，教会人们坦然面对得失，对生活充满期许和热情。每一个故事背后都饱含深情，情节跌宕起伏，令人流连忘返 [6]  。
        </p>
      </div>
    </main>
  </div>
</body>
</html>
```

```css
body, html {
  width: 100%;
  height: 100%;
  max-width: 600px;
  padding: 0;
  margin: 0;
  overflow: hidden;
}

body {
  box-sizing: border-box;
}

.content {
  padding: 10px;
  transition: background-color 1s, color 1s;
}

div.pic img {
  width: 100%;
}

#modeCheckBox {
  display: none;
}

#modeCheckBox:checked + .content {
  background-color: black;
  color: white;
  transition: all 1s;
}

#modeBtn {
  font-size: 2rem;
  float: right;
}

#modeBtn::after {
  content: '🌞';
}

#modeCheckBox:checked + .content #modeBtn::after {
  content: '🌜';
}
```

- 无需 Javascript， 更加的各司其职，但不强求

由上面的例子得出的**结论**：

- HTML/CSS/JS 各司其职
- 应当避免不必要的由 JS 直接操作样式
- 可以用 class 来表示状态
- 纯展示类交互寻求零 JS 方案

### 组件封装

组件是指 Web 界面上抽出来一个个包含模板（HTML）、功能（JS）和样式（CSS）的单元。

好的组件具备**封装性、正确性、扩展性、复用性**。

**举例说明：**用原生 JS 写一个电商网站的轮播图

- 结构设计：HTML，轮播图是一个典型的列表结构，我们可以使用无序列表 `<ul>` 元素来实现
- 展示效果：CSS

  - 使用 CSS 绝对定位将图片重叠在同一个位置
  - 轮播图切换的状态使用修饰符(modifier)
  - 轮播图的切换动画使用 CSS transition
- 行为设计：API

  - API 设计应保证原子操作，职责单一，满足灵活性。
  - getSelectedItem()
  - getSelectedItemIndex()
  - slideTo()
  - slideNext()
  - slidePrevious()
- 行为设计：控制流

  - 使用自定义事件来解耦
- 代码实现：

  - Version One： API 的简单实现

```html
<div id="my-slider" class="slider-list">
  <ul>
    <li class="slider-list__item--selected">
      <img src="https://p5.ssl.qhimg.com/t0119c74624763dd070.png"/>
    </li>
    <li class="slider-list__item">
      <img src="https://p4.ssl.qhimg.com/t01adbe3351db853eb3.jpg"/>
    </li>
    <li class="slider-list__item">
      <img src="https://p2.ssl.qhimg.com/t01645cd5ba0c3b60cb.jpg"/>
    </li>
    <li class="slider-list__item">
      <img src="https://p4.ssl.qhimg.com/t01331ac159b58f5478.jpg"/>
    </li>
  </ul>
</div>
```

```css
#my-slider{
  position: relative;
  width: 790px;
}

.slider-list ul{
  list-style-type:none;
  position: relative;
  padding: 0;
  margin: 0;
}

.slider-list__item,
.slider-list__item--selected{
  position: absolute;
  transition: opacity 1s;
  opacity: 0;
  text-align: center;
}

.slider-list__item--selected{
  transition: opacity 1s;
  opacity: 1;
}
```

```javascript
class Slider{
  constructor(id){
    this.container = document.getElementById(id);
    this.items = this.container
    .querySelectorAll('.slider-list__item, .slider-list__item--selected');
  }
  getSelectedItem(){
    const selected = this.container
      .querySelector('.slider-list__item--selected');
    return selected
  }
  getSelectedItemIndex(){
    return Array.from(this.items).indexOf(this.getSelectedItem());
  }
  slideTo(idx){
    const selected = this.getSelectedItem();
    if(selected){ 
      selected.className = 'slider-list__item';
    }
    const item = this.items[idx];
    if(item){
      item.className = 'slider-list__item--selected';
    }
  }
  slideNext(){
    const currentIdx = this.getSelectedItemIndex();
    const nextIdx = (currentIdx + 1) % this.items.length;
    this.slideTo(nextIdx);
  }
  slidePrevious(){
    const currentIdx = this.getSelectedItemIndex();
    const previousIdx = (this.items.length + currentIdx - 1)
      % this.items.length;
    this.slideTo(previousIdx);  
  }
}

const slider = new Slider('my-slider');
slider.slideTo(3);
```

- Version Two：控制流

```html
<div id="my-slider" class="slider-list">
  <ul>
    <li class="slider-list__item--selected">
      <img src="https://p5.ssl.qhimg.com/t0119c74624763dd070.png"/>
    </li>
    <li class="slider-list__item">
      <img src="https://p4.ssl.qhimg.com/t01adbe3351db853eb3.jpg"/>
    </li>
    <li class="slider-list__item">
      <img src="https://p2.ssl.qhimg.com/t01645cd5ba0c3b60cb.jpg"/>
    </li>
    <li class="slider-list__item">
      <img src="https://p4.ssl.qhimg.com/t01331ac159b58f5478.jpg"/>
    </li>
  </ul>
  <a class="slide-list__next"></a>
  <a class="slide-list__previous"></a>
  <div class="slide-list__control">
    <span class="slide-list__control-buttons--selected"></span>
    <span class="slide-list__control-buttons"></span>
    <span class="slide-list__control-buttons"></span>
    <span class="slide-list__control-buttons"></span>
  </div>
</div>
```

```css
#my-slider{
  position: relative;
  width: 790px;
  height: 340px;
}

.slider-list ul{
  list-style-type:none;
  position: relative;
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}

.slider-list__item,
.slider-list__item--selected{
  position: absolute;
  transition: opacity 1s;
  opacity: 0;
  text-align: center;
}

.slider-list__item--selected{
  transition: opacity 1s;
  opacity: 1;
}

.slide-list__control{
  position: relative;
  display: table;
  background-color: rgba(255, 255, 255, 0.5);
  padding: 5px;
  border-radius: 12px;
  bottom: 30px;
  margin: auto;
}

.slide-list__next,
.slide-list__previous{
  display: inline-block;
  position: absolute;
  top: 50%;
  margin-top: -25px;
  width: 30px;
  height:50px;
  text-align: center;
  font-size: 24px;
  line-height: 50px;
  overflow: hidden;
  border: none;
  background: transparent;
  color: white;
  background: rgba(0,0,0,0.2);
  cursor: pointer;
  opacity: 0;
  transition: opacity .5s;
}

.slide-list__previous {
  left: 0;
}

.slide-list__next {
  right: 0;
}

#my-slider:hover .slide-list__previous {
  opacity: 1;
}


#my-slider:hover .slide-list__next {
  opacity: 1;
}

.slide-list__previous:after {
  content: '<';
}

.slide-list__next:after {
  content: '>';
}

.slide-list__control-buttons,
.slide-list__control-buttons--selected{
  display: inline-block;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  margin: 0 5px;
  background-color: white;
  cursor: pointer;
}

.slide-list__control-buttons--selected {
  background-color: red;
}
```

```javascript
class Slider{
  constructor(id, cycle = 3000){
    this.container = document.getElementById(id);
    this.items = this.container.querySelectorAll('.slider-list__item, .slider-list__item--selected');
    this.cycle = cycle;

    const controller = this.container.querySelector('.slide-list__control');
    if(controller){
      const buttons = controller.querySelectorAll('.slide-list__control-buttons, .slide-list__control-buttons--selected');

      controller.addEventListener('mouseover', evt=>{
        const idx = Array.from(buttons).indexOf(evt.target);
        if (idx >= 0) {
          this.slideTo(idx);
          this.stop();
        } 
      });

      controller.addEventListener('mouseout', evt=>{
        this.start();
      });

      this.container.addEventListener('slide', evt=>{
        const idx = evt.detail.index;
        const selected = controller.querySelector('.slide-list__control-buttons--selected');
        if(selected) selected.className = 'slide-list__control-buttons';
        buttons[idx].className = 'slide-list__control-buttons--selected';
      });

      const previous = this.container.querySelector('.slide-list__previous');
      if (previous){
        previous.addEventListener('click', evt=>{
          this.stop();
          this.slidePrevious();
          this.start();
          evt.preventDefault()
        });
      }
    }
    
    const next = this.container.querySelector('.slide-list__next');
    if (next){
      next.addEventListener('click', evt => {
        this.stop();
        this.slideNext();
        this.start();
        evt.preventDefault();
      });
    }

  }

  getSelectedItem(){
    const selected = this.container.querySelector('.slider-list__item--selected');
    return selected
  }

  getSelectedItemIndex(){
    return Array.from(this.items).indexOf(this.getSelectedItem());
  }

  slideTo(idx) {
    const selected = this.getSelectedItem();
    if (selected) selected.className = 'slider-list__item';
    const item = this.items[idx];
    if (item) item.className = 'slider-list__item--selected';

    const detail = {index: idx};
    const event = new CustomEvent('slide', {bubbles: true, detail});
    this.container.dispatchEvent(event);
  }

  slideNext(){
    const currentIdx = this.getSelectedItemIndex();
    const nextIdx = (currentIdx + 1) % this.items.length;
    this.slideTo(nextIdx);
  }

  slidePrevious(){
    const currentIdx = this.getSelectedItemIndex();
    const previousIdx = (currentIdx - 1 + this.items.length) % this.items.length;
    this.slideTo(previousIdx);
  }

  start(){
    this.stop();
    // 这里使用了箭头函数（()=>{}），箭头函数中的this绑定到它被创建的上下文，通常是定义它的对象，这里的this将绑定到当前对象上。所以，每当setInterval触发时，将会调用this.slideNext()方法。
    this._timer = setInterval(()=>this.slideNext(), this.cycle);

    // 这里直接调用了this.slideNext()方法，并且将其返回值传递给setInterval。由于setInterval需要一个函数作为第一个参数，而不是函数调用的结果，这个语句并不会按预期工作。实际上，这会立即调用this.slideNext()方法，并将返回值（如果有的话）传递给setInterval，而不是在定时间隔触发时调用该方法。
    // 正确的写法是第一条语句，使用箭头函数确保在定时间隔内调用this.slideNext()方法，而不是在创建定时器时就立即调用它。
    // this._timer = setInterval(this.slideNext(), this.cycle);
  }
  stop(){
    clearInterval(this._timer);
  }

}

const slider = new Slider('my-slider');
slider.start();
```

> `=>` 是箭头函数（Arrow Function）的语法。它是 ES6（ECMAScript 2015）中引入的一种新的函数定义方式，用于简化函数的声明和编写。
> 箭头函数有两种形式：
>
> 1. 单参数、单语句的箭头函数：
>
> ```scss
> ```

scssCopy code
(param) => statement;

```
> 1. 多参数、多语句的箭头函数：
> ```scss
scssCopy code
(param1, param2, ...) => {
  // multiple statements
};
```

> 箭头函数相比传统函数表达式具有以下特点：
>
> 1. 简洁：由于语法简洁，通常在只有一个参数和单个表达式的情况下使用，可以让代码更加紧凑。
> 2. 没有 `this` 绑定：箭头函数没有自己的 `this` 绑定，而是继承外部作用域的 `this`。这在一定程度上解决了传统函数中 `this` 作用域问题。
> 3. 没有 `arguments` 对象：箭头函数也没有自己的 `arguments` 对象，而是继承外部函数的 `arguments` 对象。
>    箭头函数的使用场景包括但不限于：
>
> - 简化回调函数的定义。
> - 作为简单函数的快捷方式。
> - 在需要保留外部作用域的 `this` 时使用，避免 `this` 指向出现问题。
>   需要注意的是，由于箭头函数没有自己的 `this` 和 `arguments` 对象，所以在一些情况下，传统函数可能更适合，特别是需要动态绑定 `this` 或访问 `arguments` 对象时。

### 过程抽象

- 用来处理局部细节控制的一些方法
- 函数式编程思想的基础应用

**高阶函数**

Once

- 操作次数限制
  - 一些异步交互
  - 一次性的 HTTP 请求
    为了能够让“只执行一次”的需求覆盖不同的事件处理，我们可以将这个需求剥离处理，这个过程称为**过程抽象**。
    像这样的函数也称为**高阶函数**。
    高阶函数
    常用的高阶函数有：
    ![](static/W9V0bWLcjoOsrRxXodOcQU2hnCb.png)

![](static/B2XdbkpvMoTg6BxF7h3cdTKWnDf.png)
![](static/YlUcb5hN8o1cICxN3bCcpM3Gnld.png)

```javascript
// 让 fn 函数只能执行一次
function once(fn) {
    return function (...args) {
        if (fn) {
            const ret = fn.apply(this, args)
            fn = null
            return ret;
        }
    };
}

// 让 fn 函数在 time 内只能执行一次
function throttle(fn, time = 500) {
    let timer;
    return function (...args) {
        if (timer == null) {
            fn.apply(this, args);
            timer = setTimeout(() => {
                timer = null;
            }, time)
        }
    }
}

// 当持续触发事件时，一定时间段内没有再触发事件，事件处理函数才会执行一次；如果设定的时间到来之前，又一次触发了事件，就重新开始延时。
function debounce(fn, dur) {
    dur = dur || 100;
    var timer;
    return function () {
        clearTimeout(timer);
        timer = setTimeout(() => {
            fn.apply(this, arguments);
        }, dur);
    }
}

// 每隔 time 时间调用 fn, 实现一个 delay 调用
function consumer(fn, time) {
    let tasks = [],
        timer;

    return function (...args) {
        tasks.push(fn.bind(this, ...args));
        if (timer == null) {
            timer = setInterval(() => {
                tasks.shift().call(this)
                if (tasks.length <= 0) {
                    clearInterval(timer);
                    timer = null;
                }
            }, time)
        }
    }
}

// 对可迭代对象批量操作
const isIterable = obj => obj != null && typeof obj[Symbol.iterator] === 'function';
function iterative(fn) {
    return function (subject, ...rest) {
        if (isIterable(subject)) {
            const ret = [];
            for (let obj of subject) {
                ret.push(fn.apply(this, [obj, ...rest]));
            }
            return ret;
        }
        return fn.apply(this, [subject, ...rest]);
    }
}
```

throttle Example

```html
每500毫秒可记录一次

<button id="btn">点我</button>

<div id="circle">0</div>
```

```css
#circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: red;
  line-height: 50px;
  text-align: center;
  color: white;
  opacity: 1.0;
  transition: opacity .25s;
}

#circle.fade {
  opacity: 0.0;
  transition: opacity .25s;
}
```

```javascript
function throttle(fn, time = 500){
  let timer;
  return function(...args){
    if(timer == null){
      fn.apply(this,  args);
      timer = setTimeout(() => {
        timer = null;
      }, time)
    }
  }
}

btn.onclick = throttle(function(e){
  circle.innerHTML = parseInt(circle.innerHTML) + 1;
  circle.className = 'fade';
  setTimeout(() => circle.className = '', 250);
});
```

Debounce Example:

```html
<script src="https://s1.qhres2.com/!bd39e7fb/animator-0.2.0.min.js"></script>
<div id="bird" class="sprite bird1"></div>
```

```css
html, body {
  margin:0;
  padding:0;
}

.sprite {
  display:inline-block; overflow:hidden; 
  background-repeat: no-repeat;
  background-image:url(https://p1.ssl.qhimg.com/d/inn/0f86ff2a/8PQEganHkhynPxk-CUyDcJEk.png);
}

.bird0 {width:86px; height:60px; background-position: -178px -2px}
.bird1 {width:86px; height:60px; background-position: -90px -2px}
.bird2 {width:86px; height:60px; background-position: -2px -2px}

#bird{
  position: absolute;
  left: 100px;
  top: 100px;
  transform: scale(0.5);
  transform-origin: -50% -50%;
}
```

```javascript
var i = 0;
setInterval(function(){
  bird.className = "sprite " + 'bird' + ((i++) % 3);
}, 1000/10);

function debounce(fn, dur){
  dur = dur || 100;
  var timer;
  return function(){
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, arguments);
    }, dur);
  }
}

document.addEventListener('mousemove', debounce(function(evt){
  var x = evt.clientX,
      y = evt.clientY,
      x0 = bird.offsetLeft,
      y0 = bird.offsetTop;
  
  console.log(x, y);
  
  var a1 = new Animator(1000, function(ep){
    bird.style.top = y0 + ep * (y - y0) + 'px';
    bird.style.left = x0 + ep * (x - x0) + 'px';
  }, p => p * p);
  
  a1.animate();
}, 100));
```

Consumer Example:

```html
<div id="main">
  <button id="btn">Hit</button>
  <span id="count">+0</span>
</div>
```

```css
#main {
  padding-top: 20px;
  font-size: 26px;
}

#btn {
  font-size: 30px;
  border-radius: 15px;
  border: solid 3px #fa0;
}

#count {
  position: absolute;
  margin-left: 6px;
  opacity: 1.0;
  transform: translate(0, 10px);
}

#count.hit {
  opacity: 0.1;
  transform: translate(0, -20px);
  transition: all .5s;
}
```

```javascript
function consumer(fn, time){
  let tasks = [],
      timer;
  
  return function(...args){
    tasks.push(fn.bind(this, ...args));
    if(timer == null){
      timer = setInterval(() => {
        tasks.shift().call(this)
        if(tasks.length <= 0){
          clearInterval(timer);
          timer = null;
        }
      }, time)
    }
  }
}

btn.onclick = consumer((evt)=>{
  let t = parseInt(count.innerHTML.slice(1)) + 1;
  count.innerHTML = `+${t}`;
  count.className = 'hit';
  let r = t * 7 % 256,
      g = t * 17 % 128,
      b = t * 31 % 128;
  
  count.style.color = `rgb(${r},${g},${b})`.trim();
  setTimeout(()=>{
    count.className = 'hide';
  }, 500);
}, 800)
```

Iterative Example:

```html
<ul>
  <li>a</li>
  <li>b</li>
  <li>c</li>
  <li>d</li>
  <li>e</li>
  <li>f</li>
  <li>g</li>
</ul>
```

```javascript
const isIterable = obj => obj != null 
  && typeof obj[Symbol.iterator] === 'function';

function iterative(fn) {
  return function(subject, ...rest) {
    if(isIterable(subject)) {
      const ret = [];
      for(let obj of subject) {
        ret.push(fn.apply(this, [obj, ...rest]));
      }
      return ret;
    }
    return fn.apply(this, [subject, ...rest]);
  }
}

const setColor = iterative((el, color) => {
  el.style.color = color;
});

const els = document.querySelectorAll('li:nth-child(2n+1)');
setColor(els, 'red');
```

### 编程范式

此处为命令式与声明式，命令式强调 `How to do` 而声明式强调 `What to do`，所以命令式不可避免的比声明式复杂。

![](static/AETybVaYco76nJx0LW4cZT7Qnfg.png)
![](static/FUirbrrRsohVIMxCKJrcKSpJnkm.png)

![](static/KW2XbjTmNo2NpRxxwn0cIauAnVE.png)
![](static/L5vzbdma6oyECVxa4kvceXtCnJg.png)

**Toggle Example：**

```html
<div id="switcher" class="on"></div>
```

```css
#switcher {
  display: inline-block;
  background-color: black;
  width: 50px;
  height: 50px;
  line-height: 50px;
  border-radius: 50%;
  text-align: center;
  cursor: pointer;
}

#switcher.on {
  background-color: green;
}

#switcher.off {
  background-color: red;
}

#switcher.on:after {
  content: 'on';
  color: white;
}

#switcher.off:after {
  content: 'off';
  color: white;
}
```

- 命令式

```javascript
switcher.onclick = function(evt){
  if(evt.target.className === 'on'){
    evt.target.className = 'off';
  }else{
    evt.target.className = 'on';
  }
}
```

- 声明式

```javascript
function toggle(...actions){
  return function(...args){
    let action = actions.shift();
    actions.push(action);
    return action.apply(this, args);
  }
}

switcher.onclick = toggle(
  evt => evt.target.className = 'off',
  evt => evt.target.className = 'on'
);
```

> 虽然看起来声明式的代码更加长，但是声明式的代码更容易维护

例如，为 Toggle 添加一个状态

```css
#switcher {
  display: inline-block;
  background-color: black;
  width: 50px;
  height: 50px;
  line-height: 50px;
  border-radius: 50%;
  text-align: center;
  cursor: pointer;
}

#switcher.on {
  background-color: green;
}

#switcher.warn {
  background-color: yellow;
}

#switcher.off {
  background-color: red;
}

#switcher.on:after {
  content: 'on';
  color: white;
}

#switcher.warn:after {
  content: 'warn';
  color: black;
}

#switcher.off:after {
  content: 'off';
  color: white;
}
```

声明式只需添加一行

```javascript
function toggle(...actions){
  return function(...args){
    let action = actions.shift();
    actions.push(action);
    return action.apply(this, args);
  }
}

switcher.onclick = toggle(
  evt => evt.target.className = 'warn',
  evt => evt.target.className = 'off',
  evt => evt.target.className = 'on'
);
```

而命令式需要 else if 的逻辑判断

## Lesson 5 深入浅出 TypeScript

## Lesson 6 Web 标准与前端开发

## Lesson 7 HTTP 实用指南

VideoLink:

1. [初识 HTTP 协议 - 掘金](https://juejin.cn/course/bytetech/7169405808147431455/section/7169430296574558216)
2. [HTTP 协议的应用场景分析 - 掘金](https://juejin.cn/course/bytetech/7169405808147431455/section/7169464204594937893)
3. [HTTP 协议实战分析 - 掘金](https://juejin.cn/course/bytetech/7169405808147431455/section/7168791819554127908)

[HTTP 实用指南.pptx](https://bytedance.feishu.cn/file/boxcnUFzZ8jMkS9P3735PsXjINk)

### 初识 HTTP

![](static/ULVCbGJCeoKG4bxDCVtclsxknmh.png)
![](static/NvJjbuHekoIVb3xaWXjcH8FSnXg.png)

- Hyper Text Transfer Protocol 超文本传输协议
- 应用层协议，基于 TCP 协议
- 请求响应
- 简单可扩展：对于 C/S，可以添加双方约定的 Key-Value
- 无状态：没有记忆能力，每个请求都是独立的

![](static/T6S9bfHF0ooWfjxAimIcIdzPntL.png)
![](static/DkucbgvjhoDlQkxbGDXcA3ZYn3b.png)
![](static/QhXhbRF2Ooe1oLxntamc5xFGnDd.png)

### 协议分析

#### HTTP 协议的发展

![](static/Nd6ObUCEpojGqcxrwwHcDpSRnJg.png)

#### HTTP 协议报文

以 HTTP/1.1 为例

![](static/UcpCb3aWnoJWisxkQy5ccMjbn9e.png)

##### Method

<table>
<tr>
<td>GET<br/></td><td>请求一个指定资源的表示形式.使用GET的请求应该只被用于获取数据<br/></td></tr>
<tr>
<td>POST<br/></td><td>用于将实体提交到指定的资源，通常导致在服务器上的状态变化或副作用<br/></td></tr>
<tr>
<td>PUT<br/></td><td>用请求有效载荷替换目标资源的所有当前表示<br/></td></tr>
<tr>
<td>DELETE<br/></td><td>删除指定的资源<br/></td></tr>
<tr>
<td>HEAD<br/></td><td>请求一个与GET请求的响应相同的响应，但没有响应体<br/></td></tr>
<tr>
<td>CONNECT<br/></td><td>建立一个到由目标资源标识的服务器的隧道<br/></td></tr>
<tr>
<td>OPTIONS<br/></td><td>用于描述目标资源的通信选项<br/></td></tr>
<tr>
<td>TRACE<br/></td><td>沿着到目标资源的路径执行一个消息环回测试<br/></td></tr>
<tr>
<td>PATCH<br/></td><td>用于对资源应用部分修改<br/></td></tr>
</table>

Safe (安全的) : 不会修改服务器的数据的方法。

ldempotent （幂等）:同样的请求被执行一次与连续执行多次的效果是一样的，服务器的状态也是一样的。

##### 状态码

![](static/GSgQb98hNo63fmxTKuJcSyX5n7b.png)

- 200 0K- 客户端请求成功
- 301- 资源 (网页等) 被永久转移到其它 URL
- 302-临时跳转
- 401 Unauthorized - 请求未经授权
- 404- 请求资源不存在，可能是输入了错误的 URL
- 500-服务器内部发生了不可预期的错误
- 504 Gateway Timeout-网关或者代理的服务器无法在规定的时间内获得想要的响应

##### RESTful API

一种 API 设计风格。REST - Representational State Transfer

- 每一个 URI 代表一种资源:
- 客户端和服务器之间，传递这种资源的某种表现层
- 客户端通过 HTTP method，对服务器端资源进行操作，实现“表现层状态转化”

<table>
<tr>
<td>请求<br/></td><td>返回码<br/></td><td>含义<br/></td></tr>
<tr>
<td>GET /zoos<br/></td><td>200 OK<br/></td><td>列出所有动物园，服务器成功返回了<br/></td></tr>
<tr>
<td>POST /zoos<br/></td><td>201 CREATED<br/></td><td>新建一个动物园，服务器创建成功<br/>更新某个指定动物园的信息 (提供该动<br/></td></tr>
<tr>
<td>PUT /zoos/ID<br/></td><td>400 INVALID REQUEST<br/></td><td>更新某个指定动物园的信息 (提供该动物园的全部信息)用户发出的请求有错误，服务器没有进行新建或修改数据的操作<br/></td></tr>
<tr>
<td>DELETE /zoos/ID<br/></td><td>204 NO CONTENT<br/></td><td>删除某个动物园，删除数据成功<br/></td></tr>
</table>

##### 常用请求头

<table>
<tr>
<td>Accept<br/></td><td>接收类型，表示浏览器支持的MIME类型 (对标服务端返回的Content-Type）<br/></td></tr>
<tr>
<td>Content-Type<br/></td><td>客户端发送出去实体内容的类型<br/></td></tr>
<tr>
<td>Cache-Control<br/></td><td>指定请求和响应遵循的缓存机制，如nocache<br/></td></tr>
<tr>
<td>If-Modified-Since<br/></td><td>对应服务端的Last-Modified，用来匹配看文件是否变动，只能精确到1s之内<br/></td></tr>
<tr>
<td>Expires<br/></td><td>缓存控制，在这个时间内不会请求，直接使用缓存，服务端时间<br/></td></tr>
<tr>
<td>Max-age<br/></td><td>代表资源在本地缓存多少秒，有效时间内不会请求，而是使用缓存<br/></td></tr>
<tr>
<td>If-None-Match<br/></td><td>对应服务端的ETag，用来匹配文件内容是否改变 (非常精确)<br/></td></tr>
<tr>
<td>Cookie<br/></td><td>有cookie并且同域访问时会自动带上<br/></td></tr>
<tr>
<td>Referer<br/></td><td>该页面的来源URL(适用于所有类型的请求，会精确到详细页面地址，csrf拦截常用到这个字段)<br/></td></tr>
<tr>
<td>Origin<br/></td><td>最初的请求是从哪里发起的 (只会精确到端口),Origin比Referer更尊重隐私<br/></td></tr>
<tr>
<td>User-Agent<br/></td><td>用户客户端的一些必要信息，如UA头部等<br/></td></tr>
</table>

##### 常用响应头

<table>
<tr>
<td>Content-Type<br/></td><td>服务端返回的实体内容的类型<br/></td></tr>
<tr>
<td>Cache-Control<br/></td><td>指定请求和响应遵循的缓存机制，如no-cache<br/></td></tr>
<tr>
<td>Last-Modified<br/></td><td>请求资源的最后修改时间<br/></td></tr>
<tr>
<td>Expires<br/></td><td>应该在什么时候认为文档已经过期,从而不再缓存它<br/></td></tr>
<tr>
<td>Max-age<br/></td><td>客户端的本地资源应该缓存多少秒，开启了Cache-Control后有效<br/></td></tr>
<tr>
<td>ETag<br/></td><td>资源的特定版本的标识符，Etags类似于指纹<br/></td></tr>
<tr>
<td>Set-Cookie<br/></td><td>设置和页面关联的cookie，服务器通过这个头部把cookie传给客户端<br/></td></tr>
<tr>
<td>Server<br/></td><td>服务器的一些相关信息<br/></td></tr>
<tr>
<td>Access-Control-Allow-Origin<br/></td><td>服务器端允许的请求Origin头部 (警如为*)<br/></td></tr>
</table>

##### 缓存

- 强缓存

  - Expires 时间戳
  - Cache-Control（可能不全面）
    - 可缓存性
      - no-cache：协商缓存验证
      - no-store：不使用任何缓存
    - 到期
      - max-age：单位是秒，存储的最大周期，相对于请求的时间
    - 重新验证 重新加载
      - must-revalidate：一旦资源过期，在成功向原始服务器验证之前，不能使用
- 协商缓存

  - Etag/If-None-Match：资源的特定版本的标识符，类似于指纹
  - Last-Modified/If-Modified-Since：最后修改时间

![](static/PyzjbiuLwoFAubxihVOcGgeYnId.png)

##### Cookie

set-Cookie --Response

<table>
<tr>
<td>Name=Value<br/></td><td>各种 Cookie 的名称和值<br/></td></tr>
<tr>
<td>Expires=Date<br/></td><td>Cookie 的有效期，缺省时Cookie 仅在浏览器关闭之前有效。<br/></td></tr>
<tr>
<td>Path=Path<br/></td><td>限制指定Cookie 的发送范围的文件目录，默认为当前<br/></td></tr>
<tr>
<td>Domain=Domain<br/></td><td>限制cookie生效的域名，默认为创建cookie的服务域名<br/></td></tr>
<tr>
<td>secure<br/></td><td>仅在HTTPS 安全连接时，才可以发送Cookie<br/></td></tr>
<tr>
<td>HttpOnly<br/></td><td>JavaScript 脚本无法获得Cookie<br/></td></tr>
<tr>
<td>SameSite=[None | Strict | Lax]<br/></td><td>- None 同站、跨站请求都可发送<br/>- Strict 仅在同站发送<br/>- 允许与顶级导航一起发送，并将与第三方网站发起的GET请求一起发送<br/></td></tr>
</table>

##### HTTP/2 概述

- 更快，更稳定，更简单
- **帧 (frame) **: HTTP/2 通信的最小单位每个帧都包含帧头，至少也会标识出当前帧所属的数据流。
  ![](static/MU31bmqjGoldPoxc7zFchk6hnRh.png)
- **消息**：与逻辑请求或响应消息对应的完整的一系列帧。
- **数据流**：已建立的连接内的双向字节流可以承载一条或多条消息。
  ![](static/EV1Pb0PIsoOxTQxlMm3cbxzRn1c.png)
  交错发送，接收方重组织
- HTTP/2 连接都是永久的，而且仅需要每个来源一个连接
- **流控制**：阻止发送方向接收方发送大量数据的机制
- **服务器推送**：在客户端请求时，附带推送给客户端一些文件（应用较少）
  ![](static/TbQfb4Y7Jo3NMsxcnQIcyXGpnnh.png)

##### HTTPS 概述

- HTTPS: Hypertext Transfer Protocol Secure
- 经过 TSL/SSL 加密
- 对称加密: 加密和解密都是使用同一个密钥
- 非对称加密，加密和解密需要使用两个不同的密钥: 公钥 (public key)和私钥 (private key)
  ![](static/LYcub2zqzokN1nxHxwQcQRDWnQf.png)

![](static/Cnnubg1bboMf8OxiG2Rcddjfnpe.png)
![](static/QGRzbrMo5oq0VIxshNJctFq2nqK.png)

### 场景分析

#### 静态资源

![](static/FbrybG7C6oPshkxDZIZczhLsnsb.png)
状态码 200 不一定是发送了请求，如图是从磁盘缓存
![](static/Mx3yb3UxFolGcWx02Wkc46JYn3e.png)
![](static/N7JAbo568oXub9xwm2Ic9szGngb.png)
![](static/FdCUb76pVoRgdnx7sXRcIAuenNg.png)
![](static/KKLrbG2H3ojse5x4tsXclM0jn6f.png)
可以得到一些信息

- 强缓存
- Cache-Control：1Year
- 运行所有域名访问
- 资源类型：CSS

静态资源方案：缓存 + CDN + 文件名 Hash

- CDN：Content Delivery Network
- 通过用户就近性和服务器负载的判断，CDN 确保内容以一种极为高效的方式为用户的请求提供服务
  ![](static/W2GlbVXUnoWpbxxdceycigwunee.png)

#### 登录

##### 域 Origin

![](static/RaLlbsQhboWtewx18vVcXlrInJg.png)

##### 跨域

- CORS（Cross-Origin Resource Sharing）
- 预请求: 获知服务端是否允许该跨源请求 (复杂请求)
- 相关协议头

  - Access-Control-Allow-Origin
  - Access-Control-Expose-Headers
  - Access-Control-Max-Age
  - Access-Control-Allow-Credentials
  - Access-Control-Allow-Methods
  - Access-Control-Allow-Headers
  - Access-Control-Request-Method
  - Access-Control-Request-Headers
  - Origin
    ![](static/IivebCuTroTPGpxedUScRwc7nbc.png)
    Preflight request：向服务器发送 Option 请求这种请求是否可以跨到某域
    Main request：发送真正的请求
- 跨域解决方案

  - CORS
  - 代理服务器：同源策略是浏览器的安全策略，不是 HTTP 的
  - Iframe：诸多不便
- 鉴权

  - Session + Cookie
  - JWT（JSON Web Token）

![](static/S9jbbOl3Jof9Xtxj7iFcAMdpnAg.png)
![](static/Ldk7bRft5ohcPKxQamacdTiBnjc.png)

> 适合使用 jwt 的场景：

1. 有效期短
2. 只希望被使用一次
   比如，用户注册后发一封邮件让其激活账户，通常邮件中需要有一个链接，这个链接需要具备以下的特性：能够标识用户，该链接具有时效性（通常只允许几小时之内激活），不能被篡改以激活其他可能的账户，一次性的。这种场景就适合使用 jwt。
   而由于 jwt 具有一次性的特性。单点登录和会话管理非常不适合用 jwt，如果在服务端部署额外的逻辑存储 jwt 的状态，那还不如使用 session。基于 session 有很多成熟的框架可以开箱即用，但是用 jwt 还要自己实现逻辑。

- SSO：单点登录（Single Sign On）

![](static/UNNKbsaYxoCCb9x2j1jcWqxTnHf.png)

### 实战

#### 浏览器端

##### AJAX 之 XHR

- XHR：XMLHttpRequest
- readyState

<table>
<tr>
<td>0<br/></td><td>UNSENT<br/></td><td>代理被创建，但尚未调用open() 方法。<br/></td></tr>
<tr>
<td>1<br/></td><td>OPENED<br/></td><td>open() 方法已经被调用。<br/></td></tr>
<tr>
<td>2<br/></td><td>HEADERS RECEIVED<br/></td><td>send() 方法已经被调用并且头部和状态已经可获得<br/></td></tr>
<tr>
<td>3<br/></td><td>LOADING<br/></td><td>下载中; responseText 属性已经包含部分数据<br/></td></tr>
<tr>
<td>4<br/></td><td>DONE<br/></td><td>下载操作已完成。<br/></td></tr>
</table>
![](static/Sq60bzlFlou708xLcXuculYYnBf.png)

##### AJAX 之 Fetch

- XMLHttpRequet 的升级版
- 使用 Promise
- 模块化设计，Response、Request、Header 对象
- 通过数据流处理对象，支持分块读取
  ![](static/JUcgbvAxmooGKSx8FlSc4ll0nr1.png)

#### Node 端

标准库 HTTP/HTTPS

- 默认模块，无需安装其他依赖
- 功能有限/不是十分友好
  ![](static/L9adbJAVaoR6TFx2lmPco9kcndh.png)

常用请求库：axios

- 支持浏览器、nodejs 环境
- 丰富的拦截器
  ![](static/Kc19bzU5wotWIrxYkuocyPCNnPb.png)

#### 用户体验——网络优化

![](static/UR37b0TBqoQUB0xzRaCcv6fNnCf.png)

- CDN 是否开启 H2 的性能对比 [HTTP/2 - A Real-World Performance Test and Analysis | CSS-Tricks](https://css-tricks.com/http2-real-world-performance-test-analysis/)
  ![](static/OkiybnQVAoFRWQxsULUcRhNnn8f.png)
- 预解析、预连接
  ![](static/T4JkbIb48oq62zxOWZIcdr2yn7c.png)

![](static/XXGCb7nIJobPpnxidZjctyE4neG.png)

- 重试是保证稳定性的有效手段，但要防止加剧恶劣情况
- 缓存合理使用，作为最后一道防线

### 了解更多

#### WebSocket

- 浏览器与服务器进行全双工通讯的网络技术
- 典型场景：实时性要求高，例如聊天室
- URL 使用 ws:// 或 wss:// 开头

![](static/QKWnb9uCBoXm8AxZFELcB8NpnGe.png)

#### QUIC

- Quick UDP Internet Connection
- 0-RTT 建联（首次建联除外）
- 类似 TCP 的可靠传输
- 类似 TLS 的加密传输。支持完美前向安全
- 用户空间的拥塞控制，最新的 BBR 算法
- 支持 h2 的基于流的多路复用，但没有 TCP 的 HOL 问题
- 前向纠错 FEC
- 类似 MPTCP 的 Connection Migration
  ![](static/BgAebNbCjojJOoxyTjycRc4EnsZ.png)
  ![](static/SHLqbzD6RowJPUxIcCScXxkdndd.png)

## Lesson 10 响应式系统与 React

VideoLink：

1. [React 的历史与应用 - 掘金](https://juejin.cn/course/bytetech/7180922988034785336/section/7181287649443840061)
2. [React 的设计思路 - 掘金](https://juejin.cn/course/bytetech/7180922988034785336/section/7181297907503464509)
3. [React (hooks)的写法与 React 实现 - 掘金](https://juejin.cn/course/bytetech/7180922988034785336/section/7181298684229845053)
4. [React 状态管理库与应用级框架科普 - 掘金](https://juejin.cn/course/bytetech/7180922988034785336/section/7181301644058067001)

CoursewareLink：[响应式编程与 React.pptx](https://bytedance.feishu.cn/file/boxcnGwsB2WwY2HZAp1XHvpnhoq)

### React 历史与应用

应用

- 前端应用开发，如 Facebook， Instagram， Netflix 网页版。
- 移动原生应用开发，如 Instagram，Discord，Oculus。
- 结合 Electron，进行桌面应用开发。

历史

- 2010 年 Facebook 在其 php 生态中，引入了 xhp 框架，首次引入了组合式组件的思想，启发了后来的 React 的设计。
- 2011 年 Jordan Walke 创造了 FaxJS，也就是后来 React 原型：

![](static/WDoKbV0xqoGFJcxV0rTc3YMqnEh.png)

- 2012 年 在 Facebook 收购 Instagram 后，该 FaxJS 项目在内部得到使用，Jordan Walke 基于 FaxJS 的经验，创造了 React。
- 2013 年 React 正式开源，在 2013 JSConf 上 Jordan Walke 介绍了这款全新的框架
- 2014 年 生态大爆发，各种围绕 React 的新工具/新框架开始涌现：

### React 的设计思路

#### UI 编程痛点

1. 状态更新，UI 不会自动更新，需要手动地调用 DOM 进行更新。
2. 欠缺基本地代码层面的封装和隔离，代码层面没有组件化。
3. UI 之间的数据依赖关系，需要手动维护，如果依赖链路长，则会遇到 "Callback Hell"

#### 响应式与转换式

- 转换式：给定 **输入** 求解 **输出**。例如编译器，数值计算
- 响应式：监听事件，消息驱动。例如监控系统，UI 界面

  - 事件 --> 执行既定的回调 --> 状态变更

#### React 的解决

1. 状态更新，UI 自动更新
2. 前端代码组件化，可复用，可封装
3. 状态之间的互相依赖关系，只需要声明即可

#### 组件化

1. 组件是组建的组合/原子组件
2. 组件内拥有状态，外部不可见
3. 父组件可将状态传入组件内部

#### 状态归属问题

1. React 是单向数据流，父组件传子组件，子组件通过执行函数来影响上层组件，但是本质上还是**单向数据流**
2. 解决状态不合理上升的问题，可以采用**状态管理库**，但过多使用会影响复用

#### 组件设计

1. 组件声明了状态和 UI 的映射
2. 组件有 Props/State 两种状态
3. “组件”可由其他组件拼装而成

#### 组件代码

1. 组件内部拥有自由状态 State
2. 组件接受外部的 Props 状态提供复用性
3. 根据当前的 State/Props，返回一个 UI

#### 声明周期

![](static/VcGmbaWV4ofTSQxnwTMcOt1Znsc.png)

### React (hooks) 的写法

`React.useState` 是 React JavaScript 库中的一个钩子（hook），允许您在函数式组件中添加状态（state）。在引入钩子之前，状态只能通过使用 `this.state` 机制在类组件中进行管理。像 `useState` 这样的钩子被引入，以便在函数式组件内更轻松地管理组件状态和其他行为。

`useState` 钩子返回一个带有状态值和更新状态的函数。它接受一个初始值作为参数，并返回一个包含两个元素的数组：当前状态值和一个更新该值的函数。

```javascript
import React, { useState } from 'react';

function ExampleComponent() {
  // 使用初始值 0 声明一个名为 "count" 的状态变量
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>增加</button>
    </div>
  );
}
```

`React.useEffect` 是 React JavaScript 库中的另一个钩子（hook），用于处理副作用操作，比如数据获取、订阅、手动 DOM 操作等。在函数式组件中，由于没有生命周期方法（如 `componentDidMount` 和 `componentDidUpdate`），您可以使用 `useEffect` 来处理组件渲染周期中的副作用。

`useEffect` 接受两个参数：一个是副作用函数，另一个是一个数组，用于指定影响副作用执行的依赖项。当组件渲染时，副作用函数会被调用。如果指定了依赖项数组，则当数组中的依赖项发生变化时，副作用函数会被重新调用。如果没有指定依赖项数组，副作用函数会在每次组件渲染时都被调用。

```javascript
import React, { useState, useEffect } from 'react';

function ExampleComponent() {
  const [count, setCount] = useState(0);

  // 使用 useEffect 处理副作用
  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]); // 仅在 count 发生变化时重新调用副作用函数

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>增加</button>
    </div>
  );
}
```

### React 的实现

#### Problems

1. JSX 不符合 JS 标准语法
2. 返回的 JSX 发生改变时，如何更新 DOM
3. State/Props 更新时，要重新触发 render 函数

> 以下均为解决方法

#### JSX -> JS

![](static/B9ZtbGugUoUV7Nxdbh6caoArnZe.png)

#### Virtual DOM

Virtual DOM 是一种用于和真实 DOM 同步，而在 JS 内存中维护的一个对象，它具有和 DOM 类似的树状结构，并和 DOM 可以建立一一对应的关系。

> DOM 不是在 JS 内存中，而是在浏览器中

它赋予了 React 声明式的 API: 您告诉 React 希望让 UI 是什么状态，React 就确保 DOM 匹配该状态。这使您可以从属性操作、事件处理和手动 DOM 更新这些在构建应用程序时必要的操作中解放出来。

#### Update DOM

![](static/FKx0bA9aFoK17qxBhHwc2WdUnoe.png)

#### How to diff?

- A tradeoff between update times and calculation speed
- 完美的最小 diff 算法，需要$O(n^3)$的时间复杂度
- 牺牲理论最小 diff，换取时间，得到了$O(n)$复杂度的算法—— Heuristic O(n) Algorithm

<table>
<tr>
<td>不同类型的元素<br/></td><td>替换<br/></td></tr>
<tr>
<td>同类型的 DOM 元素<br/></td><td>更新<br/></td></tr>
<tr>
<td>同类型的组件元素<br/></td><td>递归<br/></td></tr>
</table>

### React 状态管理库

![](static/VpNqb9pRnolCzVx4c9ac6Mmln3d.png)

将状态抽离到 UI 外部进行统一管理

[Redux 中文文档 · Redux](https://www.redux.org.cn/)

[XState - JavaScript State Machines and Statecharts](https://xstate.js.org/)

[关于 MobX | MobX 中文文档 | MobX 中文网](https://www.mobxjs.com/)

[Recoil - React 状态管理库](https://recoiljs.org/zh-hans/)

### 应用级框架科普

#### Next.js

硅谷明星创业公司 Vercel 的 React 开发框架，稳定，开发体验好,支持 Unbundled Dev，swc 等其同样有 serverless 一键部署平台帮助开发者快速完成部署。口号是"Let's Make web Faster"

#### Modern.js

字节跳动 web infra 团队研发的全栈开发框架，内置了很多开箱即用的能力与最佳实践，可以减少很多调研选择工具的时间

#### Blitz

无 API 思想的全栈开发框架，开发过程中无需写 API 调用与 CRUD 逻辑，适合前后端紧密结合的小团队项目。

![](static/PX4gb5LVLoUlBBx1HhscTE6unWg.png)

![](static/WtrHb2S46oLbhUxURYNckSVvnMg.png)
![](static/RKKqbU9dZon7ZIxsUDmczTwVn0d.png)

## Lesson 11 Vite 知识体系

### 浅谈构建工具

- 前端核心要素：资源

  - JS、 TS、JSX
  - CSS、SCSS、LESS
  - PNG、JPEG、WEBP
- 模块化：ESM、CommonJS、UMD

  - 提供模块加载方案
  - 兼容不同模块规范
- 资源编译：高级语法的编译

  - 高级语法转译，如 Sass, TypeScript
  - 资源加载，如图片、字体、worker
- 产物质量：代码体积、代码性能

  - 产物压缩、无用代码删除、语法降级
- 开发效率：热更新

### Vite 概要介绍

- 定位：新一代前端构建工具
- 两大组成部分

  - No-bundle 开发服务，源文件无需打包
  - 生产环境基于 Rollup 的 Bundler
- 核心特征

  - 高性能，dev 启动速度和热更新速度非常快
  - 简单易用，开发者体验好

#### 当下问题

- 缓慢的启动 -> 项目编译等待成本高
- 缓慢的热更新 -> 修改代码后不能实时更新
- Bundle 带来的性能开销
- Javascript 语言的性能瓶颈

#### ESM

- 全球浏览器对原生 ESM 的普遍支持(目前占比 92% 以上)

  - Script 标签增加 type="module" 属性
  - 使用 ESM 模块导入导出语法
- 基于原生语言(Go、Rust)编写前端编译工具链
- 如 Go 语言编写的 Esbuild、 Rust 编写的 SWC
- 基于原生 ESM 的开发服务优势

  - 无需打包项目源代码
  - 天然的按需加载
  - 可以利用文件级的浏览器缓存

![](static/BIDMbHCK6oP2mixwytdcNPUbnlh.png)

ESM 是 ECMAScript 模块的缩写，是一种在 JavaScript 中用于组织、导入和导出代码的模块化系统。它在 ECMAScript 2015（ES6）规范中引入，旨在改进传统的脚本加载方式，并提供更好的代码组织和重用机制。

ESM 具有以下特点：

1. 模块化导入和导出： 使用 `import` 关键字从一个模块中导入函数、变量或对象，使用 `export` 关键字将这些内容暴露给其他模块。
2. 静态解析： ESM 的导入和导出是在代码解析阶段处理的，这意味着导入的模块路径必须是静态的，不能依赖于运行时的条件。
3. 延迟加载： 模块在第一次被导入时才会加载，这有助于提高性能，因为只有在需要时才会加载所需的模块。
4. 作用域隔离： 每个模块都有自己的作用域，模块中的变量不会污染全局作用域或其他模块的作用域。
5. 循环依赖处理： ESM 支持解决模块之间的循环依赖问题，确保模块加载的顺序不会导致死循环。
6. 默认导出和命名导出： 可以使用 `export default` 来指定默认导出内容，以及使用命名导出来暴露多个内容。

#### 基于 ES build 的编译性能优化

ES build —— 基于 Golang 开发的前端工具，具备如下能力

- 打包器 Bundler
- 编译器 Transformer
- 压缩器 Minifier
- 性能极高，在 Vite 中被深度采用

![](static/Un9qbjQOUo0Wh5xlmMZc2W6rneu.png)

#### 内置的 Web 构建能力

Vite 开箱即用的功能等价于

- webpack
- webpack-dev-server
- css-loader
- style-loader
- less-loader
- sass-loader
- postcss-loader
- file-loader
- MiniCssExtractPlugin
- HTMLWebpackPlugin

![](static/VbCgbATfSoekZPxzZfucrgaanwd.png)

### Vite 上手实战

#### Vite 项目初始化

```bash
# Install pnpm
npm i -g pnpm
# Initialize Commands
pnpm create vite
# Install Dependences
pnpm install
# Start Project
npm run dev
```

#### 使用 Sass / Scss & CSS Modules

![](static/EEWEbixbvo21Gwx5SDsciBHtnkf.png)
![](static/TaSOb3V7iocgSoxwb9YcRXXQnyh.png)
![](static/Ctm8bTFXdoUveJxLOKSc35STnmf.png)
![](static/EyOzbFTkLoxPyZxl0aWcf1j9nUc.png)
![](static/BDdDbLrw3oGBozxBZ7lcEbWxn6b.png)

#### 使用静态资源

除了常见的图片格式，Vite 也内置了对于 JSON、Worker、WASM 资源的加载支持 [Vite —— 静态资源处理](https://cn.vitejs.dev/guide/features.html#static-assets)

![](static/QJWqbAgxXo8upVxMPiYc4SKVnFB.png)

#### 生产环境 Tree Shaking

在现代前端开发中，Tree Shaking 是一个重要的优化技术，它用于在生产环境中剔除未使用的代码，以减小最终打包后的文件大小。Tree Shaking 主要针对 ES 模块系统中的代码，并且在使用像 Webpack、Rollup 或 Vite 这样的构建工具时表现尤为出色。

Tree Shaking 的工作原理是基于静态代码分析的。它会检查模块之间的依赖关系，并从代码中识别出未被使用的部分。这些未使用的代码片段会在最终的构建过程中被移除，从而减小了输出文件的体积。

在 Vite 中，Tree Shaking 是默认启用的。但是，为确保 Tree Shaking 的有效性，请注意以下几点：

1. 使用 ES 模块： 确保您的代码使用 ES 模块（即 `import` 和 `export` 语法）。CommonJS 模块（`require` 和 `module.exports`）不支持 Tree Shaking。
2. 避免副作用： 在您的代码中尽量避免引入有副作用的代码（比如直接操作全局作用域或修改外部状态）。这有助于 Tree Shaking 的准确性。
3. 使用纯函数： 使用纯函数可以增加 Tree Shaking 的效果。纯函数是指函数的输出仅由输入决定，不受外部状态的影响。
4. 按需引入库： 在引入第三方库时，尽量只引入您实际使用的部分。一些库可能会将整个库都打包进来，但您可以通过按需引入来最小化打包文件大小。
5. 避免动态引入： 动态 `import()` 语法会导致 Tree Shaking 失效，因为它在运行时决定加载哪个模块。尽量避免在需要 Tree Shaking 的代码中使用动态引入。

### Vite 整体架构

![](static/V7wjbZM01ompUSxfjBnchTdsnUb.png)

#### 依赖预打包

![](static/LnFrbwFS8o7ZWmxyFalc5C4yngd.png)

- 进行预打包的原因

  - 避免 node_modules 过多的文件请求
  - 将 CommonJS 格式转换为 ESM 格式
- 实现原理

  - 服务启动前扫描代码中用到的依赖
  - 用 ES build 对依赖代码进行预打包
  - 改写 import 语句，指定依赖为预构建产物路径

![](static/UT1sbFSfyo0YDoxaBIHcTIaan6g.png)

#### 单文件编译

用 ES build 编译 TS/JSX

![](static/REZQbv47RoQUSHxcPUCca9ebnNe.png)

优势：编译速度提升 10-100x

局限性：不支持类型检查、不支持语法降级到 ES5

#### 代码压缩

Esbuild 作为默认压缩工具，替换传统的 Terser、Uglify.js 等压缩工具。

![](static/EULBbB1oBoBnw2xRJMacXRtcn3b.png)

#### 插件机制

![](static/Gzlibf4vToyszGx4W7FcOPLnn7b.png)

- 开发阶段 -> 模拟 Rollup 插件机制
- 生产环境 -> 直接使用 Rollup

### Vite 进阶路线

#### 深入双引擎

ES build：[esbuild - An extremely fast bundler for the web](https://esbuild.github.io/)

Rollup.js：[Rollup](http://rollupjs.org)

#### Vite 插件开发

![](static/IwD8bE2eLoLRtsxEuiicmM0On6e.png)

通过上述的 Hook，我们可以在不同的构建阶段插入自定义的逻辑。

![](static/LthubrVmDoRCeGxh4otcoYgLnIe.png)

![](static/IbtwbQrxVoAZ15xPL1ucjzbcnsg.png)

参考资料：

[Vite 插件开发文档](https://cn.vitejs.dev/guide/api-plugin.html)

复杂度较低的插件：[JSON 加载插件](https://github.com/vitejs/vite/blob/main/packages/vite/src/node/plugins/json.ts)

复杂度中等的插件：[ES build 接入插件](https://github.com/vitejs/vite/blob/main/packages/vite/src/node/plugins/esbuild.ts)

复杂度较高的插件：[官方 React 插件](https://github.com/vitejs/vite/tree/main/packages/plugin-react)

#### 代码分割(拆包)

代码分割（Code Splitting）是一种优化前端应用性能的技术，旨在将应用的代码分成多个小块（或模块），并在需要时按需加载。这样做的主要目的是减少初始加载时所需的代码量，从而加快页面的加载速度，提升用户体验。

传统上，前端应用程序通常将所有代码打包到一个单一的文件中，这意味着用户在访问页面时必须下载整个应用的代码，即使用户可能仅仅浏览了其中的一部分内容。代码分割允许开发者将应用拆分成多个较小的模块，每个模块对应一个特定的功能或路由，然后在需要时进行按需加载。

代码分割有几个主要优点：

1. 减少初始加载时间： 通过将代码分割成小块，页面的初始加载时间可以大大减少，因为只有当前页面所需的代码块会被加载。
2. 提升用户体验： 用户能够更快地访问页面内容，因为不需要等待整个应用的代码都加载完成。
3. 节省带宽： 对于访问多个页面的应用，代码分割可以减少带宽的使用，因为用户只会下载当前页面所需的代码。
4. 优化缓存： 当用户在不同页面之间导航时，只需要加载新页面的代码块，而之前加载过的代码块可以从缓存中重用。

**拆包前：**

![](static/BBL6bwKvqokDWxx2rEHcFf8Inhf.png)

> 问题：
>
> - 无法进行并发请求
> - 缓存复用率低

**拆包后：**

![](static/ZCBEbUbm1oY6jixvErlcfpkvngc.png)

**参考资料：**

[Rollup - API Configuration Options](https://rollupjs.org/configuration-options/#output-manualchunks)

[Vite - API Configuration Options](https://cn.vitejs.dev/config/build-options.html#build-rollupoptions)

#### JS 编译工具(Babel)

Babel 是一个流行的 JavaScript 编译工具，用于将新版本的 JavaScript 代码转换为旧版本的代码，以便在不支持最新语法和功能的浏览器或环境中运行。它主要用于将 ES6+（ECMAScript 2015 及更高版本）代码转换为 ES5 代码，以及应用其他转换，如 TypeScript 转换、JSX 转换等。Babel 的主要目标是帮助开发者在不同的 JavaScript 环境中实现跨浏览器兼容性和语法支持。

Babel 提供了一套插件系统，允许开发者根据需要添加不同的插件来执行各种转换。例如，你可以使用 Babel 的插件来转换箭头函数、解构赋值、模板字符串等 ES6+ 特性为 ES5 代码。Babel 还支持预设（Presets），预设是一组预定义的插件集合，可以方便地启用一组常用的转换。

![](static/ZO21bJjoyoqGaDxErInc5Cz9n0c.png)

**出现的原因：**

- JavaScript 语法标准繁多，浏览器支持程度不同
- 开发者需要用到高级语法

**参考资料：**

[babel 官方站点](https://babeljs.io/docs/)

[babel 插件手册](https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md)

#### 语法安全降级

以 Promise 语法为例，IE11 没有支持

![](static/PfOAbfzraoVj1uxqZHvcwUJ4nFg.png)

**在构建产物中避免这些问题的方法：**

- 上层解决方案：@vitejs/plugin-legacy
- 底层原理

  - 借助 Babel 进行语法自动降级
  - 提前注入 Polyfill 实现，如 core-js, regenerator-runtime

**参考资料：**

[@babel/preset-env Document](https://babeljs.io/docs/babel-preset-env)

[Vite 官方降级插件文档](https://github.com/vitejs/vite/tree/main/packages/plugin-legacy)

#### 服务端渲染 (SSR)

服务端渲染（Server-Side Rendering，简称 SSR）是一种用于构建前端应用的技术，它与传统的客户端渲染（Client-Side Rendering，简称 CSR）有所不同。在 SSR 中，部分或全部页面内容是在服务器端生成的，然后将已渲染的 HTML 内容发送到浏览器，而不是在浏览器中使用 JavaScript 动态生成和渲染页面内容。

在传统的 CSR 中，页面的初始加载会导致浏览器下载一个包含 JavaScript 代码的 HTML 文件，然后浏览器会执行该代码以生成页面内容。这可能会导致页面在初始加载时出现白屏或加载过慢的情况，因为浏览器需要先下载和执行 JavaScript，然后才能生成和呈现页面内容。

相比之下，SSR 的优点包括：

1. 更快的初始加载： 在 SSR 中，页面的初始加载会包含已经生成好的 HTML 内容，因此用户能够更快地看到页面的内容，减少白屏时间。
2. 更好的 SEO： 由于搜索引擎可以直接看到渲染好的 HTML 内容，SSR 通常对搜索引擎优化（SEO）更友好，有助于提高页面的搜索引擎排名。
3. 更好的性能： 在一些情况下，SSR 可以减少客户端的资源下载和处理负担，从而提升性能，尤其是在网络环境较差或设备性能较弱的情况下。
4. 更好的可访问性： 一些网络爬虫或辅助技术可能无法理解或处理动态生成的内容，而通过 SSR 可以提供更好的可访问性体验。

尽管 SSR 有很多优点，但也存在一些挑战，如服务器负载增加、开发和调试复杂度等。在选择是否采用 SSR 时，需要考虑项目的需求、目标受众和技术栈等因素。

![](static/VnilbBd7DoZK94xpbCPcHrEJncp.png)

![](static/HoFHbS0TWods4txZaHecYQDenWg.png)

**参考资料：**

[Vite - SSR Document](https://cn.vitejs.dev/guide/ssr.html)

[Vite 官方 SSR-Demo Project](https://github.com/vitejs/vite/tree/main/playground/ssr-react)

[使用 Vite 搭建 SSR Project](https://juejin.cn/book/7050063811973218341/section/7066612265536978981)

#### 深入了解底层标准

![](static/PZ0cbTcF8oX5MPx7HSHcRbg2nqe.png)

**参考资料：**

[ES modules: A cartoon deep-dive – Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/)

[Ship ESM & CJS in one Package](https://antfu.me/posts/publish-esm-and-cjs)

[Pure ESM package](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c)

#### Vite 社区生态

⭐ Github 58k+ star，并且目前还在持续维护

🔨 官方提供插件

- @vitejs/plugin-vue,提供 Vue 3 支持
- @vitejs/plugin-vue-jsx,提供 Vue 3JSX 支持
- @vitejs/plugin-react,提供 React 支持
- @vitejs/plugin-legacy,提供低版本浏览器降级支持

🔥 海量社区插件 [Awesome Vite](https://github.com/vitejs/awesome-vite)

🤩 众多框架内置

![](static/KT8ybeJWBoM05KxbILycDrAMnKc.png)

> 笔记记于 2023 年暑假 ByteDance 青训营——前端
> 部分发布在稀土掘金
> CHANGE
