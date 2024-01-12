class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, dest in tickets}
        res = []
        for src, dest in tickets:
            adj[src].append(dest)
        
        for key in adj:
            adj[key].sort()
        
        
        def dfs(adj, res, src):
            if src in adj:
                destinations = adj[src][:]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, res, dest)
                    destinations = adj[src][:]
            res.append(src)
        
        dfs(adj, res, "JFK")
        res.reverse()
        
        return res
        