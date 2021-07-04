import random

from linked_list import LinkedList


def merge_sort(linked_list):
    if linked_list.size() == 1 or linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    if linked_list is None or linked_list.head is None:
        left, right = linked_list, None
    else:
        mid = linked_list.size()//2
        mid_node = linked_list.node_at_index(mid - 1)
        left = linked_list
        right = LinkedList()
        right.head = mid_node.next_node
        mid_node.next_node = None

    return left, right


def merge(left, right):
    new_linked_list = LinkedList()
    new_linked_list.add(0)
    current = new_linked_list.head

    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node
    new_linked_list.head = new_linked_list.head.next_node

    return new_linked_list


linked_list = LinkedList()

for i in range(11):
    linked_list.add(random.randint(1, 100))

print(linked_list)
print(merge_sort(linked_list))
