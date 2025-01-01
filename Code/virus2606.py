from sys import stdin

def print_answer(arr):
    for current in arr:
        if 1 in current:
            return current

    return None

count_computers = stdin.readline().strip()

count_networks = int(stdin.readline().strip())
networks = []

for i in range(count_networks):
    connect = set(map(int, stdin.readline().strip().split(' ')))
    networks.append(connect)
stack = []

while networks:
    network = networks.pop()
    temp_stack = []
    merged = False

    for i in stack:
        if i & network:
            networks.append(i | network)
            merged = True
        else:
            temp_stack.append(i)

    if merged:
        stack = temp_stack
    else:
        stack.append(network)

answer = print_answer(stack)
print(len(answer)-1) if answer is not None else print(0)

