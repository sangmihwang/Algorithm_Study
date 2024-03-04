import sys
import heapq
input = sys.stdin.readline
       
heap = []
N = int(input())
for _ in range(N):
    n = int(input())
    if n == 0:
        if heap:
            x = heapq.heappop(heap)
            print(x)
        else:
            print(0)
    else:
        heapq.heappush(heap, n)