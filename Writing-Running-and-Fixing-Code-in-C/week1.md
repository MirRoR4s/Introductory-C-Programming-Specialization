# Writing Code

在本模块中，你将学习编写代码，并在实践编程环境中完成你的第一次作业。

In this module, you will learn to write code and do your first assignment in the Practice Programming Environment. 

在之前的课程中，您已经练习了七步中的前四步，在学习步骤5:将算法转换为代码之前，您将在这里回顾它们。  

You have practiced the first four steps of the Seven Steps in the previous course, and you will review them here before learning Step 5: Translating Your Algorithm to Code. 

专业的程序员在开始写代码之前会花大部分时间做计划，你也将学会这样做!  

Expert programmers spend most of their time planning before they begin writing code, and you will learn to do the same!

## Introduction

### Introduction to Writing Code-Video

你好，欢迎来到课程2，用c编写，运行和修复代码。希望你参加了我们的编程基础课程，熟悉这七个步骤，以及c的语法和语义的基础知识。在本课程中，我们将专注于从算法到工作程序。 

Hello and welcome to Course 2, writing, running, and fixing code in C. Hopefully, you took our Programming Fundamentals course and are familiar with the seven steps, as well as the basics of the syntax and semantics of C. In this course, we are going to focus on going from an algorithm to a working program. 

我们将从讨论将算法转换为C代码开始。  

We'll start by talking about turning an algorithm into C Code. 

然后我们将讨论编辑代码，将代码写入计算机。  

Then we're going to talk about editing the code, writing the code into the computer. 

我们将教你使用 Emacs，这是一个专业程序员的编辑器。  

We are going to teach you to use Emacs, which is an editor for professional programmers. 

接下来，我们将讨论如何使用 gcc 编译代码。  

Next we'll talk about compiling the code using gcc. 

Gcc 代表 GNU 编译器集合，它将把您的代码转换成计算机可以直接执行的格式。  

Gcc, which stands for GNU Compiler Collection, will turn your code into a format that the computer can directly execute. 

编译完成后，就可以运行代码了，但第一次可能无法正常运行。  

Once you have compiled, it's time to run your code, but it may not work the first time. 

我们将讨论测试代码以发现其中的问题，并调试代码以修复这些问题。  

We'll talk about testing your code to find problems in it and debugging your code to fix those problems. 

我们还将向您介绍一些非常有用的工具，如 valgrind 和 gdb。  

We'll also introduce you to some very useful tools, like valgrind and gdb.

---

这些工具中的许多都被设计为对专家友好。 

Many of these tools are designed to be expert friendly. 

它们由专业人士使用，需要投入一点时间才能熟练使用。  

They are used by professionals and require a bit of time investment to become proficient in them. 

那么，为什么我们要使用这些专业级别的工具，而不是从更简单的工具开始呢?  

So why are we using these professional grade tools, rather than starting you on something easier?

如果您使用的是对新手友好的工具，那么它在开始时很容易使用，但您很快就会对使用它所能做的事情感到满意。 

If you work with a novice friendly tool, it is easy to use at the start, but you quickly plateau in what you can do with it.

另一方面，专家工具在开始时可能有点困难，但随着您对它们的经验的积累，您将远远超过使用新手工具所能做的事情。 

On the other hand, expert tools may be a bit difficult at the start, but as you gain experience with them, you far exceed what you could do with a novice tool. 

如果你从一个新手工具开始，你最终会被困在你的舒适区。  

If you start with a novice tool, you end up stuck in your comfort zone. 

由于学习它的前期成本，很难切换到专业工具。  

It is hard to switch to an expert tool because of the upfront cost to learn it.

---

然而，如果你从一个专家工具开始，你可以从一开始就学会使用它，并享受它长期带给你的力量。 

However, if you start with an expert tool, you can learn to use it from the start and enjoy the power it brings you in the long run.

---

作为新手和专家工具的一个例子，让我们谈谈录制视频。 

