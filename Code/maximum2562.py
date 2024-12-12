arr = []

for i in range(9):
    num = int(input())
    arr.append(num)

maximum = max(arr)
position = arr.index(maximum) + 1

print(maximum)
print(position)