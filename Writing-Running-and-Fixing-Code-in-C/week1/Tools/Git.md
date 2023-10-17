# Git

虽然在编程的早期阶段，版本控制(使用软件跟踪代码的多个版本，让多个开发人员轻松协作)似乎并不重要，但它是专业开发(甚至是更大规模的学术开发)的关键部分。

While it may not seem important in the early stages of programming, revision control—using software to track multiple versions of your code, and let multiple developers collaborate easily—is a crucial part of professional development (or even larger-scale academic development). 

目前流行的版本控制系统有很多，但大多数都有一些共同的原理。  

There are many different popular revision control systems, but most of them share some common principles. 

我们将重点关注git，它是目前最流行的工具，功能非常丰富。  

We are going to focus on git, which is currently the most popular tool, and is quite featureful.

我们强烈建议您尽早学习版本控制，并将其作为软件开发(以及您所做的大多数其他事情)的标准实践的一部分。  

We strongly recommend that you learn revision control early, and make it part of your standard practice for software development (and most other things that you do).

我们将介绍一些高级特性，以及使用版本控制的动机，详情请参阅 git 的相关书籍：https://git-scm.com/book/en/v2

We are going to introduce some high-level features, and motivations for using revision control here, but refer you to the git book for details:https://git-scm.com/book/en/v2

## Past versions

大多数版本控制系统的基本原理是，你将你的工作提交到版本控制系统，然后它会保存你工作的那个版本的快照。

The basic principle underlying most revision control system is that you commit your work into the revision control system, and it then keeps a snapshot of that version of your work.

当你提交时，你写一个日志条目，它描述了你所做的事情。  

When you commit, you write a log entry, which describes what you have done.

稍后，您可以查看日志，并在需要时返回到工作的旧版本。  

Later, you can review the log, and return to an older version of your work if you need to.

例如，如果你决定重写一段代码来改进它，但发现程序被破坏了，你可以回到之前的工作版本。

For example, if you decide to rewrite a piece of code to improve it, but find out that you have instead, broken your program, you can return to a prior working version.

解决这个问题的“新手工具”方法是保留工作的副本，并手工管理它们。

A “novice tools” approach to this problem would be to keep copies of your work, and manage them by hand.

你可能会想:“好吧，我可以在开始之前复制所有代码，然后在需要时再使用这个副本。”

You might think “well I could just copy all my code before I start, then use that copy later if I need to.” 

如果您有意识地意识到要进行有风险的代码重写，您可能会采取这种行动。  

If you are consciously aware that you are about to undertake a risky code rewrite, you might take this course of action.

然而，如果你开始修改代码，但后来才意识到问题所在，该怎么办?  

However, what if you start modifying your code, and only later realize the trouble?

如果你使用版本控制系统，你应该定期提交，这样就会有很好的过去版本。  

If you use a revision control system, you should commit regularly, and thus will have good revisions in the past.

此外，如果您手动创建常规副本，您将发现很难手动管理它们。

Furthermore, if you make regular copies manually, you will find it hard to manage them all by hand.

git等修订系统也有优秀的工具来处理过去的版本。

Revision systems such as git also have excellent tools for working with past versions.

例如，git有一个名为bisect的命令，它可以让你搜索过去你在哪里破坏了某些东西。  

For example, git has a command called bisect which lets you search for where in the past you broke something.

假设我知道一个功能在6个月前是可用的，然而今天，我运行了一些测试，发现该功能被破坏了。  

Suppose that I know that a feature was working 6 months ago, however, today, I ran some tests and realized the feature was broken.

我想回到过去，找出到底是哪个版本破坏了这个功能，看看在那个版本中发生了什么变化，然后更正代码。  

I would like to go back and find exactly which version broke the feature, see what changed in that version, and then correct the code. 

bisect 命令要求 git 帮助我搜索第一个有问题的版本。  

The bisect command asks git to help me search for the first broken version.

特别是，二分查找各个修订版本(因此得名)，以找到问题发生的位置。  

In particular, bisect binary searches through the revisions (thus the name), to find where the problem occured.

