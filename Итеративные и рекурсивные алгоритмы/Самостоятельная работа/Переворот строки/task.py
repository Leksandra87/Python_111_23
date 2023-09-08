from typing import List


def reverse_string(s: List[str]) -> None:
    l_ind = 0
    r_ind = len(s) - 1
    while l_ind < r_ind:
        s[l_ind], s[r_ind] = s[r_ind], s[l_ind]
        l_ind += 1
        r_ind -= 1
