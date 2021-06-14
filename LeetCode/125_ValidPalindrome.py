'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # leave only alphabets and numbers
        alpha_str = [st.lower() for st in s if st.isalpha() or st.isnumeric()]
        for i in range(len(alpha_str) // 2):
            if alpha_str[i] != alpha_str[-(i + 1)]:
                return False
        return True