As an example of novice versus expert tools, let's talk about recording video. 

如果我想录制视频，我只要拿出我的手机，点击录制。  

If I want to record video, I just pull out my cell phone and hit record. 

手机就是一个很好的新手友好工具的例子。  

The cell phone is a great example of a novice-friendly tool. 

它非常容易使用，但几乎没有什么高级功能。  

It's super easy to use, but has few, if any, advanced features. 

另一方面，专业的视频设置是一个专家友好的工具。  

On the other hand, a professional video setup is an expert-friendly tool. 

它有很多我的手机没有的功能。  

It has a variety of features that my cell phone doesn't. 

我不需要把无线麦克风连接到我的手机上。  

I don't need to do things like connect wireless mikes to my cell phone. 

但专业的设置需要这样的功能。  

But such features are needed in a professional setup.

---

关于工具选择的另一个微妙之处是，您的工具选择发出了关于您的专业程度的信号。 

Another subtle point about tool selection is that your tool choice sends a signal about your professionalism. 

你会雇一个只用手机的专业摄像师吗?  

Would you hire a professional videographer who just used a cell phone?

---

我会有点怀疑。

I'd be a little bit skeptical.

编程也是如此。  

The same thing happens with programming.

我的一些学生告诉我，他们很高兴学会了这些工具。  

I've had students who have told me that they were so glad they learned these tools. 

因为当面试官发现这些学生使用专业工具时，他们显然会更认真地对待他们。  

Because interviewers noticeably took them more seriously when they found out the students used professional tools.

---

我们将以跨越第三和第四门课程的项目开始来结束这门课程。 

We're going to wrap this course up with the start of a project that spans the third and fourth courses. 

你将编写一个程序，接收一张扑克牌手牌的描述，并计算每一手牌获胜的几率。  

You'll be writing a program that takes a description of a poker hand and computes the odds of each hand winning. 

让我们开始吧。  

So let's get started.

### Planning-Reading

编写代码(或者至少应该) 90% 是计划。 

Writing code is (or at least, should be), 90% planning.  

多花 10 分钟仔细规划一段代码，可以节省几个小时的调试时间。  

Investing an extra 10 minutes in carefully planning out a piece of code can save hours of debugging a snarled mess later on.  

许多新手程序员错误地在没有计划的情况下就开始编写代码，结果却在本应该相对较短的任务上花费了大量时间。

Many novice programmers mistakenly jump right into writing code without a plan, only to end up pouring hours into what should be a relatively short task.

---

计划优先不仅是新手的最佳方法，也是熟练程序员的最佳方法。 

Planning first is not only the best approach for novices, but also for skilled programmers.  

然而，如果你看到一个经验丰富的程序员在工作，你可能不会看到她在处理一个相对简单的问题时做计划。  

However, if you see a highly experienced programmer in action, you may not see her planning when working on a relatively easy problem.  

没有看到她的计划并不意味着她没有在做，而只是说明她有能力在头脑中完成所有的计划。  

Not seeing her planning does not mean that she is not doing it, but just that she is capable of doing all of the planning in her head.  

随着你编程技能的提高，这最终也会发生在你身上——有些问题你可以在头脑中解决并写下解决方案。  

As you advance in programming skill, this will eventually happen for you as well—there will be certain problems that you can just solve in your head and write down the solution.  

当然，练习解决更难的问题所需的技能将是关键，因为如果你在能力所及范围内解决问题，你的技能将得到更好的利用。

Of course, having practiced the skills required to solve harder problems will be key, as your skills will be put to better use if you work on problems at the difficult end of your capabilities.

---

正如我们在前面的课程中所讨论的，编程规划主要包括开发解决相关问题的算法。 

As we discussed in the previous course, planning for programming primarily consists of developing the algorithm to solve the relevant problem.  

一旦设计(并测试)了算法，将其转换为代码就变得相对简单了。  Once the algorithm is devised (and tested), translating it to code becomes relatively straightforward.  

