import unittest

from snakes.utils.linked_lists import ListNode


class TestListNode(unittest.TestCase):
    def test_empty(self):
        try:
            l = ListNode()
        except Warning as e:
            self.assertEqual(str(e), "No val provided on init")
            return
        self.fail('No exception was raised, expected Warning')

    def test_singly_linked_init(self):
        l = ListNode('val')
        self.assertEqual(l.val, 'val')
        self.assertEqual(l.next, None)
        self.assertEqual(l.prev, None)
        l.print()

    def test_doubly_linked_init(self):
        l = ListNode('val')
        l2 = ListNode('val2', l)
        l.next = l2
        self.assertEqual(l2.prev.val, 'val')
        self.assertIs(l2.prev.next, l2)
        self.assertEqual(l2.prev.prev, None)
        self.assertEqual(l2.val, 'val2')
        self.assertIs(l2.next, None)
        l.print()

    def test_push(self):
        l = ListNode('val')
        new_root = l.push('val-1')
        self.assertEqual(new_root.prev, None)
        self.assertEqual(new_root.val, 'val-1')
        self.assertEqual(new_root.next.val, l.val)
        self.assertIs(l.prev, new_root)

        new_new_root = l.push('val-2')
        self.assertEqual(new_new_root.prev, None)
        self.assertEqual(new_new_root.val, 'val-2')
        self.assertEqual(new_new_root.next.val, new_root.val)
        self.assertEqual(new_new_root.next.next.val, l.val)
        self.assertIs(l.prev.prev, new_new_root)
        # for your sanity
        l.print()

    def test_append(self):
        l = ListNode('val')
        l.append('val1')
        l.append('val2')
        l.append('val3')
        self.assertEqual(l.next.val, 'val1')
        self.assertIs(l.next.prev, l)
        self.assertEqual(l.next.next.val, 'val2')
        self.assertIs(l.next.next.prev, l.next)
        self.assertEqual(l.next.next.next.val, 'val3')
        self.assertIs(l.next.next.next.prev, l.next.next)
        self.assertEqual(l.next.next.next.next, None)

    def test_delete(self):
        l = ListNode('val')
        l.append('val1')
        l.append('val2')
        l.append('val3')
        l.delete('val2')
        self.assertEqual(l.val, 'val')
        self.assertEqual(l.next.val, 'val1')
        self.assertEqual(l.next.next.val, 'val3')
        l = l.delete('val')
        l.print()