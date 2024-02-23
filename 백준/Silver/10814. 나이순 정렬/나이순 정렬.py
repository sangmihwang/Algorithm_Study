import sys
input = sys.stdin.readline

N = int(input())
members = []
for i in range(N):
    age, name = map(str, input().strip().split())
    members.append([name, int(age), i]) 
members.sort(key=lambda x: (x[1], x[2]))

for i in range(N):
    print(members[i][1], members[i][0])