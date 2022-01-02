from collections import deque


n = int(input())

actions = [input() for _ in range(n)]

book_stack = deque()

for action in actions:
    if "BUY " in action:
        book_stack.append(action[4:])
    elif action == "READ":
        print(book_stack.pop())
