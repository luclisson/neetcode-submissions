class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best,l = 0,0
        h_seq = {}

        for i in range(len(s)):
            h_seq[s[i]] = h_seq.get(s[i], 0) + 1
            letter = max(h_seq,key=h_seq.get)

            if h_seq[letter] + k >= i-l+1:
                best = max(best,i - l + 1)
            else:
                while i>l and h_seq[letter]+k < i - l +1:
                    h_seq[s[l]] -= 1
                    l+=1
                    letter = max(h_seq,key=h_seq.get)
                best = max(best,i - l + 1)
        return best 