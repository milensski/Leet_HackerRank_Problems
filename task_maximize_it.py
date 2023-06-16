from math import pow
from itertools import product


n, m = map(int, input().split())

max_numbers = []

for _ in range(n):
    length, *numbers = map(int, input().split())

    max_numbers.append(pow(max(numbers), 2))

print(sum(max_numbers) % 1000)
