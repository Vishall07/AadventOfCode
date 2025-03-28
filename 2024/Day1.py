f = open("day1input.txt", "r")
# part 1
left = []
right = []
for x in f:
    data = x.split('   ')
    left.append(int(data[0]))
    right.append(int(data[1]))

left.sort()
right.sort()

res = 0
for i in range(len(left)):
    diff = abs(left[i] - right[i])
    res += diff

print(res)

# Part 2
memo = {}

for num in right:
    if(num in memo):
        memo[num] =  memo[num] + 1
    else:
        memo[num] = 1

res = 0
for num in left:
    if(num in memo):
        res += (num * memo[num])

print(res)