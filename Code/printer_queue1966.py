def check_number(arr, num):
    answer = 1
    while True:
        if arr[0] == max(arr):
            if 0 != num:
                answer += 1
                arr.pop(0)
                num = num - 1 if num != 0 else len(arr)-1
            else:
                return answer

        else:
            arr.append(arr.pop(0))
            num = num - 1 if num != 0 else len(arr)-1



count = int(input())
for i in range(count):
    inputs = input().split(' ')
    necessity = list(map(int, input().split(' ')))

    index = int(inputs[1])

    print(check_number(necessity, index))



