from typing import Optional

from neetcode.LinkedList import ListNode, create_linked_list_structure, print_linked_list


def reorder_list(head: Optional[ListNode]):
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    start_right_part = slow.next
    slow.next = None

    second_part_reversed, current = None, start_right_part
    while current:
        var = current.next
        current.next = second_part_reversed
        second_part_reversed = current
        current = var

    current_first, current_second = head, second_part_reversed

    while current_second:
        first_next, second_next = current_first.next, current_second.next
        current_first.next = current_second
        current_second.next = first_next
        current_first, current_second = first_next, second_next

    return head


if __name__ == '__main__':
    inputs = [
        [1],
        [1, 12],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
    ]
    for input_ in inputs:
        print(print_linked_list(reorder_list(create_linked_list_structure(input_))))
