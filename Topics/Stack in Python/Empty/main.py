from collections import deque

# please don't change the following line
candy_bag = deque(input().split())

# your code here
n = int(input())
stack = [input() for _ in range(n)]

for action in stack:
    if action == "TAKE":
        try:
            print(candy_bag.pop())
        except IndexError:
            print("We are out of candies :(")
    elif "PUT" in action:
        candy_bag.append(action.split("PUT ")[1])
