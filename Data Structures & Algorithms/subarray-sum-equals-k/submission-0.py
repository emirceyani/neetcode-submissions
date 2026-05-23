class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0]=1

        ans = curr = 0

        for n in nums:
            curr += n
            ans += counts[curr -k]
            counts[curr]+=1

        return ans