class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq

        graph = {}

        for i in range(1, n + 1):
            graph[i] = []

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        visited = {}

        while heap:

            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited[node] = time

            for neighbor, weight in graph[node]:

                if neighbor not in visited:
                    heapq.heappush(heap, (time + weight, neighbor))

        if len(visited) != n:
            return -1

        return max(visited.values())