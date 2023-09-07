def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    c = 0
    for i in brackets_row:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        if c == -1:
            return False
    return c == 0

    ...  # реализовать проверку скобочной группы


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets("(()())"))
