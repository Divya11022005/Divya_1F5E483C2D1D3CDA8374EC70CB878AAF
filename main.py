def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = 12
res = fact_rec(number)
print("The factorialof {} is {}.".format(number, res))