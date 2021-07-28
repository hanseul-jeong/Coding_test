'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
'''

# It could't remove overlapped case
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def cal(lefts):
            x, op, y = lefts
            if op == '-':
                return x-y
            elif op == '+':
                return x+y
            elif op == '*':
                return x*y
            else:
                return x/y

        results = []
        queue = deque([[int(e) if i%2 == 0 else e for i, e in enumerate(expression)]])
        while queue:
            left = queue.popleft()
            if len(left) == 1:
                results.append(left[0])
                continue
            for idx in range(0, len(left)-1, 2):
                queue.append(left[:idx] + [cal(left[idx:idx+3])] + left[idx+3:])
        return results
