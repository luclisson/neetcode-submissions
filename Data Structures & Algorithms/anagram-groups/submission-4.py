class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # plan: loop through input strs add to hashmap, if str is anagram of any key
        # if yes, add str to hashtable bucket, 
        # if not add str as new bucket

        hashmap = {} #dicts are implemented as hashmaps in python (i hope...)

        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str in hashmap:
                hashmap.get(sorted_str).append(word)
            else: hashmap[sorted_str] = [word]
        return list(hashmap.values())
        