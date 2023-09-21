from typing import List


def maximum_gap(nums: List[int]) -> int:
    li = sorted(nums)
    n = 0
    for i in range(len(li) - 1):
        s = li[i + 1] - li[i]
        if s > n:
            n = s
    return n


    ...