import random

SMALL = 1_000
MEDIUM = 100_000
LARGE = 1_000_000

def generate_random(n):
    return [random.randint(1, 1000000) for _ in range(n)]

def generate_sorted(n):
    return list(range(1, n + 1))

def generate_reverse_sorted(n):
    return list(range(n, 0, -1))
