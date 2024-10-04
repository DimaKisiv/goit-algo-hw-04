def tim_sort_iterative(arr):
    # Initialize the minimum run size
    min_run = 32

    # Find the length of the array
    n = len(arr)

    # Traverse the array and do insertion sort on each segment of size min_run
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, (n - 1)))

    # Start merging from size min_run, doubling the size on each iteration
    size = min_run
    while size < n:
        # Divide the array into merge_size
        for start in range(0, n, size * 2):
            # Find the midpoint and endpoint of the left and right subarrays
            midpoint = start + size
            end = min((start + size * 2 - 1), (n - 1))

            # Merge the two subarrays if within bounds
            if midpoint < end:
                merged_array = merge(arr[start:midpoint], arr[midpoint:end + 1])
                arr[start:start + len(merged_array)] = merged_array

        # Increase the merge size for the next iteration
        size *= 2

    return arr


def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    # Traverse through array from left to right
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key_item, to one position ahead
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key_item

    return arr


def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements of left (if any)
    result.extend(left[i:])

    # Append remaining elements of right (if any)
    result.extend(right[j:])

    return result