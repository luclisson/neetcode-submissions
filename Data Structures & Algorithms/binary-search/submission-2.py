class Solution:
    def helper(self,start,stop,nums,target):
        if stop - start < 0: return -1

        mid = (start + stop) // 2

        if target == nums[mid]: return mid

        if target > nums[mid]:
            return self.helper(mid+1,stop,nums,target)
        else:
            return self.helper(start,mid-1,nums,target)


    def search(self, nums: List[int], target: int) -> int:
        return self.helper(0,len(nums)-1,nums,target)