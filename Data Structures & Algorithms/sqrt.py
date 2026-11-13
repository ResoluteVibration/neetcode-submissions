def sqrt(n=None,x=None):
  if n is None:
    n = 1
  if x is None:
    x = n
  next = (x+(n/x))/2

  if abs(next-x) < 0.000001:
    print(next)
  else:
    return sqrt(n,next)

sqrt()
