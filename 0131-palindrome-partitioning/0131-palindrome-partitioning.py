class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(idx, path):
            if idx == len(s):
                res.append(path)
                return 
            
            for ei in range(idx+1, len(s)+1):
                prefix = s[idx:ei]
                if isPalindrome(prefix):
                    dfs(ei, path+[prefix])
        
        dfs(0, [])
        
        return res