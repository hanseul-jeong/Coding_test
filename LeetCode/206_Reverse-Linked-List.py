'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''

# recursive way
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        def reverse(head: ListNode, rev: ListNode) -> ListNode:
            if head is not None:
                rev, rev.next, head = head, rev, head.next
                return reverse(head, rev)
            return rev
        return reverse(head, rev)

# iterative way
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev
