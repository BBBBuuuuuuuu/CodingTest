count = int(input())

for i in range(1, 2*count):
    if i<=count:
        print(' '*(count-i) + '*'*(2*i-1))
    else:
        print(' '*(i-count) + '*'*(2*(2*count-i)-1))