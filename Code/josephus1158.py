inputs = input().split(' ')
n = int(inputs[0])
k = int(inputs[1])
last_index = k - 1

arr = [i+1 for i in range(n)]

josephus_arr = '<'
josephus_arr += str(arr.pop(last_index))

while arr:
    last_index = (last_index + k - 1) % len(arr)
    josephus_arr += ', ' + str(arr.pop(last_index% len(arr)))


josephus_arr += '>'
print(josephus_arr, end='')

