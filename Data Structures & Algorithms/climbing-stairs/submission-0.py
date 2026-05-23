class Solution:
    def climbStairs(self, n: int) -> int:
        def memoization(i, cache):
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i in cache.keys():
                return cache[i]

            cache[i] = memoization(i - 1, cache) + memoization(i - 2, cache)
            return cache[i]
        return memoization(n, {})