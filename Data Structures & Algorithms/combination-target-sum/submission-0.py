class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, curComb, combs,  nums):
            current_sum = sum(curComb)
            if current_sum == target:
                combs.append(curComb.copy())
                return
            if current_sum > target:
                return #As we care the exact sum, the condition is not k >n 

            for j in range(i, len(nums)):
                curComb.append(nums[j]) #We iterate over indices
                helper(j , curComb, combs, nums) #All combs with j 
                curComb.pop()
        combs = []
        helper(0, [], combs,  nums)
        return combs