def SearchInsert(number,target):
    left = 0
    right = len(number) - 1

    while left <= right :
        mid = (left + right) // 2

        if number[mid] == target:
            return mid
        elif number [mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(SearchInsert([1,3,5,6], 5))