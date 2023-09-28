def num_decodings(s: str) -> int:
    if not s or int(s[0]) == 0:
        return 0
    num = len(s)
    var = 1
    if num < 2 and int(s) != 0:
        return var
    for i in range(num - 1):
        val = s[i] + s[i + 1]
        if int(val[0]) != 0 and 0 < int(val) < 27:
            var += 1
    if int(s[-1]) == 0:
        var -= 1
    return var

    ...


if __name__ == '__main__':
    print(num_decodings('101'))
