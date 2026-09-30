import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[?!.,;:']",'',s.lower())
        s = s.replace(' ','')
        return s[::-1] == s
        