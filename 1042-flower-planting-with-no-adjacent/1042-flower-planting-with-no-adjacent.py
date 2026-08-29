class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

            
        for a, b in paths:
            a = a - 1
            b = b - 1
            graph[a].append(b)
            graph[b].append(a)    
        ans = [0] * n   
        for i in range(n):        
            used = set()
            for j in graph[i]:

                if ans[j] != 0:
                    used.add(ans[j])

            # Try flowers 1, 2, 3, 4
            for flower in range(1, 5):

                if flower not in used:
                    ans[i] = flower
                    break

        return ans
