T = int(input())
for _ in range(T):
    word = input()
    K = int(input())

    # 각 문자의 위치 정보 저장
    position = {}
    for i, w in enumerate(word):
        if w in position:
            position[w].append(i)
        else:
            position[w] = [i]

    min_len = float('inf')
    max_len = -1

    for key, values in position.items():
        if len(values) >= K:
            for i in range(len(values) - K + 1):
                length = values[i + K - 1] - values[i] + 1
                min_len = min(min_len, length)
                max_len = max(max_len, length)

    if min_len == float('inf'):
        print(-1)
    else:
        print(min_len, max_len)
