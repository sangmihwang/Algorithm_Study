def solution(n, costs):
    parent = [i for i in range(n)]      # parent[i]는 i의 부모 노드

    def find(node):
        while parent[node] != node:
            node = parent[node]
        return node

    def union(x, y):
        parent[find(y)] = find(x)   # y의 헤드노드의 부모를 x의 헤드노드로(두 가지를 합침)
        return
    
    costs.sort(key=lambda x: x[2])
    ans = 0
    # print(costs)
    for b1, b2, cost in costs:
        if find(b1) != find(b2):
            union(b1, b2)
            ans += cost

    return ans