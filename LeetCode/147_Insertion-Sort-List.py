'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
'''
# book version (python algorithm inverview)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cursor = node = ListNode(None)
        while head:
            while cursor.next and cursor.next.val < head.val:
                cursor = cursor.next
            cursor.next, head.next, head = head, cursor.next, head.next
            cursor = node
        return node.next

# my version
class Solution:
    def __init__(self):
        self.prev = None
    def insertionSortList(self, head: ListNode) -> ListNode:
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
