from typing import List


def trap(height: List[int]) -> int:
    max_val = max(height)
    top = 0
    if height.count(max_val) > 1:
        l_max = height.index(max_val)
        r_max = len(height) - 1 - height[::-1].index(max_val)
        for i in range(l_max + 1, r_max):
            top += max_val - height[i]
    else:
        l_max = r_max = height.index(max_val)
    h = height[0]
    for i in range(1, l_max):
        if height[i] > h:
            h = height[i]
        elif height[i] < h:
            top += h - height[i]
    h = height[-1]
    for i in range(len(height) - 2, r_max, -1):
        if height[i] > h:
            h = height[i]
        elif height[i] < h:
            top += h - height[i]
    return top

    ...



