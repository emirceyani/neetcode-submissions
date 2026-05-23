class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i , j = 0, len(heights)-1
        maxvol = 0
        while i < j:
            h = min(heights[i],heights[j])
            bottom = j-i
            vol = bottom * h
            if vol > maxvol:
                maxvol = vol
            if heights[i] == h: 
                i+=1
            else:
                j-=1
        return maxvol
        