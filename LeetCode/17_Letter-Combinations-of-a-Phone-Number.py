'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
                   5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
                   8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        visited = []
        if len(digits) == 0: return visited
        def dfs(*positions):
            current = ''.join([letters[positions[i][0]][positions[i][1]] for i in range(len(positions))])
            visited.append(current)
            for i in range(len(positions)):
                new_position = positions  # [ (number, index), ... ]
                length = len(letters[new_position[i][0]])-1
                origin_pos = new_position[i][1]
                for new_pos in [min(origin_pos + 1, length), max(origin_pos - 1, 0)]:
                    new_position[i][1] = new_pos
                    cand = ''.join([letters[new_position[i][0]][new_position[i][1]] for i in range(len(new_position))])
                    if cand not in visited:
                        dfs(*new_position)

        dfs(*[[int(n), 0] for n in digits])
        return visited
