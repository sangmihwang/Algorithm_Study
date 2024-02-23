## 백준_ 1018_ 체스판 다시 칠하기

import sys
input = sys.stdin.readline

def solW(arr):
    cnt = 0   # 첫 항을 W로 했을 때
    for i in range(0, 8, 2):    # 홀수 행
        for j in range(8):
            if j % 2 == 0:       # 홀수 열
                if arr[i][j] == 'B':
                    cnt += 1
            else:               # 짝수 열
                if arr[i][j] == 'W':
                    cnt += 1
    for i in range(1, 8, 2):     # 짝수 행
        for j in range(8):
            if j % 2 == 0:       # 홀수 열
                if arr[i][j] == 'W':
                    cnt += 1
            else:               # 짝수 열
                if arr[i][j] == 'B':
                    cnt += 1
    return cnt

def solB(arr):
    cnt = 0         # 첫 항을 B로 했을 때
    for i in range(0, 8, 2):    # 홀수 행
        for j in range(8):
            if j % 2 == 0:       # 홀수 열
                if arr[i][j] == 'W':
                    cnt += 1
            else:               # 짝수 열
                if arr[i][j] == 'B':
                    cnt += 1
    for i in range(1, 8, 2):     # 짝수 행
        for j in range(8):
            if j % 2 == 0:       # 홀수 열
                if arr[i][j] == 'B':
                    cnt += 1
            else:               # 짝수 열
                if arr[i][j] == 'W':
                    cnt += 1
    return cnt

def makeBoard(x, y):
    newboard = []
    for i in range(x, x+8):
        newboard.append(board[i][y:y+8])
    return newboard

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

minV = 64
for i in range(N-7):
    for j in range(M-7):
        v = min(solW(makeBoard(i, j)), solB(makeBoard(i, j)))
        if v < minV:
            minV = v
print(minV)

