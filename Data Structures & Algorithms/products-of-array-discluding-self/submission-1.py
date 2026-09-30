class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1 for _ in range(n)]
        post = [1 for _ in range(n)]
        curr = 1
        for i in range(n):
            pre[i] = curr
            curr *= nums[i]
        curr = 1
        for i in reversed(range(n)):
            post[i] *= curr
            curr *= nums[i]

        return [
            pre[i]*post[i]
            for i in range(n)
        ]



