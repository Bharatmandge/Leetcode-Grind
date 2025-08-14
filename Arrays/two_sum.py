# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#Example 1:
'''
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
'''
#here is the solution 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashmap = {}
       for index, number in enumerate(nums):
           complement = target - number
           if complement in hashmap:
              return [hashmap[complement], index]
           hashmap[number] = index
           
           
'''
This is the structured and fastest answer to leetcode Two sum problem so you can try
and test according to you 
'''