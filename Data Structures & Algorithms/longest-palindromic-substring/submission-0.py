class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0 
        maxpal = ""
        for i in range(len(s)):
            #ODD
            l,r = i,i 
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    length = r-l +1
                    maxpal = s[l:r+1]
                l -= 1
                r += 1
            #EVEN 
            l,r = i, i +1 
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    length = r-l +1
                    maxpal = s[l:r+1]
                l -= 1
                r += 1
        return maxpal