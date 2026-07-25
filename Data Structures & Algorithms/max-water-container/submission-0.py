class Solution:
    def maxArea(self, heights: List[int]) -> int:
      l, r = 0, len(heights)-1
      max = 0

      while l < r:

        if (min(heights[l], heights[r]) * (r - l)) > max:
            max = (min(heights[l], heights[r]) * (r - l))
        if heights[l] > heights[r]:
            r -= 1
        elif heights[l] <= heights[r]:
            l += 1
    
      return max