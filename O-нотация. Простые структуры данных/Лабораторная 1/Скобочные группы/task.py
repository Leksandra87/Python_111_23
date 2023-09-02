def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    while "()" in brackets_row:
        brackets_row = brackets_row.replace("()", "")
    return brackets_row == ""

    ...  #  реализовать проверку скобочной группы


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets("(()())"))