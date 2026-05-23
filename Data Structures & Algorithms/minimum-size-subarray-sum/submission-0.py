class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0
        length = float("inf")

        for R in range(len(nums)):
            total += nums[R]
            #Always not going to execute!
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1 #Let's shrink window until we find min len subarray
        return 0 if length == float("inf") else length