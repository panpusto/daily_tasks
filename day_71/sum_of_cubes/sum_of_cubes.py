def sum_cubes(n: int) -> int:
    return sum(num ** 3 for num in range(1, n+1))
