from itertools import combinations

nums = [3, 5, 7, 11, 13]
nums_len = 5

count = 0

def checkprime(sum_arr):
    a = sum_arr**0.5
    for i in range(2, int(a)+1):
        if sum_arr%i == 0:
            return False
    return True

for arr in combinations(nums, 3):
    print(sum(arr))
    if checkprime(sum(arr)):
        count+=1

print(count)

