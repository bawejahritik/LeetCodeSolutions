class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        ans.append([1])
        
        if numRows==1:
            return ans
        
        ans.append([1,1])
        
        if numRows==2:
            return ans
        
        for i in range(2, numRows):
            temp = [1]
            for j in range(0, len(ans[i-1])-1):
                temp.append(ans[i-1][j]+ans[i-1][j+1])
            temp.append(1)
            ans.append(temp)
        
        
        return ans