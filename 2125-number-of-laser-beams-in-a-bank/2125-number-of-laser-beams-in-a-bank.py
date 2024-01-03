class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_beams = 0
        last = 0
        
        for row in bank:
            temp = 0
            for i in row:
                if i == "1":
                    temp += 1
            
            total_beams = total_beams + last*temp
            if temp != 0:
                last = temp
        
        
        return total_beams