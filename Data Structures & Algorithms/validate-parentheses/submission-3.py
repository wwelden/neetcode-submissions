class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif c == "}" or c == "]" or c == ")":
                if len(stack) > 0:
                    comp = stack.pop()
                    if c == "}" and comp != "{": return False
                    elif c == "]" and comp != "[": return False
                    elif c == ")" and comp != "(": return False
                else: return False
        if len(stack) == 0: return True
        else: return False

        
