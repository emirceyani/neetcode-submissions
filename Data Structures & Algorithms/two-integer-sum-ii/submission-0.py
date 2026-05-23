class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R: #Utilize the soted nature of array
            if numbers[L] + numbers[R] > target:
                R -= 1 #Rightmost element is too big
            elif numbers[L] + numbers[R] < target:
                L += 1 #Leftmost element is too small
            else:
                return [L+1, R+1]