你可以手动引导搜索，告诉 git 访问的每个版本是好是坏，也可以提供一个 shell 脚本，让 git 自动执行搜索，判断这个版本是正确的还是错误的。

You can either guide the search manually by telling git whether each revision that it visits is good or bad, or you can have git perform the search fully automatically by providing a shell script that determines if the revision is correct or broken.

版本控制并不局限于代码，事实上，它对任何大型的协作项目(甚至是管理小规模的自己的数据)都非常有用 

Revision control is not limited to code, and, in fact, is incredibly useful for any large, collaborative project (or even for just managing your own data on a small scale).

为了提供一个bisect的具体例子，我们使用git来修订控制本书的所有材料。本课程基于latex源代码、代码示例、动画和视频记录。  

To provide a concrete example of bisect, we use git to revision control all of the materials for the book this course is based on—LATEX source, code examples, animations, and video recordings.

其中一个动画被无意删除了，我们需要将其从最新版本恢复。  

One of the animations got inadvertently deleted, and we needed to restore it from the most recent version.

编写一个shell脚本来测试该文件是否存在，然后运行 git bisect，在几秒钟内找到该文件被删除的修订版本，让我们从前一个修订版本中恢复它(确保我们有最新的版本!)。

Writing a shell script to test if that file existed, then running git bisect found the revision where the file was deleted in a matter of seconds, and let us restore it from the previous revision (and be sure we had the most up-to-date version!).

## Collaboration

当你在一个有数百个源文件和数十个开发人员的软件项目中工作时，你如何让每个人都了解最新的源文件? 

When you work on a software project with hundreds of source files and dozens of developers, how do you keep everyone up to date on the latest source? 

来回发送文件将是一场噩梦。  

E-mailing files back and forth would be a nightmare.

即使你只有两个人在一个项目中工作，管理开发人员之间的变更也是一阶问题。

Even if you only have two people working on a project, managing changes between the developers is a first-order concern.

版本控制系统，如git，支持推送(push)和拉取(pull)，即把修改发送到另一台存储库(位于另一台计算机上)，以及从另一个存储库获取最新版本。 

Revision control systems such as git support notions of pushing—sending your changes to another repository (located on another computer)—and pulling changes—getting the most recent version from another repository.

如果你试图推送自己的修改，但没有更新到其他仓库，git会要求你先拉取，这样就不会意外覆盖别人的修改。  

If you try to push your own changes, but are not up to date with the other repository, git will require you to pull first, so that you cannot unexpectedly overwrite someone else’s changes.

拉取时，git会确保你的更改与远程更改集成。

When you pull, git will take care to make sure your changes are integrated with the remote changes.

如果你拉取了数据，而且(自上次推送以来)还没有对自己的仓库做任何更改，git只会把你的仓库更新到最新版本。

If you pull and have not made any changes to your own repository (since the last time you pushed to that repository), git will simply update you to the most recent version of the repository.

如果你做了更改，git 将尝试将更改与远程更改合并。  

If you have made changes, git will try to merge your changes with the remote changes. 

如果你修改了不同的文件，或者同一个文件的不同部分，git 通常会自动处理合并。  

If you have changed different files, or different parts of the same file, git will typically handle the merge automatically.

然而，如果 git 不能自动合并，它将指出需要注意的问题，并要求你在回推更改之前修复它们。  

However, if git cannot merge automatically, it will indicate what problems need your attention, and require you to fix them before you push your changes back.

## Multiple versions of the present

版本控制工具，如git，不仅可以让你返回过去的版本，还可以通过一个称为分支的特性让你保留多个不同的“当前”版本。

Revision control tools, such as git, not only let you return to past versions, but also let you keep multiple different “present” versions, via a feature called branches.

为了了解为什么您可能需要多个“现有”版本，假设您正在开发一个大型软件项目，并决定开始添加一个新的、复杂的功能。  

To see why you might want multiple “present” versions, imagine that you are developing a large software project, and have decided to begin adding a new, complex feature.

添加此功能将花费您和您的5名开发人员团队4周的时间完成。  

Adding this feature will take you and your team of five developers four weeks to complete.

