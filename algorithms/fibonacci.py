"""Create algorithm Fibonacci"""

n = int(input("Введи 'n'\n"))

def fib_naive(n):
    """
    Function for calculation num fibonacci.
    This func is not good for elapsed time
    """
    if n <= 1:
        return n
    else:
        return fib_naive(n - 1) + fib_naive(n - 2)

print(fib_naive(n))