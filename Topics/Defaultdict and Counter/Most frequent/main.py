from collections import Counter


text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

n = int(input())

print(*[tup[0] + " " + str(tup[1]) for tup in Counter(text.split()).most_common(n)], sep="\n")
