from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        count_s, count_t = Counter(s), Counter(t)
        for c in count_s:
            if count_s[c] != count_t[c]:
                return False
        return True