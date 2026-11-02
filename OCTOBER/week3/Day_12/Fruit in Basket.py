fruits = [1, 2, 1, 2, 3]

start = 0
ans = 0
count = {}

for end in range(len(fruits)):
    fruit = fruits[end]

    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

    while len(count) > 2:
        old = fruits[start]
        count[old] -= 1

        if count[old] == 0:
            del count[old]

        start += 1

    length = end - start + 1

    if length > ans:
        ans = length

print(ans)