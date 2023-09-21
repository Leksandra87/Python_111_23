from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set([num for num in nums1 if num in nums2]))



    ...
