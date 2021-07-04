import random


def merge_sort(li):
    if len(li) <= 1:
        return li

    left_half, right_half = split(li)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(li):
    mid = len(li) // 2
    left_half = li[:mid]
    right_half = li[mid:]

    return left_half, right_half


def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


l = [72, 87, 42, 52, 7, 80, 93, 77, 63, 91]
print(l)
list = merge_sort(l)
print(list)

def test(li):
    n = len(li)

    if n == 0 or n == 1:
        return True
    else:
        return li[0] < li[1] and test(li[1:])

print(test(l))
print(test(list))