class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap.get(num) + 1
            else: hashmap[num] = 1
        return sorted(hashmap, key=hashmap.get, reverse=True)[:k]