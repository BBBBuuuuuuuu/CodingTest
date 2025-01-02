from collections import deque


def bfs(start, end):
    queue = deque([start])
    visited = [False] * 100002
    if start == end:
        return 0
    count = 1
    while True:
        temp = deque([])
        for num in queue:
            for current in (num*2, num+1, num-1):
                if 0 <= current<= 100001 and not visited[current]:
                    temp.append(current)
                    visited[current] = True
        if end in temp:
            return count
        else:
            queue = temp
            count += 1
position = list(map(int, input().split(' ')))
print(bfs(position[0], position[1]))