---
layout: post
title: LaTeX Ubuntu NS2 Linux Programming Facebook Twitter 京剧 越剧
date: 2011-05-20
summary: 
categories: OldTimes
---

回家数日，除了颓废之外，总归还是做了些工作的。还有一个月就要回去，这期间还有些工作要做，暂且总结一下这几日以来做的事情，给后来人行个方便。

### LaTeX

LaTeX是个好东西，放在Windows下，CTex是个好东西。其实说来说去就是Tex，一个奇伟神奇的文档编写系统。刚开始的时候，因为其不是所见即所得的形式，我还大大的觉得其落后（毕竟word的历史跟他比差远了）。然而，当熟悉了这种文档编写模式的时候，就会发现，编写出来文档之美，之标准，是普通Word文字处理所不能及的.

MathType一直是我用来公式输入的，因为还可以声称gif图片，就更加的喜欢。但是了解了Tex的公式编辑之后，对其就不那么感兴趣了，除非是聊天时突然要表示个公式，不好去编译，写文档时已经是不用它了

Windows平台下，做的很好，而且也有很多资料可查的Tex平台是CTex。推荐下载时下载完全版，这个完全版在安装时是同时支持中文和英文的，对于写英文文档的同学来说，直接装英文就很好。说实话，用LaTeX写中文文档感觉怪怪的。安装完成之后，在开始的目录下，会有一个FontSetup，是一个安装字体的东西，装上之后CTex就算是完成了。CTex中除了编辑器WinEdt之外，最常用的就是MikTex，本来MikTex是一个单独的Tex套装，CTex是在其基础上形成的，之所以说MikTex是因为其编译非常方便。于是在Windows下写文档时，我通常都是用WinEdt写tex文件，因为有语法高亮提示，看着会很舒服。再用MikTex里的编译器进行编译。这是我熟悉的编写方式。

关于LaTeX的学习，吴凌云同学写的CTEX-FAQ是一个对初学者很好的材料，会给出一个比较宏观的蓝图。Tobias Oetiker等编的《一分不太短的LaTeX介绍》再被中国CTex小组翻译之后，成了一个初学者绝妙的教材，我个人就在这两个文档的指导下，一步一步走向LaTeX文档编写的。

WinEdt是一个注册的软件，而且其6.0版网上现在还没有给出很好的注册码让其变成注册版。但是就好像因缘际会一样，不注册的WinEdt仍然是全功能软件，而且，可以修改它的配置文件使其在每次退出时把30天注册记录消除掉，用这样的方法间接的实现注册。虽然那个Unregistered Copy让我十分不爽，但是鉴于都集中在文档编写去，很少注意任务栏也就是了。

Linux平台下，我到现在为止还没有装上LaTeX开发环境，原因是因为比较大，尤其是在我这比较扯淡的网速下，近两日想要考虑在上面装上一个LaTeX开发环境。apt-get的超级牛力也不是盖的。（下文还有介绍）

LaTeX大概就是这么多了，刚开始接触LaTeX的时候，使用者可能觉得怎么这么麻烦，头尾都要写，但是当你看到自己编写的文档编译出来之后，就会发现那种效果是多么的令人惊艳。所以，一定要坚持下去。尤其是在编写大型文档时，LaTeX所表现出来的，超乎寻常的智能和体贴，是完全将Word抹杀的。

LaTeX就像龙泉剑，Word就像青铜剑，青铜剑是个剑客就可拿得，无论是顶级的还是低级的。然而一旦从青铜剑换上龙泉剑，虽然开始的时候还无法驾驭这么强大的神兵，但是勤加练习，一定会感受到为什么被成为神兵的道理。这一点，对有志于成为学者的人尤为重要。

### Ubuntu

Ubuntu，用Sheldon的话说，是我最喜欢的Linux系统。虽然还有ReadHat和RedFlag等Linux发行版，但是Ubuntu无疑是我目前为止用到过最爽的系统，以至于我有心重新格式化整个系统，将250G的半壁江山割给它。

我用的Ubuntu是10.10版，这个版本是去年12月发行的。作为一个稳定版，我在下载的时候毫不犹豫的选择了它。现在11.04已经出来了，有的同学刚刚装上Ubuntu的，选择了这个版本，但是我觉得好像不是很明智，也许是我个人的癖好而已，无论什么，都是喜欢最新的稳定版。（虽然电脑中存在着大量的Beta版本软件……）

