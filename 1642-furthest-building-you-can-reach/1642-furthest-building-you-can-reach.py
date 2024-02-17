class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jump_pq = []
        for i in range(len(heights)-1):
            jump_height = heights[i+1] - heights[i]
            if jump_height <= 0:
                continue
            heappush(jump_pq, jump_height)
            if len(jump_pq) > ladders:
                bricks -= heappop(jump_pq)
            if bricks < 0:
                return i
        return len(heights)-1
                