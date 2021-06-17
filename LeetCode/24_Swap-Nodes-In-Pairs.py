'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        root = rev = ListNode(0)
        while head and head.next:
            pair = ListNode(head.next.val, ListNode(head.val))
            rev.next = pair
            rev = rev.next.next
            head = head.next.next
        if head is not None:
            rev.next = head
        return root.next
