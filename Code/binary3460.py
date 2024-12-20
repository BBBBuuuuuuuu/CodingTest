count = int(input())
arr = [int(input()) for i in range(count)]

for i in range(count):
    binaryNum = bin(arr[i]).removeprefix('0b')[::-1]

    position = 0
    for char in binaryNum:
        if char == '1':
            print(position, '', end='')
        position += 1