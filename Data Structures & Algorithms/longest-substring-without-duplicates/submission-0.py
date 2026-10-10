class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        seq = []
        for i in range(len(s)):
            if not s[i] in seq:
                seq.append(s[i])
            else:
                while len(seq)>1 and seq[0]!=s[i]:
                    seq.pop(0)
                seq.pop(0)
                seq.append(s[i])

            if len(seq) > best:
                best = len(seq)

        return best
