class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper2(i, nums, curSet, subsets):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            # decision to include nums[i]
            curSet.append(nums[i])
            helper2(i + 1, nums, curSet, subsets)
            curSet.pop()

            # decision NOT to include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper2(i + 1, nums, curSet, subsets)
        nums.sort()
        subsets, curSet = [], []
        helper2(0, nums, curSet, subsets)
        return subsets