一旦用代码实现了程序，就需要测试(可能还需要调试)这个实现。  Once you have implemented your program in code, you will need to test—and likely debug—that implementation.  

对程序在每一步应该做什么有一个清晰的计划，可以使调试过程变得容易得多。

Having a clear plan of what the program should do at each step makes the debugging process significantly easier.

---

尽管之前的课程解释了步骤1-4，并做了一些示例，但我们现在将重新审视它们。 

Even though the previous course explained Steps 1–4, and worked some examples, we are going to revisit them now.

重新审视这些步骤的一个原因是，它们对编程至关重要，而且很可能已经从你的脑海中消失了，就像我们上一节课中看到的那样。  

One reason for revisiting these steps is that they are crucial to programming, and it is likely that they have somewhat faded from your mind, as we last saw them last course.  

然而，我们现在也将重新审视它们，因为你已经在模块中介绍了阅读代码和类型的材料，这些你在第一周不知道。  

However, we are also going to revisit them now as you have been introduced to the material in the modules on Reading Code and Types which you did not know in the first week. 

因此，我们现在可以讨论类型，并将所有东西表示为数字。  

Accordingly, we can now talk about types, and representing everything as numbers.  

在我们回顾步骤 1-4 后，我们将继续步骤 5 ，将我们的算法转换为代码。  

After we revisit Steps 1–4, we will continue on to Step 5, translating our algorithms to code.  

在本模块结束时，视频书写 isPrime 将解决从步骤 1 到步骤 5 的整个问题。  

At the end of this module, the video Writing isPrime will work an entire problem from Step 1 to Step 5.

## More about Steps 1-4

### Revisiting Step 1-Reading

#### Work an Example Yourself

设计算法的第一步是自己研究问题的实例。 

The first step to devising an algorithm is to work an instance of the problem yourself.  

如前所述，如果你不能解决这个问题，就不能指望编写算法来解决它，这就像试图向别人解释如何做一件你自己也不理解的事情。  

As we discussed earlier, if you cannot do the problem, you cannot hope to write an algorithm to do it—that is like trying to explain to someone how to do something which you yourself do not understand how to do.  

然而，你不仅要能够解决这个问题，而且要足够有条理地去解决，这样你就可以分析为了解决问题你所做的事情并对问题进行概括。

However, you have to not only be able to do the problem, but also do it methodically enough that you can analyze what you did and generalize it.

通常，独立解决问题的一个关键部分是描绘出问题及其解决方案。 

Often, a key part of working the problem yourself is drawing a picture of the problem and its solution.  

绘制一幅清晰而精确的图可以让你在处理问题时可视化它的状态。  

Drawing a clear and precise picture allows you to visualize the state of the problem as you manipulate it. 

对问题的状态有一个清晰的概念，以及你是如何处理它的，这将有助于你下一步的工作，在这一步中，你可以准确地写下你在这个问题的实例上做了什么。

Having a clear idea of the state of the problem, and how you are manipulating it will help you with the next step, in which you write down precisely what you did on this instance of the problem.

在本章余下的内容中，我们将以下面的问题为例:

We will use the following problem as an example to work from for the rest of this chapter:

给定两个矩形，计算表示它们交点的矩形。

Given two rectangles, compute the rectangle which represents their intersection.

你可以假设矩形是垂直的或水平的。

You may assume the rectangles are vertical or horizontal.

我们在这里应该做的第一件事是至少处理这个问题的一个实例(我们可能想要处理更多)。 

The first thing we should do here is to work at least one instance of this problem (we may want to work more). 

为此，我们需要一些领域知识——什么是矩形(有4条边的形状，使相邻边成直角)，它们的交点是什么(在两个矩形内的面积)。

In order to do this, we need a bit of domain knowledge—what a rectangle is (a shape with 4 sides, such that adjacent sides are at right angles), and what their intersection is (the area that is within both of them).

