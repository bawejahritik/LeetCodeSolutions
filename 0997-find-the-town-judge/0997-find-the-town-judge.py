class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        graph = {}
        children = set()
        for a, b in trust:
            graph[b] = [a] + graph.get(b, [])
            children.add(a)
        
        for key, val in graph.items():
            if len(val) == n-1 and key not in children:
                return key

        return -1