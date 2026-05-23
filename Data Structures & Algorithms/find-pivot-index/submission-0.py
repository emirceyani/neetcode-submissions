class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Construct prefix sum
        prefix = []
        total = 0 
        for n in nums:
            total += n
            prefix.append(total)
        for i in range(len(nums)):
            if i == 0 and sum(nums[i+1:]) == 0:
                return 0
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
                
        return -1