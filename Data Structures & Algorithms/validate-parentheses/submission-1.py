class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rel = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for char in s:
            if char in rel:
                stack.append(char)
            else:
                if stack:
                    last_opening = stack.pop()
                else:
                    #found closing before opening
                    return False

                if char == rel.get(last_opening):
                    continue
                else:
                    return False
        # check if every opening has been closed
        return len(stack) == 0