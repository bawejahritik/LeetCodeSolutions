class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
            if count == len(digits) and count != 0:
                res.append("".join(path))
                return
            if count == 0 and count==len(digits):
                return
            
            for letter in KEYBOARD[digits[count]]:
                dfs(count+1, path+[letter])
                
        
        res = []
        dfs(0, [])
        return res