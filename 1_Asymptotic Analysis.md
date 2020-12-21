
## What is Asymptotic Analysis ?

The study of change in performance of the algorithm with the change in the order of the input size is defined as asymptotic analysis.

## What is Asymptotic Notations ?

>The efficiency of an algorithm depends on the amount of time, storage and other resources required to execute the algorithm. The efficiency is measured with the help of asymptotic notations.


> Asymptotic notations are the mathematical notations used to describe the running time of an algorithm when the input tends towards a particular value or a limiting value.


### The time required by an algorithm comes under three types:

- Worst case: It defines the input for which the algorithm takes a huge time.

- Average case: It takes average time for the program execution.

- Best case: It defines the input for which the algorithm takes the lowest time


#### For example:- 

In bubble sort, when the input array is already sorted, the time taken by the algorithm is linear i.e. the best case.

But, when the input array is in reverse condition, the algorithm takes the maximum time (quadratic) to sort the elements i.e. the worst case.

When the input array is neither sorted nor in reverse order, then it takes average time. These durations are denoted using asymptotic notations.
rithm running time.

<h1 class="h1">Asymptotic Analysis</h1>
<p>As we know that data structure is a way of organizing the data efficiently and that efficiency is measured either in terms of time or space. So, the ideal data structure is a structure that occupies the least possible time to perform all its operation and the memory space. Our focus would be on finding the time complexity rather than space complexity, and by finding the time complexity, we can decide which data structure is the best for an algorithm.</p>
<p>The main question arises in our mind that on what basis should we compare the time complexity of data structures?. The time complexity can be compared based on operations performed on them. Let's consider a simple example.</p>
<p>Suppose we have an array of 100 elements, and we want to insert a new element at the beginning of the array. This becomes a very tedious task as we first need to shift the elements towards the right, and we will add new element at the starting of the array.</p>

<p>Suppose we consider the linked list as a data structure to add the element at the beginning. The linked list contains two parts, i.e., data and address of the next node. We simply add the address of the first node in the new node, and head pointer will now point to the newly added node. Therefore, we conclude that adding the data at the beginning of the linked list is faster than the arrays. In this way, we can compare the data structures and select the best possible data structure for performing the operations.</p>
<h3 class="h3">How to find the Time Complexity or running time for performing the operations?</h3>
<p>The measuring of the actual running time is not practical at all. The running time to perform any operation depends on the size of the input. Let's understand this statement through a simple example.</p>
<p>Suppose we have an array of five elements, and we want to add a new element at the beginning of the array. To achieve this, we need to shift each element towards right, and suppose each element takes one unit of time. There are five elements, so five units of time would be taken. Suppose there are 1000 elements in an array, then it takes 1000 units of time to shift. It concludes that time complexity depends upon the input size.</p>
<p>Therefore, if the input size is n, then f(n) is a function of n that denotes the time complexity.</p>
<h3 class="h3">How to calculate f(n)?</h3>
<p>Calculating the value of f(n) for smaller programs is easy but for bigger programs, it's not that easy. We can compare the data structures by comparing their f(n) values. We can compare the data structures by comparing their f(n) values. We will find the growth rate of f(n) because there might be a possibility that one data structure for a smaller input size is better than the other one but not for the larger sizes. Now, how to find f(n).</p>
<p>Let's look at a simple example.</p>
<p>f(n) = 5n<sup>2</sup> + 6n + 12</p>
<p>where n is the number of instructions executed, and it depends on the size of the input.</p>
<p>When n=1</p>
<p>% of running time due to 5n<sup>2</sup> = <img src="https://static.javatpoint.com/ds/images/data-structure-asymptotic-analysis1.png" alt="Asymptotic Analysis"> * 100 = 21.74%</p>
<p>% of running time due to 6n = <img src="https://static.javatpoint.com/ds/images/data-structure-asymptotic-analysis1_2.png" alt="Asymptotic Analysis"> * 100 = 26.09%</p>
<p>% of running time due to 12 = <img src="https://static.javatpoint.com/ds/images/data-structure-asymptotic-analysis1_3.png" alt="Asymptotic Analysis"> * 100 = 52.17%</p>
<p>From the above calculation, it is observed that most of the time is taken by 12. But, we have to find the growth rate of f(n), we cannot say that the maximum amount of time is taken by 12.  Let's assume the different values of n to find the growth rate of f(n).</p>
<table class="alt">
    <tbody><tr>
        <td>n</td>
        <td>5n<sup>2</sup></td>
        <td>6n</td>
		<td>12</td>
    </tr>
    <tr>
        <td>1</td>
        <td>21.74%</td>
        <td>26.09%</td>
		<td>52.17%</td>
    </tr>
  <tr>
        <td>10</td>
        <td>87.41%</td>
        <td>10.49%</td>
		<td>2.09%</td>
    </tr>
  <tr>
        <td>100</td>
        <td>98.79%</td>
        <td>1.19%</td>
		<td>0.02%</td>
    </tr>
  <tr>
        <td>1000</td>
        <td>99.88%</td>
        <td>0.12%</td>
		<td>0.0002%</td>
    </tr>
