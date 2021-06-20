'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
# two pointer way
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        max_length = 1
        i,j = 0, 0
        while i < len(s)-1:
            max_length = (j+1 - i) if (j+1 - i) > max_length else max_length 
            if j < len(s)-1 and s[j+1] not in [s[idx] for idx in range(i, j+1)]: j+=1
            else:
                i += 1
        return max_length


# previous
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        queue = deque([(i, 1) for i in range(len(s)-1)])
        max_length = 1
        while queue:
            top_idx, n_words = queue.popleft()
            max_length = max_length if n_words < max_length else n_words
            if top_idx + n_words == len(s): continue
            if s[top_idx + n_words] not in [st for st in s[top_idx:top_idx+n_words]]:
                queue.append((top_idx, n_words+1))
        return max_length
