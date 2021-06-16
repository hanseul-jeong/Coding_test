'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        if len(nums) < 2: return results
        for i in range(len(nums) - 2):
            # remove repetition
            if i > 0 and nums[i - 1] == nums[i]: continue
            left, right = i + 1, len(nums)-1
            while left < right:
                cand = [nums[i], nums[left], nums[right]]
                if sum(cand) == 0:
                    # remove repetition
                    if not ((left > i + 1 and nums[left - 1] == nums[left]) or (
                            right < len(nums)-1 and nums[right + 1] == nums[right])):
                        results.append(cand)
                if sum(cand) >= 0:
                    right -= 1
                else:
                    left += 1
        return results
