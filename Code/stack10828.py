count = int(input())
stack = []

def check_command():
    string = input()
    if string == 'pop':
        run_pop()
        return
    elif string == 'size':
        run_size()
        return
    elif string == 'empty':
        run_empty()
        return
    elif string == 'top':
        run_top()
        return

    splited = string.split(' ')
    if splited[0] == 'push':
        run_push(int(splited[1]))
        return


def run_pop():
    if len(stack) == 0:
        print(-1)
        return
    print(stack.pop())

def run_size():
    print(len(stack))

def run_empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def run_top():
    if len(stack) == 0:
        print(-1)
        return
    print(stack[-1])


def run_push(num):
    stack.append(num)

for i in range(1, count + 1):
    check_command()