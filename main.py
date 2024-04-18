def find_factors(n):
  factors = []
  for i in range(1, n):
    if n % i == 0:
      factors.append(i)
  return factors


def classify(n):
  if n <=0:
    raise ValueError("Classification is only possible for positive integers.")
  factors = find_factors(n)
  sum_factors = sum(factors)
  if sum_factors == n:
    return "perfect"
  elif sum_factors > n:
    return "abundant"
  else:
    return "deficient"

print(classify(6))
print(classify(12))
print(classify(15))