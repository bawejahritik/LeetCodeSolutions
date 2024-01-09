class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        
        for src, dest in prerequisites:
            graph[dest].append(src)
            
        def find_indegree(graph):
            indegree = {node: 0 for node in range(numCourses)}

            for i in range(numCourses):
                for j in graph[i]:
                    indegree[j] += 1

            return indegree
        
        def topo_sort(graph):
            res = []
            q=deque()
            indegree = find_indegree(graph)
            for node in indegree:
                if indegree[node] == 0:
                    q.append(node)
            
            while len(q) > 0:
                node = q.popleft()
                res.append(node)
                
                for i in graph[node]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
            
            return res if len(graph) == len(res) else []
        
        
        return topo_sort(graph)
            