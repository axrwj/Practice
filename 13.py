from collections import deque
from typing import List, Optional


class AdjacencyMatrixGraph:
    def __init__(self, n_vertices: int):
        self.n = n_vertices
        self.matrix = [[False] * n_vertices for _ in range(n_vertices)]

    def add_edge(self, u: int, v: int):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.matrix[u][v] = True
            self.matrix[v][u] = True
        else:
            raise IndexError("Vertex index out of range")

    def bfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in range(self.n):
                if self.matrix[u][v] and not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return order

    def dfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        order = []

        def _dfs(u):
            visited[u] = True
            order.append(u)
            for v in range(self.n):
                if self.matrix[u][v] and not visited[v]:
                    _dfs(v)

        _dfs(start)
        return order

    def shortest_path(self, start: int, end: int) -> Optional[List[int]]:
        if start == end:
            return [start]
        visited = [False] * self.n
        parent = [-1] * self.n
        queue = deque([start])
        visited[start] = True

        while queue:
            u = queue.popleft()
            for v in range(self.n):
                if self.matrix[u][v] and not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    if v == end:
                        path = []
                        cur = end
                        while cur != -1:
                            path.append(cur)
                            cur = parent[cur]
                        return path[::-1]
                    queue.append(v)
        return None


class AdjacencyListGraph:
    def __init__(self, n_vertices: int):
        self.n = n_vertices
        self.adj = [[] for _ in range(n_vertices)]

    def add_edge(self, u: int, v: int):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.adj[u].append(v)
            self.adj[v].append(u)
        else:
            raise IndexError("Vertex index out of range")

    def bfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return order

    def dfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        order = []

        def _dfs(u):
            visited[u] = True
            order.append(u)
            for v in self.adj[u]:
                if not visited[v]:
                    _dfs(v)

        _dfs(start)
        return order

    def shortest_path(self, start: int, end: int) -> Optional[List[int]]:
        if start == end:
            return [start]
        visited = [False] * self.n
        parent = [-1] * self.n
        queue = deque([start])
        visited[start] = True

        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    if v == end:
                        path = []
                        cur = end
                        while cur != -1:
                            path.append(cur)
                            cur = parent[cur]
                        return path[::-1]
                    queue.append(v)
        return None


def main():
    n = 6
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5)]

    print("=" * 50)
    print("Граф:")
    print("Вершины: 0–5")
    print("Рёбра:", edges)
    print("=" * 50)

    print("\n[Матрица смежности]")
    g1 = AdjacencyMatrixGraph(n)
    for u, v in edges:
        g1.add_edge(u, v)

    print("BFS из 0:", g1.bfs(0))
    print("DFS из 0:", g1.dfs(0))
    print("Кратчайший путь 0 → 5:", g1.shortest_path(0, 5))

    print("\n[Список смежности]")
    g2 = AdjacencyListGraph(n)
    for u, v in edges:
        g2.add_edge(u, v)

    print("BFS из 0:", g2.bfs(0))
    print("DFS из 0:", g2.dfs(0))
    print("Кратчайший путь 0 → 5:", g2.shortest_path(0, 5))

    print("\n[Тест: отсутствие пути]")
    print("Путь 0 → 10 (несуществующая вершина):", "N/A")
    print("Путь между несвязными компонентами (если бы были):")
    g3 = AdjacencyListGraph(3)
    g3.add_edge(0, 1)
    print("Граф с рёбрами: [(0,1)], вершины: 0,1,2")
    print("Путь 0 → 2:", g3.shortest_path(0, 2))


if __name__ == "__main__":
    main()