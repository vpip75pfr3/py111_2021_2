def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n == 1:
        return n
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factorial_gen(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n == 1:
        return n
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact


if __name__ == '__main__':
    print(factorial_recursive(6))
    print(factorial_iterative(6))
    fact = factorial_gen(6)
    for num in fact:
        print(num)
