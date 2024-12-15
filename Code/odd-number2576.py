arr=[]

for i in range(7):
    num = int(input())
    if num%2 == 1 :
        arr.append(num)

if arr.__len__()==0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))