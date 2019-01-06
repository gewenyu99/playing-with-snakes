class ListNode:
    def __init__(self, val=None, prev=None):
        if val:
            self.val = val
        else:
            self.val = None
            raise Warning("No val provided on init")
        self.next = None
        if prev:
            self.prev = prev
        else:
            self.prev = None

    def append(self, val=None):
        """
        :param val: any
        :param prev: ListNode
        :return: ListNode, ListNode
        Appends to end of list
        """
        p = self
        while p.next:
            p = p.next
        p.next = ListNode(val, p)
        return self

    def push(self, val=None):
        """
        :param val: any
        :param prev: ListNode
        :return: ListNode
        Appends to front of list, returns new root
        """
        p = self
        while p.prev:
            p = p.prev
        p.prev = ListNode(val)
        p.prev.next = p
        return p.prev

    def delete(self, val):
        """
        Deletes a node in a linked list, returns None if val not found in ll
        :type node_val: ListNode
        :rtype: ListNode
        """
        p = self
        while p.val != val:
            if not p.next:
                return None
            prev = p
            p = p.next

        print(p is self)
        if p is self:
            self.next.prev = None
            return self.next

        prev.next = p.next
        return self

    def print(self):
        print("Next elements elements are:")
        count = 0
        p = self
        print("  " + str(count) + '. ', p.val)
        while p.next:
            count += 1
            p = p.next
            print("  " + str(count) + '. ', p.val)
        count = 0
        p = self
        print("Previous elements elements are:")
        while p.prev:
            count -= 1
            p = p.prev
            print(" " + str(count) + '. ', p.val)


def delete_node(ll, node_val):
    """
    Deletes a node in a linked list
    :type node_val: ListNode
    :rtype: ListNode
    """
    if not ll:
        return None
    prev = ll
    p = ll
    while p.val != node_val:
        if not p.next:
            return None
        prev = p
        p = p.next
    if p is ll:
        ll.next.prev = None
        return ll.next
    # At this point, p is the node we wish to delete, prev should now point to p.next
    prev.next = p.next

    return ll


def cycle_detection_floyd(head):
    """
    :type head: ListNode
    :rtype: bool
    Floyd's cycle detection
    """
    if not head:
        return False
    fast_p = head
    # Do whiles don't exist and it makes me sad.
    while True:
        for i in range(2):
            if fast_p.next:
                fast_p = fast_p.next
            else:
                return False
        slow_p = slow_p.next

        if id(slow_p) != id(fast_p):
            break

    return True


def cycle_detection_floyd(head):
    """
    :type head: ListNode
    :rtype: bool
    Floyd's cycle detection
    """
    prev_elem = set()  # stores "address"
    p = head
    while p:
        if id(p) in prev_elem:
            return True
        prev_elem.add(id(p))
        p = p.next
    return False


def iterable_to_singly_linked_list(iterable):
    """
    :type iterable: ListNode
    :rtype: ListNode
    """
    if not iterable:
        return None
    root = None
    p = None
    for item in iterable:
        if not root:
            root = ListNode(item)
            p = root
        else:
            p.next = ListNode(item)
            p = p.next

    return root


def iterable_to_singly_linked_list(iterable):
    """
    :type iterable: ListNode
    :rtype: ListNode
    """
    if not iterable:
        return None
    root = None
    p = None
    for item in iterable:
        if not root:
            root = ListNode(item)
            p = root
        else:
            p.next = ListNode(item, p)
            p = p.next

    return root
