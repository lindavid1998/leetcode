class Solution:
    def isValid(self, s: str) -> bool:
        '''
        O(n) time and space
        Stack
        '''
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        for c in s:
            if c not in pairs:
                stack.append(c)
                continue
            if len(stack) == 0 or pairs[c] != stack.pop():
                return False
        
        return len(stack) == 0
