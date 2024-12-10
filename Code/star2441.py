count = int(input())

for i in range(1, count+1):
    print(' '*(i-1) + '*'*(count-i+1))