def solution_station_4(x: int) -> bool:
  """Return True if x is prime, else False."""
  if x < 2:
    return False
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      return False
  return True