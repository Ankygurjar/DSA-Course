

def fib(n: int) -> int: # Simple Rrcursion for Finding the Fibonacci
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)



def dp(self, number, memo): #Memoization
    if memo[number] == -1:
        res = 0
        if number == 0 or number == 1:
            return number
        else:
            res = self.dp(number-1, memo) + self.dp(number-2, memo)
        memo[number] = res
    return memo[number]

def dp












