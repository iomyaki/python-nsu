# Subtask #1
def first_n_fib(n):
    """
    :param n: number of Fibonacci sequence's elements, int (natural)
    :return: first n elements of Fibonacci sequence, list
    """

    fibs = [0, 1]

    if n < 1:
        return 'Incorrect input'
    elif n == 1:
        return fibs[0]
    elif n == 2:
        return fibs
    else:
        for i in range(2, n):
            fibs.append(fibs[i - 1] + fibs[i - 2])
        return fibs


# Subtask #2
def nth_fib(n):
    """
    :param n: number of an element in Fibonacci sequence, int
    :return: n-th element of Fibonacci sequence, int
    """

    def recursive_fib(m):
        if m <= 1:
            return [0, 1]
        else:
            previous, nxt = recursive_fib(m - 1)
            return [nxt, previous + nxt]

    return recursive_fib(n)[0]


print(*first_n_fib(13))
print(nth_fib(2))
