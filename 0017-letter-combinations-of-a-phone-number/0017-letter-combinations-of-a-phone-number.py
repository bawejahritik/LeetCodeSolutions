class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        KEYBOARD = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
                    }
        
        def dfs(count, path):
            if count == len(digits):
                res.append("".join(path))
                return 
            
            for letter in KEYBOARD[digits[count]]:
                dfs(count+1, path+[letter])
                
        
        res = []
        dfs(0, [])
        return res