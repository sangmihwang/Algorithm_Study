import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
# dict = {}
for i in range(N):
    pokemon = input().strip()
    lst.append(pokemon)
    # dict[i+1] = pokemon
dict = {k:v for k, v in enumerate(lst)}
dictR = {v:k for k, v in enumerate(lst)}
for _ in range(M):
    ques = input().strip()
    if ques.isdecimal():
        print(dict[int(ques)-1])
    else:
        print(dictR[ques]+1)
