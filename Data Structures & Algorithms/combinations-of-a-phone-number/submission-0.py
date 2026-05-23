class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(i, curComb):
            if len(curComb) == len(digits):
                #34 culd be DG , EH, ...
                combs.append(curComb)
                return


            for c in digitToChar[digits[i]]:
                #One digit is fixed 
                helper(i + 1, curComb+c) #Explore other digits 

        if digits:
            helper(0,"")
        return combs