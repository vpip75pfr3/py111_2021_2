def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    open = 0
    for letter in brackets_row:
        if letter == ')':
            open -= 1
        elif letter == '(':
            open += 1
        if open < 0:
            return False
    return not bool(open)
