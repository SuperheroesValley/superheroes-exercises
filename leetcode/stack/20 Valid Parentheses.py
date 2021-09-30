class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        open_ = {"(", "{", "["}
        close_ = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for item in s:
            if item in open_:
                stack.append(item)
            else:
                if len(stack) == 0 or stack.pop() != close_[item]:
                    return False
                
        return True if len(stack) == 0 else False
