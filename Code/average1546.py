count = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

new_scores = [new_score/max_score*100 for new_score in scores]

print(sum(new_scores)/count)