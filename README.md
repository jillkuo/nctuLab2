# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program
> * Show the screenshot of using iPerf command in Mininet  
   
編輯完Python code後，回到終端機下達指令: 
   
> chmod +x topology.py  
   
意思是使用chmod(用於控制用戶對檔案的權限的命令)，增加對檔案執行的權限(+x)，這個檔案叫做topology.py。  
接著輸入指令:
   
> ./topology.py  
   
來執行topology.py。 
接下來就會進入CLI mode。  
然後輸入iPerf command進行測量。  

![alt text](https://github.com/nctucn/lab2-jillkuo/blob/master/iPerf.png)  

---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail  

**Topo** is base class for Mininet topologies.  
1. **addSwitch('name_of_the_Switch')**  
   在topology中增加Switch，命名為name_of_the_Switch。  
2. **addHost('name_of_the_Host')**  
   在topology中增加Host，並命名為name_of_the_Host。  
3. **addLink(data_of_the_Link)**  
   在topology中增加Link，並且說明它分別連接哪兩個Switch或Host，bandwidth是多少，time delay是多少ms，以及loss rate。  
4. **start()**  
   啟動network。  
5. **dumpNodeConnections(net.hosts)**  
   dumps connections from a set of hosts  
6. **dumpNodeConnections(net.switches)**  
   dumps connections from a set of switches  
7. **CLI(net)**  
   開啟CLI mode  
8. **Mininet**  
   用來管理network的main class  
9. **setLogLevel('info')**  
   default output，'info' 是指network的一些基本資訊。

### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail  

執行topology.py後，會進入到CLI mode。  
接著輸入:  

> h6 iperf -s -u -i 1 > ./out/result &  

將名為h6的Host訂為傳出端Server(-s)，使用UDP協定(-u)，每經過一秒都顯示一筆數據(-i 1)，然後把結果輸出到./out/result  
接著輸入:  

> h3 iperf -c 10.0.0.6 -u -i 1  

將名為h3的Host訂為接收端Client(-c)，其server的IP為10.0.0.6，使用UDP協定(-u)，每經過一秒都顯示一筆數據(-i 1)  

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**
   打開PieTTY連接到學校的系統140.113.195.69且port為10025，進入到屬於自己的container中，並且login。  
   在container中輸入:  
   > git clone https://github.com/nctucn/lab2-jillkuo.git  
   
   取的這次lab所需要的檔案。  
   接著嘗試輸入:  
   > mn  
   
   試跑一下Mininet。  
   若出現Error，則輸入:  
   > service openvswitch-switch start  
   
   來開啟Open vSwitch的service。  

2. **Example of Mininet**
   接著來試跑一下下載的檔案中所提供的sample code(example.py)。  
   首先先進入example.py所在的資料夾，輸入:  
   > cd /root/lab2-jillkuo/src/  
   
   然後增加執行的權限，輸入:  
   > chmod +x example.py  
   
   接著執行程式，輸入:  
   > ./example.py
   
   就會看到結果。  
   若是出現Error，則輸入:  
   > mn -c  
   
   再次輸入:  
   > ./example.py  
   
   即可。  

3. **Topology Generator**
   首先要先創建或編輯topology.py，輸入:  
   > vim topology.py  
   
   進入檔案後，按i做編輯，按ESC離開編輯模式，輸入:wq離開檔案，回到終端機。  
   詳細的內容解釋都在topology.py裡的註解中。  
   接著要執行topology.py，輸入:  
   > chmod +x topology.py  
   > ./topology.py  
   
   若出現Error，則一樣輸入:  
   > mn -c  
   
   再次輸入:  
   > ./topology.py  
   
   即可。
   這個時候因為在topology.py加入了CLI(net)，所以會進入到CLI mode。  

4. **Measurement**
   這次我所做的是topology2，所以我在進入到CLI mode後要進行量測的是在h6與h3之間傳封包的實驗。  
   因此輸入:  
   > h6 iperf -s -u -i 1 > ./out/result &  
   
   接著輸入:  
   > h3 iperf -c 10.0.0.6 -u -i 1  
   
   就會得到結果，其中在packet loss的數據中，其理論值為13% ~ 18%，但是其中有一次我的測量結果為23%，大於理論值，但僅此一次，推測是機率造成的問題。  
   若要離開CLI mode回到終端機，則輸入:  
   > exit  
   
   接下來必須將檔案push到Github，因此在終端機中來到要push的資料夾，輸入:  
   > git add .  
   > git commit -m "COMMIT MESSAGE"  
   > git push origin master  
   
   來完成動作。  

---
## References

> TODO: 
> * Please add your references in the following

* **參考資料**  
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)  
    * [README](https://github.com/guodongxiaren/README)  
    * [chmod](https://en.wikipedia.org/wiki/Chmod)  
    * [利用 iperf 測試網路效能](https://cms.35g.tw/coding/%E5%88%A9%E7%94%A8-iperf-%E6%B8%AC%E8%A9%A6%E7%B6%B2%E8%B7%AF%E6%95%88%E8%83%BD/)  
    * [Python error: command not found](https://stackoverflow.com/questions/30285154/python-error-command-not-found)  

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [YOUR_NAME](YOUR_GITHUB_LINK)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
