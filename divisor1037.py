count = int(input())
divisors = input()

arr = list(map(int, divisors.split()))
print(min(arr)*max(arr))