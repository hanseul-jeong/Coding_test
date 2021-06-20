'''

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # remove empty linked lists
        lists = [l for l in lists if l is not None]
        if lists == [] : return None
        root = ListNode(-10001)
        for j in lists:
            # initialize
            if root.val == -10001: 
                root = j
                continue
            i = root
            if i.val > j.val:
                i, j = j, i
            root = i
            prev = ListNode(0, root)
            while j:
                if i is None or i.val > j.val:
                    i, j = j, i
                prev.next = i
                prev = prev.next
                i = i.next
        return root
