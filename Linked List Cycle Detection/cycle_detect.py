""" Linked List Cycle Detection """

class ListNode:
    """
    List Node class
    """
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def has_cycle(head):
    """
    Check whether there is cycle
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
