class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_map = set(nums)
        lens = []

        for num in h_map:
            #find starter
            if (num-1) not in h_map:
                length = 1
                #calc length
                while num + length in h_map:
                    length+=1
                lens.append(length)
        return max(lens,default=0)