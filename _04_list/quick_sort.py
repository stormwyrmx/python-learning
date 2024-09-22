def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 示例使用
arr = [21, 25, 21, 23, 22, 20, 31, 29, 33, 30]
sorted_arr = quicksort(arr)
print(sorted_arr)

