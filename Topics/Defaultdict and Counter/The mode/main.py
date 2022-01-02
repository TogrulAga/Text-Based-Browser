from collections import Counter


data = input().split()

print(Counter(data).most_common(1)[0][0])