</tbody></table>
<p>As we can observe in the above table that with the increase in the value of n, the running time of 5n<sup>2</sup> increases while the running time of 6n and 12 also decreases. Therefore, it is observed that for larger values of n, the squared term consumes almost 99% of the time. As the n<sup>2</sup> term is contributing most of the time, so we can eliminate the rest two terms.</p>
<p><strong>Therefore,</strong></p>
<p>f(n) = 5n<sup>2</sup></p>
<p>Here, we are getting the approximate time complexity whose result is very close to the actual result. And this approximate measure of time complexity is known as an Asymptotic complexity. Here, we are not calculating the exact running time, we are eliminating the unnecessary terms, and we are just considering the term which is taking most of the time.</p>
<p>In mathematical analysis, asymptotic analysis of algorithm is a method of defining the mathematical boundation of its run-time performance. Using the asymptotic analysis, we can easily conclude the average-case, best-case and worst-case scenario of an algorithm.</p>
<p>It is used to mathematically calculate the running time of any operation inside an algorithm.</p>
<p><strong>Example:</strong> Running time of one operation is x(n) and for another operation, it is calculated as f(n2). It refers to running time will increase linearly with an increase in 'n' for the first operation, and running time will increase exponentially for the second operation. Similarly, the running time of both operations will be the same if n is significantly small.</p>
<p>Usually, the time required by an algorithm comes under three types:</p>
<p><strong>Worst case:</strong> It defines the input for which the algorithm takes a huge time.</p>
<p><strong>Average case:</strong> It takes average time for the program execution.</p>
<p><strong>Best case:</strong> It defines the input for which the algorithm takes the lowest time</p>
<h3 class="h3">Asymptotic Notations</h3>
<p>The commonly used asymptotic notations used for calculating the running time complexity of an algorithm is given below:</p>
<ul class="points">
<li>Big oh Notation (?)</li>
<li>Omega Notation (Ω)</li>
<li>Theta Notation (θ)</li>
</ul>
<h3 class="h3">Big oh Notation (O)</h3>
<ul class="points">
<li>Big O notation is an asymptotic notation that measures the performance of an algorithm by simply providing the order of growth of the function.</li>
<li>This notation provides an upper bound on a function which ensures that the function never grows faster than the upper bound. So, it gives the least upper bound on a function so that the function never grows faster than this upper bound.</li>
</ul>
<p>It is the formal way to express the upper boundary of an algorithm running time. It measures the worst case of time complexity or the algorithm's longest amount of time to complete its operation. It is represented as shown below:</p>
<img src="https://static.javatpoint.com/ds/images/data-structure-asymptotic-analysis.png" alt="Asymptotic Analysis">
<p><strong>For example:</strong></p>
<p>If <strong>f(n)</strong> and <strong>g(n)</strong> are the two functions defined for positive integers,</p>
<p>then <strong>f(n)</strong> = <strong>O(g(n))</strong> as <strong>f(n) is big oh of g(n)</strong> or f(n) is on the order of g(n)) if there exists constants c and no such that:</p>
<p><strong>f(n)≤c.g(n) for all n≥no</strong></p>
<p>This implies that f(n) does not grow faster than g(n), or g(n) is an upper bound on the function f(n). In this case, we are calculating the growth rate of the function which eventually calculates the worst time complexity of a function, i.e., how worst an algorithm can perform.</p>
<p><strong>Let's understand through examples</strong></p>
<p>Example 1: f(n)=2n+3 , g(n)=n</p>
<p>Now, we have to find <strong>Is f(n)=O(g(n))?</strong></p>
<p>To check f(n)=O(g(n)), it must satisfy the given condition:</p>
<p><strong>f(n)&lt;=c.g(n)</strong></p>
<p>First, we will replace f(n) by 2n+3 and g(n) by n.</p>
<p>2n+3 &lt;= c.n</p>
<p>Let's assume c=5, n=1 then</p>
<p>2*1+3&lt;=5*1</p>
<p>5&lt;=5</p>
<p>For n=1, the above condition is true.</p>
<p>If n=2</p>
<p>2*2+3&lt;=5*2</p>
<p>7&lt;=10</p>
<p>For n=2, the above condition is true.</p>
<p>We know that for any value of n, it will satisfy the above condition, i.e., 2n+3&lt;=c.n. If the value of c is equal to 5, then it will satisfy the condition 2n+3&lt;=c.n. We can take any value of n starting from 1, it will always satisfy. Therefore, we can say that for some constants c and for some constants n0, it will always satisfy 2n+3&lt;=c.n. As it is satisfying the above condition, so f(n) is big oh of g(n) or we can say that f(n) grows linearly. Therefore, it concludes that c.g(n) is the upper bound of the f(n). It can be represented graphically as:</p>
<img src="https://static.javatpoint.com/ds/images/data-structure-asymptotic-analysis2.png" alt="Asymptotic Analysis">
<p>The idea of using big o notation is to give an upper bound of a particular function, and eventually it leads to give a worst-time complexity. It provides an assurance that a particular function does not behave suddenly as a quadratic or a cubic fashion, it just behaves in a linear manner in a worst-case.</p>
<h3 class="h3">Omega Notation (Ω)</h3>
<ul class="points">
<li>It basically describes the best-case scenario which is opposite to the big o notation.</li>
<li>It is the formal way to represent the lower bound of an algorithm's running time. It measures the best amount of time an algorithm can possibly take to complete or the best-case time complexity.</li>
<li>It determines what is the fastest time that an algorithm can run.</li>
</ul>
<p>If we required that an algorithm takes at least certain amount of time without using an upper bound, we use big- Ω notation i.e. the Greek letter "omega". It is used to bound the growth of running time for large input size.</p>
<p>If <strong>f(n)</strong> and <strong>g(n)</strong> are the two functions defined for positive integers,</p>
<p>then <strong>f(n) = Ω (g(n))</strong> as <strong>f(n) is Omega of g(n)</strong> or f(n) is on the order of g(n)) if there exists constants c and no such that:</p>
<p><strong>f(n)&gt;=c.g(n) for all n≥no and c&gt;0</strong></p>
<p><strong>Let's consider a simple example.</strong></p>
<p>If f(n) = 2n+3, g(n) = n,</p>
<p>Is f(n)= <strong>Ω</strong> (g(n))?</p>
<p>It must satisfy the condition:</p>
<p><strong>f(n)&gt;=c.g(n)</strong></p>
<p>To check the above condition, we first replace f(n) by 2n+3 and g(n) by n.</p>
<p><strong>2n+3&gt;=c*n</strong></p>
<p>Suppose c=1</p>
<p><strong>2n+3&gt;=n</strong> (This equation will be true for any value of n starting from 1).</p>
<p>Therefore, it is proved that g(n) is big omega of 2n+3 function.</p>
<img src="https://static.javatpoint.com/ds/images/data-structure-asymptotic-analysis3.png" alt="Asymptotic Analysis">
<p>As we can see in the above figure that g(n) function is the lower bound of the f(n) function when the value of c is equal to 1. Therefore, this notation gives the fastest running time. But, we are not more interested in finding the fastest running time, we are interested in calculating the worst-case scenarios because we want to check our algorithm for larger input that what is the worst time that it will take so that we can take further decision in the further process.</p>
<h3 class="h3">Theta Notation (θ)</h3>
<ul class="points">
<li>The theta notation mainly describes the average case scenarios.</li>
<li>It represents the realistic time complexity of an algorithm. Every time, an algorithm does not perform worst or best, in real-world problems, algorithms mainly fluctuate between the worst-case and best-case, and this gives us the average case of the algorithm.</li>
<li>Big theta is mainly used when the value of worst-case and the best-case is same.</li>
<li>It is the formal way to express both the upper bound and lower bound of an algorithm running time.</li>
</ul>
<p>Let's understand the big theta notation mathematically:</p>
<p>Let f(n) and g(n) be the functions of n where n is the steps required to execute the program then:</p>
<p><strong>f(n)= θg(n)</strong></p>
<p>The above condition is satisfied only if when</p>
<p><strong>c1.g(n)&lt;=f(n)&lt;=c2.g(n)</strong></p>
<p>where the function is bounded by two limits, i.e., upper and lower limit, and f(n) comes in between. The condition <strong>f(n)= θg(n)</strong> will be true if and only if c1.g(n) is less than or equal to f(n) and c2.g(n) is greater than or equal to f(n). The graphical representation of theta notation is given below:</p>
<img src="https://static.javatpoint.com/ds/images/data-structure-asymptotic-analysis4.png" alt="Asymptotic Analysis">
<p>Let's consider the same example where<br>
f(n)=2n+3<br>
g(n)=n<br>
</p>
<p>As c1.g(n) should be less than f(n) so c1 has to be 1 whereas c2.g(n) should be greater than f(n) so c2 is equal to 5. The c1.g(n) is the lower limit of the of the f(n) while c2.g(n) is the upper limit of the f(n).</p>
<p>c1.g(n)&lt;=f(n)&lt;=c2.g(n)</p>
<p>Replace g(n) by n and f(n) by 2n+3</p>
<p>c1.n &lt;=2n+3&lt;=c2.n</p>
<p>if c1=1, c2=2, n=1</p>
<p>1*1 &lt;=2*1+3 &lt;=2*1</p>
<p><strong>1</strong> &lt;= <strong>5</strong> &lt;= <strong>2</strong> // for n=1, it satisfies the condition c1.g(n)&lt;=f(n)&lt;=c2.g(n)</p>
<p><strong>If n=2</strong></p>
<p>1*2&lt;=2*2+3&lt;=2*2</p>
<p>2&lt;=7&lt;=4 // for n=2, it satisfies the condition c1.g(n)&lt;=f(n)&lt;=c2.g(n)</p>
<p>Therefore, we can say that for any value of n, it satisfies the condition c1.g(n)&lt;=f(n)&lt;=c2.g(n). Hence, it is proved that f(n) is big theta of g(n). So, this is the average-case scenario which provides the realistic time complexity.</p>
<h3 class="h3">Why we have three different asymptotic analysis?</h3>
<p>As we know that big omega is for the best case, big oh is for the worst case while big theta is for the average case. Now, we will find out the average, worst and the best case of the linear search algorithm.</p>
<p>Suppose we have an array of n numbers, and we want to find the particular element in an array using the linear search. In the linear search, every element is compared with the searched element on each iteration. Suppose, if the match is found in a first iteration only, then the best case would be Ω(1), if the element matches with the last element, i.e., nth element of the array then the worst case would be O(n). The average case is the mid of the best and the worst-case, so it becomes <strong>θ(n/1). The constant terms can be ignored in the time complexity so average case would be θ(n)</strong>.</p>
<p>So, three different analysis provide the proper bounding between the actual functions. Here, bounding means that we have upper as well as lower limit which assures that the algorithm will behave between these limits only, i.e., it will not go beyond these limits.</p>
<h3 class="h3">Common Asymptotic Notations</h3>
<table class="alt">
    <tbody><tr>
        <td>constant</td>
        <td>-</td>
        <td>?(1)</td>
    </tr>
    <tr>
        <td>linear</td>
        <td>-</td>
        <td>?(n)</td>
    </tr>
    <tr>
        <td>logarithmic</td>
        <td>-</td>
        <td>?(log n)</td>
    </tr>
    <tr>
        <td>n log n</td>
        <td>-</td>
        <td>?(n log n)</td>
    </tr>
    <tr>
        <td>exponential</td>
        <td>-</td>
        <td>2?(n)</td>
    </tr>
    <tr>
        <td>cubic</td>
        <td>-</td>
        <td>?(n3)</td>
    </tr>
    <tr>
        <td>polynomial</td>
        <td>-</td>
        <td>n?(1)</td>
    </tr>
    <tr>
        <td>quadratic</td>
        <td>-</td>
        <td>?(n2)</td>
    </tr>
</tbody></table>



