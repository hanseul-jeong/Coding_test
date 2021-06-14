'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''

class Solution:

    def is_palindrome(self, word):
        return word == word[::-1]
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = s[0]
        if len(s) == 1: return max_palindrome
        queue = deque([])
        # find minimum palindrome
        for i in range(len(s)-1):
            if self.is_palindrome(s[i:i+2]): queue.append((i,i+2))
            if i < len(s)-2 and self.is_palindrome(s[i:i+3]): queue.append((i,i+3))
        while queue:
            left, right = queue.popleft()
            if len(max_palindrome) < right - left:
                max_palindrome = s[left:right]
            left -= 1
            right += 1
            if left < 0 or right > len(s) : continue
            if self.is_palindrome(s[left:right]):
                queue.append((left, right))

        return max_palindrome
