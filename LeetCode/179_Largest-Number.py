'''
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''


class Solution:
    def is_x_bigger(self, x, y):
        return max(x+y, y+x) == x + y

    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        cur = [nums[0]]
        for n in nums[1:]:
            for i in range(len(cur)):
                if self.is_x_bigger(n, cur[i]):
                    cur = cur[:i] + [n] + cur[i:]
                    break
            if i == len(cur)-1: cur.append(n)
        return str(int(''.join(cur)))
