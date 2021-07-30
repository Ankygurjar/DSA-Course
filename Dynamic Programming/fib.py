

def fib(n: int) -> int: # Simple Rrcursion for Finding the Fibonacci
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)



n = 10

memo = [-1] * (n + 1)


def fib2(n: int) -> int:
    if memo[n] == -1:
        res = 0
        if n == 0 or n == -1:
            return n
        else:
            res = fib(n - 1) + fib(n - 2)
        memo[n] = res
    return memo[n]














