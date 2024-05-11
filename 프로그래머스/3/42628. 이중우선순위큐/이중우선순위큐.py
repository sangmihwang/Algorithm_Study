import heapq

def solution(operations):
    answer = [0, 0]
    mx = []
    mn = []
    for o in operations:
        word, num = map(str, o.split())
        if word == 'I':
            heapq.heappush(mn, int(num))
            heapq.heappush(mx, (-int(num), int(num)))
        elif mx and word == 'D':
            if num == '1':
                val = heapq.heappop(mx)[1]
                mn.remove(val)
            else:
                val = heapq.heappop(mn)
                mx.remove((-val, val))
    if mn:
        answer[0] = heapq.heappop(mx)[1]
        answer[1] = heapq.heappop(mn)
    
    return answer