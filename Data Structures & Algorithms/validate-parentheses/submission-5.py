class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)<2:
            return False
        l=[]
        for i in range(len(s)):
            print(s[i])
            if s[i] not in ["]","}",")"]:
                l.append(str(s[i]))
            else:
                if len(l) == 0 : 
                    return False
                if str(l[-1]+s[i]) not in ["[]","{}","()"]:
                    print(str(l[-1]+s[i]))
                    return False
                l.pop()
        if len(l) >0:
            return False
        return True
