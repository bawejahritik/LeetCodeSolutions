class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for i, j in prerequisites:
            graph[i].append(j)
        
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            
            if graph[course] == []:
                return True
            
            visiting.add(course)
            
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            
            graph[course] = []
            
        
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True