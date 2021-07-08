'''
  Calculating GCD of two numbers
'''
# Simple Solution

def gcd(a, b):
  res = min(a, b)
  while res > 1:
    if a%res == 0 and b%res == 0:
      break
    res -= 1
  return res

# Using Euclidean Algorithm:

def gcdEA(a, b):
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a

# Optimized Version of Euclidean Algorithm:

def gcdOEA(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)
