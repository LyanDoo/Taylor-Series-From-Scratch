PI = 3.14159265359

def factorial(n):
  if (n == 1.0 or n == 0.0):
    return 1.0
  else:
    return n * factorial(n-1.0)

def deg_to_radian(deg):
  return (deg*(PI/180.0))

def sine(deg,n_terms=200):
  deg = deg_to_radian(deg)
  result = 0.0
  for i in range(n_terms):
    i = float(i)
    result += (((-1.0)**i)*(deg**((2.0*i)+1.0))/factorial((2.0*i)+1.0))
  return result
