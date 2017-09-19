from collections import Counter
# Opdracht 2.1
tuple = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
c = Counter(tuple)
print(sorted(c.items()))
