class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum=0
        left=0
        right=len(height)-1
        
        while right>=left:
            minheight=min(height[left],height[right])
            area=(right-left)*minheight
            if area>=maximum :
                maximum=area
            if height[left]>height[right]:
                right-=1
            else:                
                left+=1
        
        return maximum
            

        