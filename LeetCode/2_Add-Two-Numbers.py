'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addLinked(l1, l2, n_raise=0):
            # l1 and l2 is None
            if not (l1 or l2):
                # 올림이 있을 경우
                if n_raise != 0: return ListNode(n_raise)
                return l1
            if l1 is None: 
                l1, l2 = l2, l1
            t1 = 0 if l1 is None else l1.val
            t2 = 0 if l2 is None else l2.val
            cand = (t1 + t2 + n_raise)
            l1.val, n_raise = cand % 10, cand // 10
            l1_ = l1 if l1 is None else l1.next
            l2_ = l2 if l2 is None else l2.next
            l1.next = addLinked(l1_, l2_, n_raise)
            return l1
        return addLinked(l1, l2)
