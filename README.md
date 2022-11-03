# '<i>And Function</i>' Neural Network
I built this simple neural network for the Brandeis Univ. Quant Club to demonstrate how a network is created from the ground up. It has three main goals:

1) Show how one would provide a function to a neural network without explicitly writing the function out in math
2) Demonstrate how through multiple iterations a network can use the previous error to get closer to our expected outcome
3) Provide a clear understanding as to how we can use the final results the network provided us with

### What is it training on?
It's provided with three lists, where the first two are the conditions and the last is the outcome. Simply, it is the fact that two conditions must be met for the final condition to be true. For example: 

0 and 0 = 0 |
1 and 0 = 0 |
0 and 1 = 0 |
1 and 1 = 1

The network will understand that for the condition to be met, our outcome must be exactly 1. Visually, imagine a 1x1 graph where (0,0), (0,1), (1,0) and (1,1) are all plotted. Our final outcome would only be true if the data provided to us were to be at the location (1,1). This is what our neural network concludes. 

Food for thought: What larger implications does this hold? How would one approach a non-linear function? 

### Contact
It is probable that there is a mistake somewhere in this code. If you identify this mistake, please contact me directly at EphraimJZimmerman@gmail.com
