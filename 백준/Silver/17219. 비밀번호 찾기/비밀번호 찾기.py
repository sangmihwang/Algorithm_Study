import sys
input = sys.stdin.readline

N, M = map(int, input().split())
password = {}
for _ in range(N):
    url, pw = map(str, input().strip().split())
    password[url] = pw
for _ in range(M):
    que = input().strip()
    print(password[que])
