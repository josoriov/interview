"""
LeetCode 19. Remove Nth Node From End of List

Approach:
- Use a dummy node before head to simplify edge cases (e.g. removing
  the head itself).
- Advance a "fast" pointer n steps ahead of a "slow" pointer.
- Move both forward together until fast reaches the end; slow will
  then be right before the node to remove.
- Bypass the target node by updating slow.next.

Time: O(L) — single pass over the list of length L
Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # sentinel to handle head-removal cleanly
    dummy = ListNode(0, head)
    # will end up just before the target node
    to_remove = dummy
    # will be n steps ahead of slow
    first = dummy

    # Move fast n+1 steps ahead so the gap between slow and fast is n nodes
    for _ in range(n + 1):
        first = first.next

    # Advance both pointers until fast falls off the end
    while first:
        to_remove = to_remove.next
        first = first.next

    # slow.next is the node to remove — bypass it
    to_remove.next = to_remove.next.next

    # real head (may have changed if n == len)
    return dummy.next    


def list_to_ll(vals: list) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def ll_to_list(head: ListNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test 1: [1,2,3,4,5], n=2 → [1,2,3,5]
head1 = list_to_ll([1, 2, 3, 4, 5])
print(ll_to_list(removeNthFromEnd(head1, 2)))

# Test 2: [1], n=1 → []
head2 = list_to_ll([1])
print(ll_to_list(removeNthFromEnd(head2, 1)))

# Test 3: [1,2], n=1 → [1]
head3 = list_to_ll([1, 2])
print(ll_to_list(removeNthFromEnd(head3, 1)))
