'''
Python program to find the factorial of a number
  Create a recursive funtion that runs till n becomes zero and add n to n - 1 in every iteration
'''

def factorial( n ):
  if n == 0:
    return 0
  return n * factorial(n-1)

factorial(4) # => 24
