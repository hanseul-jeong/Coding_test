'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        parents = deque([root])
        childs = deque([])
        d = 0
        while parents:
            tmp = deque([])
            for i in range((2 ** d)):
                p = parents.popleft()
                tmp.appendleft(p)   # reverse
                if p is None:
                    childs.extend([None, None])
                else:
                    childs.extend([p.left, p.right])
            if all([t is None for t in tmp]): break
            parents = tmp
            tmp = childs
            for i in range(-1, -((2 ** (d+1)) + 1), -2):
                if not parents: break
                p = parents.popleft()
                if not p: continue
                left, right = childs[i], childs[i-1]
                p.left, p.right = left, right
            parents = tmp
            d+= 1
        return root
