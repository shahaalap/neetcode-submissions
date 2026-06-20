# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid of linked list

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #reverse from mid to end
        prev = slow
        cur = slow.next

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        last = prev

        slow.next = None

        while head and last:
            if head == slow or last == slow:
                break

            hnext = head.next
            lnext = last.next

            head.next = last
            last.next = hnext

            head = hnext
            last = lnext
       
