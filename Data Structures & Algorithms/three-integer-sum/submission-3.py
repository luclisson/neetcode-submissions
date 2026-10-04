class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        out = []
        for ind,num in enumerate(nums):
            print(f'trying to find with {num}')
            l,r = ind+1,len(nums)-1
            while l<r:
                if nums[l] + nums[r] + num > 0:
                    r-=1
                elif nums[l] + nums[r] + num < 0:
                    l+=1
                else:
                    triplet = sorted([nums[l],nums[r],num])
                    if triplet not in out:
                        out.append(triplet)
                    l+=1
                    r-=1
        return out