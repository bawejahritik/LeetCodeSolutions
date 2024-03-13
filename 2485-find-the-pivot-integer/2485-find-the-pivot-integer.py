class Solution:
    def pivotInteger(self, n: int) -> int:
        left = sum(range(1, n+1))
        right = 0
        
        while left != 0:
            print(left, right)
            right = right + n
            if left == right:
                return n
            left = left-n
            n -= 1
        
        return -1