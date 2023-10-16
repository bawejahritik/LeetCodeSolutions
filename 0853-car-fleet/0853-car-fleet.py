class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        
        pairs.sort(reverse=True)
        
        for p, s in pairs:
            if stack:
                t1 = (target-stack[-1][0])/stack[-1][1]
                t2 = (target-p)/s
            if not (stack and t1>=t2):
                stack.append([p, s])
                
        
        return len(stack)