def is_match(s: str, p: str) -> bool:
    if p == '*':
        return True
    n = len(s)
    for i in range(n):
        if s[i] != p[i] and p[i] != '?':
            if p[i] != '*':
                return False
            if p[i] == '*':
                ind = p.rindex('*')
                if ind == n-1:
                    return True
                if s[i + 1] != p[ind + 1]:
                    return False
    return True





    ...
