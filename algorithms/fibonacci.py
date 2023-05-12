from array import array
"""Create algorithm Fibonacci"""

n = int(input("Введи 'n'\n"))

def fib_naive(n):
    """
    Function for calculation num fibonacci.
    This func is not good for elapsed time (recursion)
    """
    if n <= 1:
        return n
    else:
        return fib_naive(n - 1) + fib_naive(n - 2)

print(fib_naive(n))

def fib_effective(n):
    """
    This func is fast
    """
    f = []
    f.insert(0, 0)
    f.insert(1, 1)
    f.insert(2, 1)
    if n <= 1:
        return n
    else:
        for i in range(2, n):
            f[1], f[2] = f[2], f[1] + f[2]
        return f[2]

print(fib_effective(n))