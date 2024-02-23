class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-stone for stone in stones]
        heapify(new_stones)

        while len(new_stones) > 1:
            h1 = -heappop(new_stones)
            h2 = -heappop(new_stones)
            
            if h1 == h2:
                continue
            else:
                h1 -= h2
                heappush(new_stones, -h1)
        
        return -new_stones[0] if len(new_stones) == 1 else 0