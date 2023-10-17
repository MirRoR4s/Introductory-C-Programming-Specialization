# Emacs

编程时，编辑器(用于编写代码的程序)是提高效率的关键。

When you are programming, your editor—the program you use to actually write your code—is key to your productivity.

编辑器最重要的一点是，它不会妨碍你通过键盘将想法从大脑中传递到源代码中。

One of the most important aspects of the editor in your productivity is not getting in the way of the flow of ideas from your brain through your keyboard, and into your source code.

虽然这一点对初学者来说可能看起来很奇怪或不重要，但当你变得更有经验时，你会开始发现自己在编程时“很投入”。  

While this point may seem odd or unimportant to novice programmers, as you become more experienced, you will start finding yourself “In The Zone” as you program.

当你处于“In The Zone”时，你的精神焦点完全专注于你的程序，你的头脑中充满了你对程序的计划和设计。  

When you are “In The Zone,” your mental focus is fully dedicated to your programming, and you have your mind full of your plans and designs for the program.

在这里，扰乱你的注意力会让你离开这个区域，破坏你的精神注意力，失去你的思路。

Here, disrupting your focus at all can take you out of The Zone, destroying your mental focus and losing your train of thought.

程序员编辑器(如 Emacs 和 Vim )的设计使得您可以在双手不离开键盘的情况下完成所有需要的操作。

Programmer’s editors (such as Emacs and Vim) are designed so that you can do everything you need without taking your hands off the keyboard.

在键盘上做任何事情对于保持专注是至关重要的——暂停鼠标，在菜单中寻找你需要的东西足以扰乱你的注意力。  

The ability to do everything on the keyboard is crucial to staying in The Zone—pausing to grab the mouse and stumble through menus looking for what you need can be enough to disrupt your focus.

相反，使用像 Emacs 和 Vim 这样的工具的程序员在肌肉记忆中有键盘快捷键，他们可以在不有意识地思考如何执行活动的情况下，将全部注意力放在编程任务上。

Instead, programmers using tools like Emacs and Vim have the keyboard shortcuts for anything they do regularly in muscle memory—they can perform the activities without consciously thinking about how, leaving their full focus to their programming tasks.

编程编辑器除了能让你不受鼠标干扰而保持专注之外，还提供了许多其他提高生产力的功能。

Besides enabling you to stay In The Zone by not having the distraction of the mouse, programming editors provide a variety of other productivity enhancing features.

其中一个功能是语法高亮——根据输入的单词在语言语法中的适应程度对其进行着色(例如，关键字、类型名称、声明的函数名称、字符串字面量、整数常量等)。 
One such feature is syntax highlighting—coloring the words that you type based on how they fit into the syntax of the language (e.g, keywords, type names, the name of a function being declared, string literals, integer constants, etc…). 

语法高亮可以帮助你更容易地阅读代码，例如，你可以很容易地区分字符串字面量中的文本。

Syntax highlighting helps make it easier for you to read the code—for example, you can easily distinguish what text is inside a string literal.

它还可以帮助你避免、识别和纠正错误，例如不小心使用了一个关键字(你不熟悉的)作为变量名，字符串字面量中的引号不匹配(或不正确的转义)，或拼写错关键字。

It also helps you avoid, identify and correct mistakes—such as accidentally using a keyword (that you are not familiar with) as a variable name, mismatching (or improperly escaping) quotation marks in string literals, or misspelling keywords.

另一个特性是能根据语言结构自动缩进。 

Another feature is automatic indentation according to the structure of the language. 

程序员通常认为，根据嵌套级别(包含多少个{})缩进代码是正确样式和格式的关键元素。  

Programmers generally consider indenting code according its nesting level (how many {} it is inside of) to be a key element of proper style and formatting. 

这不仅有助于提高可读性，而且让编辑器根据实际嵌套级别(而不是程序员认为的级别)自动缩进，可以帮助尽早识别和纠正错误。

Not only does this help with readability, but having the editor automatically indent based on the actual nesting level (as opposed to what the programmer thinks it is) can help identify and correct errors earlier.

编程编辑器的第三个重要特性是它们能够与程序员使用的其他工具进行交互，这些工具包括调试器、编译/构建工具和版本控制系统。 

A third important feature of programming editors is their ability to interact with the other tools used by the programmer—the debugger, the compilation/build tools, and revision control systems.

例如，在Emacs中，您可以在编辑器中进行编译，如果编译产生错误，则直接跳转到编辑器中的每个错误。  

For example, in Emacs, you can compile from within the editor, and if the compilation results to errors, jump directly to each of them within the editor. 

同样，在使用调试器gdb时，Emacs知道如何与gdb交互，并显示代码中的当前执行点，让您可以向gdb发送有关正在查看的特定代码行的命令。

Likewise, when using the debugger gdb, Emacs understands how to interact with gdb and will display the current execution point in your code, and let you send commands to gdb about a particular line of code you are viewing.

我们还会注意到，编程编辑器通常在用途方面有很大的灵活性。 

We will also note that programming editors typically have a lot of flexibility in what they are useful for.

本书的作者几乎在编写本书时都使用Emacs !  

The authors of this book use Emacs for pretty much everything that they write, including this book itself! 

与编程一样，在编写文本时，保持专注对生产力至关重要。

As with programming, staying In The Zone is crucial to productivity when writing text.

虽然Emacs和Vim都是适合专业程序员的编辑器，但这里我们将重点介绍Emacs。

While both Emacs and Vim are appropriate editors for professional programmers, we will focus on Emacs here.

我们注意到，如果您使用(或想学习)Vim，那很好，但讲师使用并了解Emacs。  

We note that if you use (or want to learn) Vim, that is great, but the instructors use and know Emacs.

我们建议你对这两种编辑器有一个基本的了解(如果你需要使用的系统只安装了一种，而没有安装另一种)。  

We recommend having a basic familiarity with both editors (in case you ever need to use a system where one is installed, but not the other).

然而，我们注意到，几乎不可能同时成为这两方面的专家。  

However, we note that it virtually impossible to be an expert in both of them.

请记住，您希望训练肌肉记忆，以便您可以本能地执行编辑器命令，而无需考虑它们。  

Remember that you want to train your muscle memory so that you can perform editor commands by instinct, without thinking about them.

对于两套完全不同的编辑器命令，大多数人都无法做到这一点。

Most people cannot do this for two completely different sets of editor commands.

**重要提示**:当使用像 emacs 这样的程序时，请确保如果你用 ctrl-z 挂起一个进程，你总是会返回到你用 “fg” 开始的会话。 

**IMPORTANT**: When using programs like emacs, be sure that if you suspend a process with ctrl-z that you always return to the session you started with "fg". 

不要重复启动emacs会话。

Do NOT repeatedly start emacs sessions. 

这将导致你的PPE关闭，直到第二天才能完成任务。  

This will cause your PPE to get shutdown, locking you out of the assignments until the next day.