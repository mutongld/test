class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    tmp = ListNode(0)
    ret = tmp

    while l1 and l2:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    if l1 is not None:
        tmp.next = l1
    elif l2 is not None:
        tmp.next = l2
    
    return ret.next

if __name__ == "__main__":
    pass