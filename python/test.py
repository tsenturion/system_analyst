# что делает этот код?
from itertools import permutations

data = input()

numbers = data.split(",")

unique_perms = set(permutations(numbers))

for perm in unique_perms:
    print("".join(perm))