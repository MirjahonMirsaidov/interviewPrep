def binary_search(values, target):
    first = 0
    last = len(values) - 1

    while first <= last:
        midpoint = (first + last)//2
        if values[midpoint] == target:
            return midpoint
        elif values[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return None

list = []
for i in range(2):
    list.append(i)

print(binary_search(list, 1))