from collections import deque


string = input()
brackets = deque()
for char in string:
    if char in "()":
        brackets.append(char)

if brackets.count("(") != brackets.count(")"):
    print("ERROR")
elif all(char == "(" for char in list(brackets)[:len(brackets) // 2]):
    print("OK")
else:
    print("ERROR")
