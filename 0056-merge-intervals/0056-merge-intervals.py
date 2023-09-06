class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        
        intervals.sort()
        
        while i<len(intervals)-1:
            s1 = intervals[i][0]
            e1 = intervals[i][1]
            s2 = intervals[i+1][0]
            e2 = intervals[i+1][1]
            
            if e1>=s2:
                s1=min(s1, s2)
                e1=max(e1, e2)
                intervals.pop(i+1)
                intervals[i][0] = s1
                intervals[i][1] = e1
            else:
                i+=1
        
        return intervals
            