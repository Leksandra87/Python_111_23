from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """
    n = len(nums)
    while n > 1:
        flag = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                flag = False
        n -= 1
        if flag:
            break

    ...
