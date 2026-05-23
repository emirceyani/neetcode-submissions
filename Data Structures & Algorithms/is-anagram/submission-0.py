from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        count_s = dict(sorted(Counter(s).items()))
        count_t = dict(sorted(Counter(t).items()))
        print(count_s, count_t)
        for c,s in zip(count_s, count_t):
            if count_s[c] != count_t[s]:
                return False
        return True