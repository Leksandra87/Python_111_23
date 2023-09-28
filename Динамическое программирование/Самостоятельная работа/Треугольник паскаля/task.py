from typing import List


def generate(num_rows: int) -> List[List[int]]:
    res = [[1] * i for i in range(1, num_rows + 1)]
    if len(res) > 2:
        for i in range(2, len(res)):
            for j in range(1, len(res[i]) - 1):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res
    ...


if __name__ == '__main__':
    print(generate(5))