下载下来Ubuntu的镜像是多国语言版的，用wubi来安装的时候可以体现的出来。如果你不是从硬盘安装而是用wubi来在硬盘上虚拟出一个系统来，那么一切的过程都是相当简单的，只需要把镜像和wubi放在同一个目录下，然后打开wubi，填写以下需要的信息就行了。重启机器，你会发现和Windows并列的，还有一个Ubuntu的选项。进去之后，Ubuntu自己开始配置，一切都是傻瓜式操作，比Windows的配置还简单。

这里推荐使用Ubuntu的英文版，说实在的，打算学Linux就已经是一件超出Windows用户的事情，那么英语应该也不是什么障碍，况且Ubuntu下的文档写的十分亲民，几乎没有阅读障碍。我虽然没有使用过中文版本，但就Windows如此成熟的操作系统，仍有大量的文档是英文的在先，那种中英交错的操作系统着实的drives me crazy。

Ubuntu下的文件组织结构是完全不同于Windows的，于是我就靠着Ubuntu Software Center来管理软件，也就不再想那个实际上非常有效率，表观赏让我不能理解的文件组织模式。而这也是我最近混迹于Linux系统下的一条经验，如果不理解，忽视之。需要理解的，正视之，以点带面，就会慢慢的熟悉起来了。

我在Ubuntu下做的比较多的还是NS2和Linux Programming的学习，对于命令，基本上是来一个记一个，我觉得这一点对于像我这样从Windows平台下转而变成Linux平台下编程的人员来说还是挺重要的，不然一个Linux就是一大本书，虽然都是知识，但是那样有些太没有主次了，而且在Windows下的开发经验也完全体现不出来优势。

最后一个是关于快捷键，我对于快捷键的痴狂，是自从我发誓把鼠标拔出我的电脑开始的。因为笔记本的触摸板并不是像鼠标那样十分的好用，于是我就开始了疯狂的使用快捷键，刚到Ubuntu的时候，除了几个文档编辑的快捷键以外，我几乎不知道什么快捷键了，以至于刚刚安装上Ubuntu的前两天，我就是单纯无效率的使用触摸板（因为鼠标已经被我扔了，我说的是，真扔了）。这个情况直到我第三天开始腾出时间来开始找到Ubuntu主要的快捷键开始，经过大约一周的磨练，基本上也快完全掌握了。Linux环境下的软件有一个好处，控制台下自然是要由命令来执行的，而图形界面的也基本上都有强大的快捷键系统。和Windows一样，基本上都是通用的。至少到现在我用到的软件为止，都是有强大的快捷键系统支撑的。

对于无线网卡的驱动。我得要说一下，我和很多的同仁一样，也是用的博通的网卡，我的更加偏门，是我刚开始在网上搜的时候都没有见到的430M。Ubuntu论坛上有很多关于解决博通网卡驱动的文章，但是对于刚刚接触Linux的人士来说，操作起来不仅具有难度，而且个个机器的情况不同，如果出现了错误就更加会让用户失落。我实际上回忆不起来我是怎么做到让网卡被识别的，只好稍微的回忆一下。当时我在装了一些和硬件驱动有关的软件之后，Ubuntu突然弹出一个页面来，其中有一个关于博通网卡的驱动，我点了install。然后就万事大吉了。（大家不妨往这个方向努力一下，Ubuntu中好像有关于drivers的软件）

### NS2

NS2=Network Simulation 2。是网络仿真软件，没有图形界面，不过在分析中是有模拟仿真过程的图形界面的。这个东西是通信专业中算是必备的一个软件，不过自然的是，通信专业受限要有通信基础，而我是从单纯的编程和分析角度切入的，于是前面的那些必备的基础，我就略过了吧。

这个软件折腾的我不轻，首先是在Windows平台下，我不会用它进行完全的工作，转到Linux下，几次安装受阻。再后来，我在Ubuntu Software Center中发现了NS2，点下了install，等了一会，完成了。神马环境变量，神马配置信息，神马都不用管。于是在一片欢呼雀跃的时候，我开始了正式学习NS2的旅程。

学习NS2的，TCL语言是不可避免的，于是开始照着网络上的标程开始敲，一切如常。当基本把TCL语言的规则搞得差不多的时候，就要开始进行简单的网络模拟了，这时一个让我不爽的东西出来了，图像化的模拟器nam出不来。上网查，说是我自己还要编译一下nam，这也没什么难的，关键就在于我是用Ubuntu装的NS2，找不到nam这个目录，于是不能编译。彻头彻尾的囧了两天，这个问题在百思论坛上也挂了两天。有位仁兄告诉我，可以再Software Center中找到nam装上，我上网一搜，一个blogspot上的博文图片表示确实有，但是我自己在寻找的时候却找不到。

