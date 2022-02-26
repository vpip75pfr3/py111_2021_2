def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 1:
        return n
    chislo_1 = 0
    chislo_2 = 1
    for i in range(n):
        chislo_fib = chislo_1 + chislo_2
        chislo_1 = chislo_2
        chislo_2 = chislo_fib
    return chislo_fib


def fib_generator(n: int):
    if n == 1:
        return n
    chislo_1 = 0
    chislo_2 = 1

    for i in range(n):
        chislo_fib = chislo_1 + chislo_2
        chislo_1 = chislo_2
        chislo_2 = chislo_fib
        yield chislo_fib


if __name__ == '__main__':
    # print(fib_recursive(10))
    print(fib_iterative(5))
    x = fib_generator(5)
    for n in x:
        print(n)
