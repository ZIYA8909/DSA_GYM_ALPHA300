
fruits = [1, 2, 1, 2, 3]
start = 0
ans = 0

for end in range(len(fruits)):
    types=set()

    for i in range(start,end+1):
        types.add(fruits[i])

    while len(types)>2:
        start+=1
        types=set()

        for i in range(start,end+1):
            types.add(fruits[i])

    length=end-start+1

    if length>ans:
        ans=length

print(ans)
