from typing import List


def missing_number(nums: List[int]) -> int:
    n = len(nums)
    res = [0 for _ in range(n + 1)]
    for num in nums:
        res[num] += 1
    return res.index(0)
    ...
