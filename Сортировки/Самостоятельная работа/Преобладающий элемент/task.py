from typing import List


def majority_element(nums: List[int]) -> int:
    maj_elem = None
    counter = 0
    for num in nums:
        if counter == 0:
            maj_elem = num
            counter += 1
        else:
            if num == maj_elem:
                counter += 1
            else:
                counter -= 1
    return maj_elem


    ...
