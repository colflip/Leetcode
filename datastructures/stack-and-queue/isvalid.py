class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (top == '(' and c != ')') or (top == '[' and c != ']') or (top == '{' and c != '}'):
                    return False
        return not stack


s = "()[]{}"
print(Solution().isValid(s))
