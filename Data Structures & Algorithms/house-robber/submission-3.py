class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(n):
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])
            dp = [nums[0], max(nums[0], nums[1])]
            i=2
            while i < len(nums):
                tmp = dp[1]
                dp[1] = max(tmp, dp[0]+ nums[i])
                dp[0] = tmp
                i+=1
            return dp[1]
        return helper(len(nums))
                