我们选择什么实例实际上是由我们自己决定的。 

What instance we pick is really up to us.  

对于某些问题，有些实例会比其他实例更容易让人洞察到问题，有些会暴露出边界情况——算法需要对该情况进行特别处理。  

For some problems, some instances will be more insightful than others, and some will expose corner cases—inputs where our algorithm needs to behave specially.  

在选择问题的特定实例时，最重要的规则是要选择一个你可以完全且精确地用手工解决的实例。  

The most important rule in picking a particular instance of the problem is to pick one that you can work completely and precisely by hand.

![image-20230928165509466](image-20230928165509466.png)

求解矩形相交问题的一个例子

**Working an example of the rectangle intersection problem**

---

上图显示了步骤 1 矩形相交问题的结果。 

The figure above shows the results of Step 1 for the rectangle intersection problem.  

我们选择了一个问题的实例——从 (-4,1) 到 (8,6) 的黄色阴影的矩形与从 (1，-1) 到 (4,7) 的蓝色阴影的矩形相交。  

We picked an instance of the problem—here the yellow-shaded rectangle from (-4,1) to (8,6) intersecting with the blue-shaded rectangle from (1,-1) to (4,7).  

结果是从 (1,1) 到 (4,6) 的绿色矩形。

The resulting intersection is the green-shaded rectangle from (1,1) to (4,6).

---

关于这个例子，你应该注意几点。 

You should note a few things about this example.  

首先，虽然黄色/蓝色/绿色并不是问题的真正一部分，但在图表中添加额外的信息来帮助您理解发生了什么并没有错。  

First, while the yellow/blue/green coloring is not truly a part of the problem, there is nothing wrong with adding extra information to your diagram to help you understand what is going on.  

其次，注意这个图是精确绘制的——我们绘制了一个笛卡儿坐标网格，并把矩形放在了正确的坐标上。  

Second, note that the diagram is done precisely—we drew a Cartesian coordinate grid, and placed the rectangles at their correct coordinates.  

这种精确性不仅确保了我们从分析图表中获得的任何信息都是正确的，而不是草率绘图的结果(尽管某些关系是否通常是正确的，或我们选择的特定情况的结果，并不能通过仔细绘图来保证)。  

This precision not only ensured that any information we obtained from analyzing our diagram was correct and not a result of sloppy drawing (though whether some relationship is generally true, or a consequence of the specific case we chose is not guaranteed by a careful drawing).  

你通常不需要绘制绘图员级别的东西，但越精确越好。

You typically do not need to draw things with draftsman-level precision, but the more precise you can be, the better.

---

在这种情况下，我们可以通过查看图片并留意绿色区域的位置来确定答案。 

In this case, we can tell the answer just by looking at the picture and seeing where the green region is.  

然而，要编写这样的程序，我们需要弄清楚其背后的数学原理，我们需要能够以某种方式解决这个问题，而不仅仅是看着图表看到答案。  

However, to write a program to do this, we need to figure out the math behind it—we need to be able to work the problem in some way other than just looking at the diagram and seeing the answer.   

有时候，当你只能看到答案时，尝试用数学方法解决问题是很困难的。  

Sometimes trying work things mathematically is hard when you can just see the answer.  

学习把显而易见的事情放在一边，思考发生了什么是需要学习的关键编程技能，但需要一些时间。

Learning to put the obvious aside and think about what is going on is a key programming skill to learn, but takes some time.

---

如果你纠结于这个问题，解决这个问题的另一个例子可能是有用的，但排除额外的信息，让你在不理解的情况下直接找到答案。 

If you struggle with it, it may be useful to work another instance of the problem, but eliminate extra information that lets you jump straight to the answer without understanding. 

下图展示了矩形问题的另一个例子，去掉了笛卡尔网格(请注意，它仍然被绘制为矩形的大小和相对位置正确)。  

The figure below shows a different instance of the rectangle problem with the Cartesian grid removed (note that it was still drawn such that the rectangles are the right size and in the correct relative positions).  

