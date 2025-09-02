def solution_station_1(n: int) -> int:
  """
  Given an integer n, returns the nth Fibonacci number.
  Uses an iterative approach for efficiency with large n.
  """
  if n <= 0:
    return 0
  if n == 1:
    return 1

  a, b = 0, 1
  for _ in range(2, n + 1):
    a, b = b, a + b

  return b