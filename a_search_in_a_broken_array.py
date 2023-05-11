# ID: 87120645


def broken_search(nums, target, lf=0, r=None) -> int:
    r = r or len(nums) - 1

    if r < lf:
        return -1
    mid = (lf + r) // 2
    if nums[mid] == target:
        return mid

    if nums[lf] <= nums[mid]:
        if nums[lf] <= target < nums[mid]:
            return broken_search(nums, target, lf, mid)
        return broken_search(nums, target, mid + 1, r)

    if nums[mid] < target <= nums[r]:
        return broken_search(nums, target, mid + 1, r)
    return broken_search(nums, target, lf, mid)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [100, 101, 1, 4, 5, 7, 12, 19, 21]
    assert broken_search(arr, 5) == 4
    arr = [5, 1]
    assert broken_search(arr, 1) == 1
    arr = [5, 1]
    assert broken_search(arr, 6) == -1
    arr = [3, 5, 6, 7, 9, 1, 2]
    assert broken_search(arr, 4) == -1
    arr = [1]
    assert broken_search(arr, 1) == 0
    arr = [1, 2, 3, 5, 6, 7, 9, 0]
    assert broken_search(arr, 3) == 2
    arr = [3271, 3298, 3331, 3397, 3407, 3524, 3584, 3632, 3734, 3797, 3942,
           4000, 4180, 4437, 4464, 4481, 4525, 4608, 4645, 4803, 4804, 4884,
           4931, 4965, 5017, 5391, 5453, 5472, 5671, 5681, 5959, 6045, 6058,
           6301, 6529, 6621, 6961, 7219, 7291, 7372, 7425, 7517, 7600, 7731,
           7827, 7844, 7987, 8158, 8169, 8265, 8353, 8519, 8551, 8588, 8635,
           9209, 9301, 9308, 9336, 9375, 9422, 9586, 9620, 9752, 9776, 9845,
           9906, 9918, 16, 25, 45, 152, 199, 309, 423, 614, 644, 678, 681, 725,
           825, 830, 936, 1110, 1333, 1413, 1617, 1895, 1938, 2107, 2144, 2184,
           2490, 2517, 2769, 2897, 2970, 3023, 3112, 3156]
    assert broken_search(arr, 25) == 69
