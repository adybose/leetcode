# Leetcode problem #206 https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # iterative approach
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            previous = None # this will be the last node of the reversed linked list

            # we iterate over the linked list starting from the head till the pointer to the next node exists
            # a linked list is referred to by its head element
            while head:
                # set a temporary variable to store the current node and use that to set node.previous
                temp = head
                # iterate to the next node by shifting the head to the next node of the current head
                head = head.next
                temp.next = previous
                previous = temp
            
            return previous
