class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        a, b = {}, {}

        for v1,v2 in zip(s,t):
            a[f'{v1}'] = a.get(f'{v1}',0) +1
            b[f'{v2}'] = b.get(f'{v2}',0) +1
        
        return a == b

        