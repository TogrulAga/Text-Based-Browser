from collections import deque


n = int(input())

stack = deque()

for _ in range(n):
    operation = input()
    if "PUSH" in operation:
        stack.append(int(operation.split("PUSH ")[1]))
    else:
        stack.pop()

print(*[stack.pop() for _ in range(len(stack))], sep="\n")
