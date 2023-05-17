# ID: 87181808

from typing import List


def broken_search(nums: List[int], target: int, *args) -> int:
    left, right = args or (0, len(nums) - 1)

    if right < left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid

    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            return broken_search(nums, target, left, mid)
        return broken_search(nums, target, mid + 1, right)

    if nums[mid] < target <= nums[right]:
        return broken_search(nums, target, mid + 1, right)
    return broken_search(nums, target, left, mid)
