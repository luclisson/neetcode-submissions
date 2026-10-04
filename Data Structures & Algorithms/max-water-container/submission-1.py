class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l,r = 0,n-1
        max_water = 0
        while l<r:
            distance = r - l
            curr_water = distance * min(heights[l],heights[r])

            if max_water < curr_water:
                max_water = curr_water
            
            if heights[l] == max(heights[l],heights[r]):
                r-=1
            else:
                l+=1
        
        return max_water
            

        