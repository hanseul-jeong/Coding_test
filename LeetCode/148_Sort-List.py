'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''
# merge sort (linked list)
class Solution:
    def __init__(self):
        self.stack = []
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        half, slow, fast = None, head, head
        while fast and fast.next:
            half = slow
            slow = slow.next
            fast = fast.next.next
        left, right = head, half.next
        half.next = None
        l1 = self.sortList(left)
        l2 = self.sortList(right)
        return self.mergesort(l1, l2)

    def mergesort(self, left, right):
        root, l, r = ListNode(-1), left, right
        node = root
        while l and r:
            if l.val < r.val:
                node.next = l
                l = l.next
            else:
                node.next = r
                r = r.next
            node = node.next
        node.next = l if not r else r
        return root.next


# previous -> It exceeds time limit
class Solution:
    def __init__(self):
        self.prev = None
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return head
        def merge(prev, left):
            if not left: 
                self.prev = prev
                return None
            if prev.val > left.val:
                merge(ListNode(left.val, prev), left.next)
            else:
                pivot = prev
                while pivot:
                    if not pivot.next or pivot.next.val > left.val: 
                        tmp = pivot.next
                        pivot.next = ListNode(left.val)
                        pivot.next.next = tmp
                        break
                    pivot = pivot.next
                merge(prev, left.next)
            return prev

        merge(ListNode(head.val), head.next)
        return self.prev
