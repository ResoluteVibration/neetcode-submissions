class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = area = left = 0
        right = len(heights) - 1
        while left < right:
            w = abs(left - right)
            h = min(heights[left],heights[right])
            area = w*h
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area