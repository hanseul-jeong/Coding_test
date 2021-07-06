'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        def getDepth(node, depth):
            if not node: return depth
            left = getDepth(node.left, depth+1)
            right = getDepth(node.right, depth + 1)
            if self.flag and (left - right < -1 or left - right > 1):
                self.flag = False
                return depth
            return left if left > right else right
        getDepth(root, 0)
        return self.flag
