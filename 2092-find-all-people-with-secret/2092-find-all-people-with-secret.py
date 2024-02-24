class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))
        
        q = deque([(0, 0), (firstPerson, 0)])
        
        earliest = [float('inf')] * n
        
        earliest[0] = 0
        earliest[firstPerson] = 0
        
        while q:
            person, time = q.popleft()
            for t, n in graph[person]:
                if t >= time and earliest[n] > t:
                    earliest[n] = t
                    q.append((n, t))
        
        res = []
        
        for i, time in enumerate(earliest):
            if time != float('inf'):
                res.append(i)
        
        return res