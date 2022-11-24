What is binary search?

Usually, if we want to to find a target element in a group like as an array of numbers, the simple apporach would be go through every single element in the array with time complexity of (O(n)). 

However, if these elements are sorted, we are able to take the advantage of this privilege to bring down the search time to O(log n). For example, if we want to scan 100 elements, the worst case scenario would be 10 searches. That can be a great performance improvement while performing operations.

Pictorically, binary search can be depicted below-

![image](https://user-images.githubusercontent.com/33410914/203826136-b1d71b16-92b0-4fc9-98cb-c2af5a105bc1.png)


The reason behind this huge performance boost is because for each search iterations, we are able to slice the elements we will be looking at in half. Fewer elements to look at = faster search time. And this all comes from the simple fact that in a sorted list, everything to the right of n will be greater or equal to it, and vice versa.
