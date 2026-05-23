class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            L, R = i+1, len(nums) - 1
            target = -nums[i]
            while L < R: 
                #Utilize the sorted nature of array
                if (nums[L] + nums[R]) > target:
                    R -= 1 
                elif (nums[L] + nums[R]) < target:
                    L += 1
                else:
                    if [nums[L], nums[R], -target] not in res:
                        res.append([nums[L], nums[R], -target])
                        L+=1
                    else:
                        R-=1
                    
        return res