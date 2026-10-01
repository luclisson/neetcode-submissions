class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h_map = {}
        for ind,num in enumerate(numbers):
            dif = target - num
            if num in h_map:
                return [h_map.get(num)[1]+1,ind+1]
            else:
                h_map[dif] = (num,ind)
