def is_subsequence(s: str, t: str) -> bool:
    if not s:
        return True
    sl = list(s)
    tl = list(t)
    for _ in range(len(t)):
        res = tl.pop()
        if res == sl[-1]:
            sl.pop()
        if not sl:
            break
    return not sl

    ...
