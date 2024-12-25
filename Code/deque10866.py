from sys import stdin

count = int(input())
deque = []

for i in range(count):
    command = stdin.readline().strip().split(' ')

    if command[0] == 'push_front':
        deque.insert(0, command[1])
    elif command[0] == 'push_back':
        deque.append(command[1])
    elif command[0] == 'pop_front':
        print(deque.pop(0)) if len(deque) != 0 else print(-1)
    elif command[0] == 'pop_back':
        print(deque.pop(-1)) if len(deque) != 0 else print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        print(1) if len(deque) == 0 else print(0)
    elif command[0] == 'front':
        print(deque[0]) if len(deque) != 0 else print(-1)
    elif command[0] == 'back':
        print(deque[-1]) if len(deque) != 0 else print(-1)
