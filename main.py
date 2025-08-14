def sorting(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sorting(left) + middle + sorting(right)

testcases = [[4,1, 5, 0, 10], [1, 5, 3, 2, 5]]
print([sorting(tc) for tc in testcases])