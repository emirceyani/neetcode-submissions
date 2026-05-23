class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = n
        while num%2 == 0 and num>1:
            num//=2
        return True if num == 1 else False