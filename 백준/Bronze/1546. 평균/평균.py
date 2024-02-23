N = int(input())
score = list(map(int, input().split()))
new = []
best = max(score)

for s in score:
    new.append(s/best*100)
print(sum(new)/len(score))
