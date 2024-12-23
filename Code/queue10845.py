from sys import stdin

count = int(input())
queue = []

for i in range(count):
    command = stdin.readline().strip()

    if command not in ['pop', 'size', 'empty', 'front', 'back']:
        print(command)
        command = command.split(' ')
        if command[0] == 'push':
            queue.append(command[1])

    if command == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
