class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [],[]
        preprod, sufprod=1,1
        prefix.append(1)
        for i in range(1,len(nums)):
            preprod *= nums[i-1] 
            prefix.append(preprod)
        for num in nums[::-1]:
            sufprod *= num
            suffix.append(sufprod)
        suffix.pop();  suffix2 = suffix[::-1] ; suffix2.append(1)
        return [prefix[i] * suffix2[i] for i in range(len(nums))]