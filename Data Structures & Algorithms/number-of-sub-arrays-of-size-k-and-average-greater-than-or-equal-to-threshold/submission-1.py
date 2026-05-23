class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        wsum = sum(nums[:k-1])# Cur window of size <= k
        cnt = 0

        for L in range(len(nums)-k + 1):
            wsum+=nums[L + k-1]
            if wsum/k >=threshold:
                cnt+=1
            wsum-=nums[L]
            
        return cnt