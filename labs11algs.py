def broken_search(nums, target) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
k = int(input("введите элемент: "))
print("Результат поиска:", broken_search(arr, k))