工作进行了一周后，在当前发布的软件版本中发现了一个关键问题，必须尽快修复。

One week into the effort, a critical problem is found in the currently released version of your software, which must be fixed as soon as possible.

这种情况是分支的一个很好的应用。

Such a situation is a great use of branches.

开发团队可以维护一个分支production，其中包含准备发布的代码。  

The development team might maintain one branch, production which contains code that is ready for release.

对生产分支可能做的更改只有那些已经准备好部署的更改。  

The only changes that may be made to the production branch are those that are ready for deployment.

另一个开发分支可以用于主动开发——添加新功能、测试功能，等等。  

Another development branch can be used to work on active development—adding new features, testing them, etc.

在上面描述的情况下，开发分支是团队添加新的复杂功能的地方。

In the situation described above, the development branch is where the team would be adding the new complex feature.

这些分支如何提供帮助?

How do these branches help?

负责修复生产环境代码中的 bug 的开发人员可以检出该分支(在“当前”的版本上工作)，而其他开发人员可以继续在开发分支上工作。  

The developer assigned to fix the bug in the production code can checkout that branch (working on that version of the “present”), while the other developers can continue working on the development branch.

事实上，这个开发人员可以(也应该)创建一个新的分支(让我们称之为bugfix)来修复bug。  

In fact, this developer could (and should) make a new branch (let us call it bugfix) to work on the bug fix.

然后，开发人员可以将更改提交到bugfix，如果其他开发人员也需要进行该修复，则可以切换到该分支。  

The developer can then commit changes to bugfix, and other developers can switch to this branch if they need to work on that fix as well.

bug 修复完成后，可以将其合并回生产分支，将变更合并到生产软件中。

When the bug fix is complete, it can be merged back into the production branch, incorporating the changes into the production software.

与此同时，新功能的开发将继续在开发分支上进行。

At the same time, development of new features continues on the development branch.

bug 修复完成后，还可以将其合并到开发分支中。  

When the bug fix is completed, it can also be merged into the development branch.

同样，当新功能开发完成，可以发布时，可以将其合并回生产分支。  

Likewise, when the development of new features are completed, and ready for release, they can be merged back into the production branch.

每当合并发生时，git将执行与合并从另一个仓库拉取的更改时类似的操作，要么自动处理，要么要求开发人员找出解决冲突的方法。

Whenever these merges happen, git will perform similar actions as in the case of merging in changes pulled from another repository—either handling it automatically if it can, or requiring the developer to figure out how to resolve conflicts.

请注意，这是一个小规模的激励性例子。

Note that this is a bit of a small-scale motivational example.

如果我们真的在开发一个大型软件，我们几乎肯定会想要比上面描述的更多的分支。  

If we were really developing a large piece of software, we would almost certainly want more branches than those described above.

我们可能有不同的开发人员并行处理不同的功能，并希望通过分支来管理这些更改的组合。  

We may have different developers working on different features in parallel, and want to manage combination of those changes with branches.

我们可能还需要用于不同测试阶段或其他目的的分支。

We might also want branches for different stages of testing, or other purposes.

## Read more!

我们希望已经向你展示了版本控制的一些巨大好处，建议你进一步阅读有关 git 的在线书籍: http://git-scm.com/book/en/v2/

Having, hopefully, shown you some of the great benefits of revision control, we recommend further reading from the online book about git: http://git-scm.com/book/en/v2/


在我们看来，阅读(尝试和理解)前两章是“必须”的，即使是那些对学习编程没什么兴趣的人。 

In our opinion, reading (trying out, and understanding) the first two chapter is a “must” even for those who are only casually interested in learning to program. 

如果你对认真的软件开发感兴趣，应该快速掌握第3 ~ 6章，然后在培养其他编程技能的同时继续磨练你的 git 技能。  

If you are interested in serious software development, you should master chapters 3–6 quickly, and then continue to hone your git skills as you develop your other programming skills.

随着时间的推移，您应该了解剩余的材料，并熟练使用 git。  

Over time, you should learn about the remaining material, and work to use git fluently.