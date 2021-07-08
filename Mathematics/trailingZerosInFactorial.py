'''
  The program computes the number of trailing zeros in a factorial of a number.
  Algorithm:
  1. Initialize a result variable as result = 0
  2. Start a while loop with a condition i <= n
  3. result = result + (n/i)
  4. increement i by i = i*5
  5. Return result
  Time Complexity of the algorithm is Theta(logn)
'''

def TrailingZeros(n):
  result = 0
  while i <= n:
    result = result + int(n/1)
    i = i*5
  return result
