# -*- coding: utf-8 -*-
"""binary search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QIxd-N8Yx129Y4ZCRTmMZNIZun_bfYiH

Binary Search in python

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. Runtime complexity should be O(log n)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        
        return -1

"""You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = 1
        
        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid) == False:
                left = mid+1
            else:
                right = mid-1
                result = mid
                
        return result

"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  Runtime complexity should be O(log n)"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l<=r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        
        return l