我们仍然可以从这个图中精确地求解这个问题，但只看笛卡尔网格就能得到答案有点困难。  

We can still precisely work the problem from this diagram, but it is a little harder to just look at the Cartesian grid and see the answer.  

在继续之前，花点时间算出答案。  

Take a second to work out the answer before you continue.

![image-20230928170902497](image-20230928170902497.png)

#### Another instance of the rectangle problem, with the Cartesian grid removed

请注意，处理一些问题的实例，采取不同的方法，并在这样做的时候包含/排除各种额外的信息是没有错的。 

Note that there is nothing wrong with working a few instances of the problem, taking different approaches as you do it, and including/excluding various extra information as you do so.   

一般来说，在编程的早期阶段多花点时间总比在后期阶段陷入困境要好(如果真的陷入困境，你可能想回到早期阶段，用另一个问题实例重做一次)。  

In general, it is better to spend extra time in an earlier step of programming than getting stuck in a later step (if you do get stuck, you might want to go back to an earlier step and redo it with another instance of the problem).  

对于步骤1，做几个不同的问题的例子比进入步骤2时只想到“我刚才做了，这很明显”要好。  

For Step 1, doing a few different instances of the problem is preferable to moving into Step 2 and only being able to come up with "I just did it—it was obvious."


## 工具

### 编程环境介绍

课程提供了在线的编程环境，无需在自己的电脑上下载和安装编程环境。

- 通过 git 提交和获取作业


### Instructions for Learners Upgrading from a Previous Course Version

不是从之前的版本转过来的可以直接跳过


### Programming Assignment: Assignment 00_hello

第一个编程作业，往 hello.txt 写入 hello，然后 git push，最后运行 grade 命令获取分数。

- 忽略掉别人编写的作业，一股脑全部 push 就行


### Solutions to a Few Common Problems

一些常见问题的解决方案，暂时还没有遇到，先跳过。

### [UNIX 基础](https://www.coursera.org/learn/writing-running-fixing-code/supplement/pAYd3/unix-basics)

#### UNIX 定义

问：UNIX 指的是什么？

`UNIX` 是一种多用户、多任务的操作系统，非常适合用于进行编程和编程相关的任务。

在过去 UNIX 指的是贝尔实验室于 20 世纪 70 年代所开发的一种特定的操作系统，但是在如今 UNIX 更多指的是一些类 UNIX 操作系统，比如 LINUX、MACOS 等。

#### 命令行

命令提示符默认会显示一些信息，如当前的主机名、当前的用户名、当前所在目录等。

- `~` 表示用户的家目录

问：为什么要显示当前的主机名？

因为我们有可能同时在多台计算机上打开终端。

问：为什么要显示当前的用户名？

因为我们有可能在同一个系统上出于不同的目的创建不同的用户。

所有程序都有一个当前目录，包括命令行shell。 All programs have a current directory, including the command shell. 

当您第一次启动命令shell时，它的当前目录是您的主目录。  When you first start your command shell, its current directory is your home directory.  

你可以在上图中看到，第一行的提示符是\[~\]。  You can see this in the image above, where the prompt on the first line is \[~\].

在UNIX系统中，每个用户都有一个home目录，用于存储文件。  On a UNIX system, each user has a home directory, which is where they store their files. 

通常，用户的家目录名与用户名匹配。  Typically the name of user’s home directory matches their user name. 

在Linux系统上，它们通常在/home中(所以名为“drew”的用户的家目录是/home/drew)。  On Linux systems, they are typically found in /home (so a user named “drew” would have a home directory of /home/drew). 

Mac OSX 通常把家目录放在 /Users 目录下(所以drew的家目录是/Users/drew)。  Mac OSX typically places the home directories in /Users (so “drew” would have /Users/drew). 

家目录非常重要，因此它有自己的缩写，`~`。  The home directory is important enough that it has its own abbreviation, ~. 

