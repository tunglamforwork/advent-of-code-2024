# Part 1
# with open("input.txt", "r") as file:
#     left = []
#     right = []
#     for pair in file:
#         left_col, right_col = pair.split(",")
#         left.append(int(left_col.strip()))
#         right.append(int(right_col.strip()))

#     left.sort()
#     right.sort()

#     result = sum([abs(int(a) - int(b)) for a, b in zip(left, right)])
#     print(result)


# Part 2
from collections import Counter

with open("input.txt", "r") as file:
    left = []
    right = []
    for pair in file:
        left_col, right_col = pair.split(",")
        left.append(int(left_col.strip()))
        right.append(int(right_col.strip()))

    left_counter = Counter(left)
    right_counter = Counter(right)
    result = 0
    for val in left:
        if val not in right:
            continue
        tmp = val * right_counter[val]
        result += tmp

    print(result)
