class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(curr_amt, noOfCoins):
            if curr_amt in memo:
                return memo[curr_amt]

            if curr_amt == amount:
                return 0
            ans = inf
            for coin in coins:
                if coin <= amount-curr_amt:
                    ans = min(ans, dfs(curr_amt+coin, noOfCoins+1)+1)
            memo[curr_amt] = ans
            return ans

        res = dfs(0, 0)
        return res if res!=inf else -1   