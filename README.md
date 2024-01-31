What is binary search?

Usually, when we search for a target element in an array of numbers, the simple approach would be to go through every element in the array with a time complexity of (O(n)). 

However, if these elements are sorted, we are able to take advantage of this privilege to bring down the search time to O(log n). For example, if we want to scan 100 elements, the worst-case scenario would be 10 searches. That can be a great performance improvement while performing operations.

Pictorially, binary search can be depicted below-


![1EYkSkQaoduFBhpCVx7nyEA](https://user-images.githubusercontent.com/33410914/203827425-b16a0806-db92-459a-84b9-cf36802a365a.gif)


In the first diagram, the mid element of the sorted array is 23. Now, as our target element is 37 which is greater than 23, the search will move to the right where again it will search the mid element which is 41. As 41 > 37, the search function goes to the left where it is able to find our target element within 3 steps. 

In the second diagram, for sequential search, the search function will scan through all elements in the array until it reaches the target element. The steps involved in finding it are 11. This is where binary search comes to the rescue.

The reason behind this huge performance boost is that for each search iteration, we are able to slice the elements we will be looking at in half. Fewer elements to look at corresponds to faster search times. This all comes from the simple fact that in a sorted list, everything to the right of n will be greater or equal to it, and vice versa.
