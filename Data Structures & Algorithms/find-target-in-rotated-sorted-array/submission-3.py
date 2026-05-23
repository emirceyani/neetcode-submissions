class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        
        # Binary search on some range of values
        def binarySearch(left, right):

            while left <= right:
                mid = (left + right) // 2

                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
            return -1

        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid +1
            else:
                R = mid
        pivot = L



        result = binarySearch(0, pivot - 1)
        if result != -1:
            return result

        return binarySearch(pivot, len(nums) - 1)




    