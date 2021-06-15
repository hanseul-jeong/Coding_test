'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if len(height) <= 2: return water
        left = -1
        prev_asc = True
        for i in range(1, len(height)):
            if height[i] - height[i-1] >= 0:    # ascending
                prev_asc = True
            else:   # descending
                if not prev_asc: continue   # continuous descending
                if left >=0:    # not a first time
                    level = min(height[left], height[i-1])
                    for iv in range(left, i-1):
                        water += max(level - height[iv], 0)
                left = i-1
                prev_asc = False
        level = min(height[left], height[-1])
        for iv in range(left, len(height)):
            water += max(level - height[iv], 0)
        return water
