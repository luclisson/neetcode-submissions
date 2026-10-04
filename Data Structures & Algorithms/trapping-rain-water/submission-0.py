class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = []
        post = []
        c_max = 0
        water = 0
        for h in height:
            if h >= c_max:
                c_max = h
            pre.append(c_max)
        c_max = 0

        for h in reversed(height):
            if h >= c_max:
                c_max = h
            post.append(c_max)
        post = list(reversed(post))
        
        for i in range(1,n-1):
            l,r = i-1,i+1
            water += (min(pre[i],post[i]) - height[i])
        return water

        