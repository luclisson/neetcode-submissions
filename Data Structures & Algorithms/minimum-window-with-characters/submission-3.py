class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        "------- planning -------"
        """
        t will be a hashmap again
        track how many unique letters are in t
        while iterating over s check if letter in t_map
            if so check if amount is matching aswell
                if so update have var
        if have and need var are matching this means we found a window from l to index of iteration with all chars of t_map
        use sliding window algo to minimize the window
        """
        t_map = {}
        for letter in t:
            t_map[letter] = t_map.get(letter,0) + 1

        s_map = {}
        l = 0
        have,need = 0,len(t_map)
        res, resLen = (-1, -1), float("infinity")
        for indx,letter in enumerate(s):
            s_map[letter] = s_map.get(letter,0) + 1
            if letter in t_map and s_map[letter] == t_map[letter]:
                have += 1

            while l <= indx and have == need:
                if indx - l + 1 < resLen:
                    resLen = indx - l + 1
                    res = (l,indx)
                s_map[s[l]] = s_map.get(s[l],0) -1

                if s[l] in t_map and t_map[s[l]] > s_map[s[l]]:
                    have -= 1

                if s_map[s[l]] <= 0:
                    del s_map[s[l]]
                    
                l += 1
        
        return s[res[0]:res[1]+1] if resLen < float('infinity') else ""






