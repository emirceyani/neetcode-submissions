class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, curSet, subset):
            if i >= len(nums):
                subset.append(curSet.copy())
                return

            # decision to include nums[i]
            curSet.append(nums[i])
            helper(i + 1, nums, curSet, subset)
            curSet.pop()

            # decision NOT to include nums[i]
            helper(i + 1, nums, curSet, subset)
        subset, curSet = [], []
        helper(0, nums, curSet, subset)
        return subset