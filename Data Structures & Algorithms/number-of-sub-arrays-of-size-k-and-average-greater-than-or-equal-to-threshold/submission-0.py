class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        window = []# Cur window of size <= k
        L = 0
        cnt = 0

        for R in range(len(nums)):
            if R - L + 1 > k:
                window.remove(nums[L])
                L += 1
            window.append(nums[R])
            if len(window) == k:
                if float(sum(window))/len(window) >= threshold:
                    cnt+=1
        return cnt