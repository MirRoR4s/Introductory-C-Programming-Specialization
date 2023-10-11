# Revisiting Step 2

## Write Down What You Just Did

Now, you are ready to think about what it was _exactly_ that you just did, and write down a step-by-step approach to solve one specific instance of the problem. Using our example from a figure in the previous lecture:

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/AtFN3qRbEee8sxKIYeYw8g_7fcaba0fe7467c441ab03cecd607b855_4.1.2-another-instance.png?expiry=1697155200000&hmac=tATOfgcHKxUHdzKMcssgI1zbQJdc3S3hGs4b18vlroA)

this would basically be a set of steps anyone could follow to find the intersection of the rectangle from (-2,1) to (6,3) with the rectangle from (-1,-1) to (4,4). Note that you are not trying to generalize to _any_ rectangles here, just writing down what you did for _this particular_ pair of rectangles.

There are actually two important pieces to think about here. The first is how you represented the problem with numbers. Remember the key rule of programming: Everything is a number. Since a rectangle is not a number (in the way, for example, that the price of bread , we will have to find a way to properly _represent_ a rectangle using a number (or several). If you go back and read the descriptions of the instances of the problems we worked, you will find that we already have been representing each rectangle with 4 numbers—two for the bottom left corner, and two for the top right corner. Now that we have assured ourselves that rectangles are numbers, we know that we can happily compute on them—we also have an idea of what information we should think of a rectangle as having (each of which is just a number): a bottom, a left, a top, and a right. This analysis leads us to make the same definition of a rectangle as in the Structs lecture in the _Programming Fundamentals_ course, but we underscore here as it is an important part of the programming process.

The second thing we need to think about is what exactly it was that we did to come up with our answer, and write it down. These steps can be anywhere in the spectrum of pseudocode—notation that looks like programming, but does not obey any formal rules of syntax—to pure natural language (_e.g._, English) that you are comfortable with. The important thing here is not any particular notation, but to have a clear idea of what you did in a step-by-step fashion before you try to generalize the steps.

For example, we might write the following:

### I found the intersection of

**left: -2**

**bottom: 1**

**right: 6**

**top: 3**

and

**left: -1**

**bottom: -1**

**right: 4**

**top: 4**

### by making a rectangle with

**left: -1**

**bottom: 1**

**right: 4**

**top: 3**

In this case, we do not have many steps, but it is still crucial for us to write them down.