这时候，一个神奇的想法掉入了我的心理。

~~~
sudo apt-get install nam
~~~

由于过于激动，打错了好几次。当对了的那一刻，apt-get开始发挥其神奇牛力，驱动着网络，我顺便瞄了一眼：nam1.15。完成之后再次运行刚开始的时候的模拟，成功，图形界面跑出来了！于是为了庆祝这一盛事，我进行了一个京剧+火影忍者的联播。京剧是《四郎探母》一共12折，火影忍者是432集，昨个刚翻译出来。

用来编写代码的工具和在Linux下写程序的编辑器是一样的，都是用的Emacs。Emacs是个神奇的编辑器，拥有一个完全不同的编译器，基本上除了电脑上的Home等已经编程的建之外，就连复制粘贴这样的快捷键就是完全不同的样子。Emacs除了文档写作之外，基本上是属于一个控制台为核心控制的编辑器，产生了这么多风格独特的快捷键也是情有可原的。

### Linux Programming

在Ubuntu下，除了NS2的学习之外，就是Linux
Programming了。除了为了更加的熟悉C语言是怎么在系统中发挥作用的，其次也是为了进行Linux开发打的基础。我相信我暂时放弃VC平台下的开发是一个明智的事情，因为我在Linux编程的学习中，我没有看到那么多繁复的操作，一切都像原来C语言那样自然。

对于这项工作，我才刚刚开始，学到了shell编程的阶段。在Linux下，无论是什么编程语言，让我觉得风格统一的，而不是像Windows下，不同中见出的统一。我刚开始进行Windows下窗口开发的时候，觉得源程序是那么的恶心，觉得不是C语言，但是掐头去尾，又是了。而Linux就完全没有这样的事情，main函数还是main函数，printf还是printf。一切都是自然的。

而由于对于Linux下编程还没有更深入的体会，再有感想，再说。

在Windows下，由于各种原因，用的都是集成开发环境，中间的过程，有过一些了解，但是没有深入，而使用了GCC之后，开始亲手把中间的文件进行编译（当然，是必要的），那种细致入微的感觉，是我从来没有感受到过的。觉得很好很强大。

### Facebook Twitter

自从回国之后Facebook，Twitter就不能上了，不能上了，总归是要想上的办法的。于是面对着不高不矮的墙，开始准备翻。翻墙么，容易极了，自由门兄，在线代理兄（当然，要管用的），SSH兄，VPN兄。这几个里面，我恐怕没有用过的，只有SSH兄了。剩下的三个，我都是在以前还没意识到墙外春色的时候，单纯为了换IP使用的。

VPN兄，现在有点不好使了，一不想花钱，二不想麻烦，虽然质量很好，但是鉴于上面两点，不用了。在线代理兄，倒是能登录几个页面的不过好像也不大管用了。SSH兄，服务商给了我一个，配置了半天，也没搞上，据群里的弟兄说，他们这两天也挂不上，暂时就算了，于是从回来到现在，一直都是靠着自由门兄撑腰的。

我一直说，轮子功干的几件好事之一就是自由门兄。轮子功自己虽然有些丧尽天良，而且现在派系四立，但自由门兄倒是尽职尽责，不过唯一不好的地方就是不能访问国内IP的东西了，虽然国内的有很多五毛党，但不是所有人都拿这玩意当成什么政治武器来使唤的的。于是穿梭在国内的资料站和国外的资料站的时候，不可避免的就是自由门兄的开开合合。

今天登陆facebook的时候，发现facebook被锁了，估计是facebook兄看见我的IP老换吧。不知道铁通的IP到底是怎么回事，竟让还有把我认成邢台的。而更加悲剧的是facebook问我安全问题，虽然我一贯是那几个问题，但是竟然试了几遍都没成。今天是没戏了，明天接着蒙答案去。

Twitter和Penny Can是一回事，不深入没事，深入了，就不可自拔。除了学习和研究的时候，只要开开自由门兄，我基本上都是在twitter上泡着，而不是新浪微博。虽然新浪微博上有我一千多条微博，还有快200人的followers。没准过两天我会发现，然后直接关了新浪微博。

