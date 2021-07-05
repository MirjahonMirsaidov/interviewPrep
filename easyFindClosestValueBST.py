# Average: O(log(n)) time and space
# Worst: O(n) time and space
# recursive implementation
# def find_closest(tree, target):
#     return helper(tree, target, tree.root)
#
#
# def helper(tree, target, closest):
#     # if tree has not child nodes return current closest value
#     if tree is None:
#         return closest
#     # if current node value is closer, define it closest
#     if abs(tree.value - target) < abs(closest - target):
#         closest = tree.value
#
#     # if current node is greater than target, this means closer values are right side of the tree
#     if tree.value > target:
#         return helper(tree.right, target, closest)
#     elif tree.value < target:
#         return helper(tree.left, target, closest)
#     else:
#         return closest


# Average: O(log(n)) time / O(1) space
# Worst: O(n) time / O(1) space
# iterative implementation
def find_closest(tree, target):
    # current node
    current = tree
    closest = tree.value
    # while current node has child nodes
    while current:
        # if current node is closer, define it closest
        if abs(current.value - target) < abs(closest - target):
            closest = current.value
        # if current node is greater than target, this means right side of the tree is closer to target
        if current.value > target:
            current = current.right
        elif current.value < target:
            current = current.left
        else:
            break
    return closest
