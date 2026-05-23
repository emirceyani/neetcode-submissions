class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1 , max(piles)
        res = R
        while L <= R:
            mid =  (R + L) //2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if h >= totalTime:
                res = mid
                R = mid - 1
            else:
                L = mid + 1
        return res

        