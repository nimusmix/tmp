import sys
sys.stdin = open('sample_input (6).txt')

T = int(input())

def bfs(s, g, N):
    visited = [0] * (N+1)
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        v = queue.pop(0)
        if v == g:
            return visited[v] - 1
        for w in adjList[v]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v]+1
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjList = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G, V)}')