使用 ~ 本身指的是你自己的家目录。  Using ~ by itself refers to your own home directory. 

紧跟用户名的 ~ 指的是该用户的家目录(例如，~fred 指的是 fred 的主目录)。Using ~ immediately followed by a user name refers to the home directory of that user (e.g., ~fred would refer to fred’s home directory).

您应该了解一些与目录相关的有用命令。 There are a handful of useful directory-related commands that you should know. 

第一个是 cd，代表“更改目录”。  The first is cd, which stands for “change directory.” 

该命令将当前目录更改为指定为其命令行参数的另一个目录(回想一下，命令行参数写在命令行上，在命令名称之后，用空格与命令名称分隔)。  This command changes the current directory to a different directory that you specify as its command line argument (recall from earlier that command line arguments are written on the command line after the command name and are separated from it by white space). 

例如，cd / 会将当前目录更改为/(文件系统的根目录)。  For example, cd / would change the current directory to / (the root of the filesystem). 

请注意，如果没有空格(cd/)，命令shell将其解释为一个名为 “cd/” 的命令，并且没有参数，并给出一个错误消息，它无法找到这个命令。  Note that without the space (cd/) the command shell interprets it as a command named “cd/” with no arguments, and gives an error message that it cannot find the command. 

在上图中，你可以看到 cd 命令的两种用法。  In the image above, you can see two uses of the cd command.  

第一个将当前目录从 home 目录更改为 learn2prog 目录。  The first changes the current directory from the home directory to the learn2prog directory.  

第二行修改了 00_hello 目录(在 learn2prog 目录中)。The second changes to the 00_hello directory (which is inside of the learn2prog directory).

cd 的参数可以是你有权限访问的任何目录的路径名(相对路径或绝对路径，一般来说，你可以使用其中任何一个)。 The argument to cd can be the pathname (relative or absolute—as a general rule, you can use either) for any directory that you have permission to access. 

我们稍后会更详细地讨论权限，但现在，只要知道如果你没有权限访问你请求的目录，cd 将给你一个错误消息，并且不会更改目录就足够了。We will discuss permissions in more detail shortly, but for now, it will suffice to say that if you do not have permission to access the directory that you request, cd will give you an error message and not change the directory.

另一个有用的命令是 `ls`，它列出了目录的内容——其中包含哪些文件和目录。 Another useful command is ls which lists the contents of a directory—what files and directories are inside of it. 如果没有参数，ls将列出当前目录的内容。  With no arguments, ls lists the contents of the current directory. 

如果指定一个或多个路径名作为参数，ls 将列出有关它们的信息。  If specify one or more path names as arguments, ls will list information about them. 

对于指定目录的路径名，ls 将显示目录的内容。  For path names that specify directories, ls will display the contents of the directories. 对于指定普通文件的路径名，ls将列出有关已命名文件的信息。  For path names that specify regular files, ls will list information about the files named.  

你可以在上图中看到两个 ls 的例子。  You can see two examples of ls in the image above.  

第一个显示了 learn2prog 目录的内容(这里是本专门化课程2和3的所有作业)。  The first shows the contents of the learn2prog directory (here, all the assignments for Courses 2 and 3 in this Specialization).  第二个显示了00_hello目录的内容:一个README文件，其中包含作业说明，hello.txt是本次作业的交付文件，grade.txt是对作业的反馈)。
  The second shows the contents of the 00_hello directory: a README with the instructions for the assignment, hello.txt which is the deliverable for this assignment, and grade.txt which gives feedback on your work).

前面的视频展示了一个使用 `cd` 和 `ls` 命令的例子。 The previous video showed an example of using the cd and ls commands. 

这个示例中的第一个命令是 cd learn2prog，它将当前目录更改为相对路径examples。  The first command in the example is cd learn2prog, which changes the current directory to the relative path examples. 

然后提示符将当前目录显示为~/learn2prog。  Then the prompt showed the current directory as ~/learn2prog. 

