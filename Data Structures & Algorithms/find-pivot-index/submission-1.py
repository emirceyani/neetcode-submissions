class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Construct prefix sum
        for i in range(len(nums)):
            if i == 0 and sum(nums[i+1:]) == 0:
                return 0
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
                
        return -1