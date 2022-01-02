from collections import Counter


elements = list(Counter(input().lower().split()).elements())
elements.sort()
print(elements)
