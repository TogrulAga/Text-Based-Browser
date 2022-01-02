from collections import deque

n = int(input())

my_stack = deque()

[my_stack.append(input()) for _ in range(n)]

print(*[my_stack.pop() for _ in range(n)], sep="\n")
