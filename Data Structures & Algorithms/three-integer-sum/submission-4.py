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
                    res.append([nums[L], nums[R], -target])
                    L+=1
                    R-=1
                    while nums[L]==nums[L-1] and L<R:
                        L+=1
                    
        return [list(item) for item in set(tuple(row) for row in res)]