from sys import stdin

count = int(input())

def check_result(arr):
    sum_vps = 0
    if sum(vps) == 0:
        for i in range(len(vps)):
            sum_vps += vps[i]
            if sum_vps > 0:
                return 'NO'
    else:
        return 'NO'

    return 'YES'

for i in range(count):
    vps = list(stdin.readline().strip())

    for j in range(len(vps)):
        vps[j] = -1 if vps[j] == '(' else 1

    print(check_result(vps))