还有一些外国神牛的BLOG在墙内也打不开了，我估计都是因为其几句话而已，但是这实在是无理取闹，而且须知墙越高，越容易塌。据称方校长被砸了，看来他没有小布什的敏捷和温家宝的幸运。这倒是一个怪诞，一个中央下来的算是比较高官的人物，竟然受到了这样的礼遇，而且跟他作对的不止是那帮武大的学生，还有身后的3亿多网民。我一直只是对墙反感，倒是不知道是谁盖起来的，昨天才知道，那位墙父的姓氏名讳。他跟一般的砖家叫兽是有区别的，他是懂技术的，而且是真的懂，不是那种故弄玄虚道貌岸然的主。这也就注定了，那帮砖家叫兽只能在地方电视台上喊喊，而他，可以被全中国网民所憎恨。

### 京剧

生在邯郸，喜欢戏曲，虽然能听得下去豫剧，却不喜欢。这是有些蹊跷的，在邯郸这个地方，找个喜欢豫剧的一把抓，找个喜欢京戏，尤其是京戏加越剧的人，就难找的很。找到了，无非是什么流派都喜欢的人。

京剧和越剧，在我心里给个排位，越剧似乎算是略胜一筹，因为在我看来，越剧是文人戏，我喜欢那种柔柔的，却清脆的东西，越剧就是这么个玩意。京剧，忠臣良将，才子佳人我都喜欢。不喜欢的，是当今涌出来的现代戏，现在装上有线电视之后，有那么几个戏剧频道，播一些这两年才出来的本子，无论是扮相还是唱腔，都经不起推敲，这样的东西，是糟蹋京戏。

喜欢京剧，是从喜欢相声开始的，相声里有两个段子，一个是《四大须生》，一个是《四大名旦》。南昆北义，东柳西梆；马谭杨奚，梅尚程荀。是从那些脍炙人口的唱段开始的。若是再究一究根底，是从一出叫《龙凤呈祥》的戏出来的，当时还小，迷着三国，有天晚上，家里换到这《龙凤呈祥》，讲的是刘备东吴相亲的故事。我自然是对这段故事熟悉的不能再熟悉了，借着这股子劲，把这出戏从头看到了尾。 也有的没有的记住了乔玄的些唱段。

再后来和戏曲结缘的时候，就是评戏的《花为媒》，那时候赵丽蓉老师还主要当着评剧演员呢，这出《花为媒》的两个媒婆之一，就是她演的，颇是有意思。在此之后，一直到《四大须生》之前，京剧的印象在我心里就一直是春晚的戏曲联唱。这个时间，有那么几年。

我开始的时候，觉得如果我不睁眼看字幕，实际上是不能知道演员说什么的，因为有的字拉的很长，京字京韵有的时候听不大清楚。可听了那么几出戏之后，就觉得远不是那么回事，真的好演员，是要带着观众进入情境的，而这情景，是跟台上怎么样没什么关系的。固然唱念做打重要，但如若真的带入了情境，这动作表情，都成了无形的东西映在观众的心理。于是，我也从我自己的角度解释了为何老人有滋有味的听着收音机理出来的声音，他们进去了。

### 越剧

越剧是个文人戏。这是我说过多遍的，即便是武打戏，也难见到那种京剧式的快意恩仇，多的却是一份俏皮和灵巧。更不用说那才子佳人的戏码了。

我整折整折的戏，所看过的并不多，《梁祝》，《西厢记》和《红楼梦》。是我最先看的。尤其是梁祝，又是看了多遍。《追鱼》，《穆桂英挂帅》也是看过些，但并没有整折子看过。真的是美啊。越剧时间不长，150年左右，却形成了独有的古典特色，归结起来，恐怕又是江南小桥流水人家养出来的戏曲。

越剧不管是什么角，都是淡淡的妆，衣服上，边边角角都是雅致的纹路。男的行云流水，女的袅袅婷婷，别是有一番风趣的。喜欢越剧，唱念做打，都是喜欢的，尤其是唱，所谓的“纤音入云”者。且真的能把人震住，所谓震住人，是分几种的。声音大是一种，行云流水下来，繁复的贯口是一种。越剧两者都不是，而是那文人独喜欢的雅致的气息，震住了人。

越剧是少讲什么忠义的，这么绵软，忠义讲了也没什么说服力。倒是儿女情长，月上柳梢头的功夫没少下。什么时候真的演起大忠大义的戏来，除了俏皮，恐怕没有一处可看的了。不过矛盾那么激化，俏皮也没什么好看的了。

我故事就少讲了，驾驭文字的底子没有那么厚，除了一个劲的浮夸，没什么好说的。回家十余天，有这么几个令人兴奋的东西一直跟在身边，真好。
