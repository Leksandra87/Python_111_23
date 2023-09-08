from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for ind_1, num_1 in enumerate(nums):
        num_2 = target - num_1
        seq = nums[ind_1 + 1:]
        if num_2 in seq:
            ind_2 = seq.index(num_2) + ind_1 + 1
            return [ind_1, ind_2]


