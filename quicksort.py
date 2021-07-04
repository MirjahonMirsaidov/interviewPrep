import random


def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for i in values[1:]:
        if i < pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


list = [random.randint(1, 100) for i in range(10)]
print(list)
print(quicksort(list))