class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for ind,value in enumerate(nums):
            dif = target - value

            if dif in map:
                return [map.get(dif),ind]
            map[value] = ind
        return None
