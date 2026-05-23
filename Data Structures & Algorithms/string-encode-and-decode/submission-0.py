class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"$"+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i< len(s):
            l = i
            while s[l] != "$":
                l+=1
            length = int(s[i:l])
            i = l + 1
            l = i + length
            res.append(s[i:l])
            i=l
        return res
