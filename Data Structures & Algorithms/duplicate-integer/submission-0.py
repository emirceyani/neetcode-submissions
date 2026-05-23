class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cntMap = {}
        for num in nums:
            if num in cntMap:
                return True
            else:
                cntMap[num] = 1
        return False