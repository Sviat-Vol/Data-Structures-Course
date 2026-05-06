""" Merge Two Sorted Lists """

class ListNode:
    """
    List Node class
    """
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def merge_two_lists(l1, l2):
    """
    Merge two sorted lists
    """
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next
