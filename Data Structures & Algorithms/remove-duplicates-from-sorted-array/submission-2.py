class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       uniques = sorted(list(set(nums)))
       nums[:len(uniques)] = uniques
       return len(uniques)
