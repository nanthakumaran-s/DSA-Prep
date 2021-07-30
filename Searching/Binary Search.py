# O(log(n)) time | O(1) space
def binarySearchIterative(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
    return -1

# O(log(n)) time | O(log(n)) space
def binarySearchRecursive(array, target):
    binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearchHelper(array, target, left, mid - 1)
    elif array[mid] < target:
        return binarySearchHelper(array, target, mid + 1, right)