第二个命令是 `ls`，它列出了 examples 目录的内容(因为没有参数，所以 ls 列出了当前目录的内容)。  The second command is ls, which lists the contents of the examples directory (since there are no arguments, ls lists the current directory’s contents). 

在这个例子中，当前目录中有一个目录(00_hello)和一个普通文件(README)。  In this example, the current directory has a directory (00_hello) and a regular file (README) in it. 

大多数系统上的默认情况是 ls 将其输出的代码着色:目录以深蓝色显示，而普通文件以纯白色显示。  The default on most systems is for ls to color code its output: directories are shown in dark blue, while regular files are shown in plain white. 

还有其他文件类型，它们也以不同的颜色显示。There are other file types, which are also shown in different colors.

ls 命令也可以接受特殊的参数，称为“选项”。 The ls command also can take special arguments called “options”. 

例如，ls 的 `-l` 选项要求 ls 打印它列出的每个文件的额外信息。  For example, for ls the -l option requests that ls print extra information about each file that it lists. 

选项 `-a` 要求列出所有文件。  The -a option requests that ls list all files. 

相比之下，它的默认行为是跳过文件名以开头的文件。  By contrast, its default behavior is to skip over files whose names begin with.(i.e., a dot). 

虽然这种行为看起来很奇怪，但它源于 UNIX 的约定，即文件以。  While this behavior may seem odd, it arises from the UNIX convention that files are named with a .  if and only if you typically do not want to see them. 

这些“点文件”的一个常见用途是用于配置文件(或目录)。  One common use of these “dot files” is for configuration files (or directories). 

例如，命令shell(它解析并执行您在提示符下输入的命令)在每个用户的家目录中维护一个配置文件。  For example, a command shell (which parses and executes the commands you type at the prompt) maintains a configuration file in each user’s home directory. 

对于shell bash命令，这个文件名为.bashrc。  For the command shell bash, this file is called .bashrc. 

对于命令shell tsch，这个文件被称为 `.cshrc`。

For the command shell tsch, this file is called .cshrc.

The other common files whose names start with . are the special directory names . and .. . 

In any directory, . refers to that directory itself (so cd . would do nothing—it would change to the directory you are already in). 

This name can be useful when you need to explicitly specify something in the current directory (./myCommand). 

The name .. refers to the parent directory of the current directory—that is, the directory that this directory is inside of. 

Using cd .. takes you “one level up” in the directory hierarchy. 

The exception to this is the .. in the root directory, which refers back to the root directory itself, since you cannot go “up” any higher.

与许多 UNIX 命令一样，ls 命令还有许多其他选项。 The ls command has many other options, as do many UNIX commands. 

随着时间的推移，您将熟悉经常使用的选项。  Over time, you will become familiar with the options that you use frequently. 

然而，您可能想知道如何找到您不知道的其他选项。  However, you may wonder how you find out about other options that you do not know about. 

与大多数 UNIX 命令一样，ls 也有一个手册页(如前所述)，其中描述了如何使用该命令以及它所采用的各种选项。  Like most UNIX commands, ls has a man page (as we discussed previously) which describes how to use the command, as well as the various options it takes. 

你可以在命令提示符下输入 `man ls` 来阅读这个手册页。You can read this manual page by typing man ls at the command prompt.

另外两个与目录相关的有用命令是 mkdir 和 rmdir。 Two other useful directory-related commands are mkdir and rmdir. 

mkdir 命令接受一个参数，并通过指定的名称创建一个目录。  The mkdir command takes one argument and creates a directory by the specified name. 

rmdir 命令接受一个参数并移除(删除)指定的目录。  The rmdir command takes one argument and removes (deletes) the specified directory. 

使用 rmdir 删除一个目录，该目录必须是空的(不能包含任何文件或目录，除了)。  To delete a directory using rmdir, the directory must be empty (it must contain no files or directories, except for . and .. which cannot be deleted).
