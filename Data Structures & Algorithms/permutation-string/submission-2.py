class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # ------- planning -------
        """
        go through s1 and transform it to h_map
        sliding window s2 and build a h_map of sequence
        if s1_hmap == s2_hmap true
        if through s2 and not s2_hmap == s1_hmap return false

        other plan could be to sort s1 and sort the sequence
        solution 1 sould be far more efficient tho
        """
        if len(s1)>len(s2):
            return False
        #building s1_hmap O(n1) where n1 is len(s1)
        s1_hmap = {}
        for letter in s1:
            s1_hmap[letter] = s1_hmap.get(letter,0) + 1
        
        #sliding window algo for s2 O(n2) where n2 is len(s2)
        s2_hmap = {}
        l=0
        for i,letter in enumerate(s2):
            s2_hmap[letter] = s2_hmap.get(letter,0) + 1

            if s1_hmap == s2_hmap:
                return True
            if i - l + 1 > len(s1):
                while (
                    l<i and 
                    i - l + 1 > len(s1)
                ):
                    s2_hmap[s2[l]] = s2_hmap.get(s2[l],0) - 1
                    if s2_hmap[s2[l]] <=0:
                        del s2_hmap[s2[l]]
                    l += 1
                    if s1_hmap == s2_hmap:
                        return True
        return False

