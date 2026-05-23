class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trgtMap ={}
        for i in range(len(nums)):
            trgtMap[nums[i]] = i #Fill the number & indices
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in trgtMap:
                if i != trgtMap[diff]:
                    res.append(i)
                    res.append(trgtMap[diff])
                    return sorted(res)
        return []

