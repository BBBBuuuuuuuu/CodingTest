def solution(priorities, location):
    answer = 1
    while True:
        if priorities[0] == max(priorities):
            if location != 0:
                priorities.pop(0)
                answer += 1
                location = location - 1
            else:
                return answer
        else:
            priorities.append(priorities.pop(0))
            location = location - 1 if location != 0 else len(priorities)-1

print(solution([1, 1, 9, 1, 1, 1], 0))