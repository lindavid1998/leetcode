class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        O(n) time, O(1) space
        Two pointers, traverse from opposite ends
        '''
        def isAlphanumeric(c):
            if ord('a') <= ord(c) <= ord('z'):
                return True
            
            if ord('A') <= ord(c) <= ord('Z'):
                return True
            
            if ord('0') <= ord(c) <= ord('9'):
                return True
            
            return False

        l = 0
        r = len(s) - 1

        while l < r:
            # ignore any nonalphanumeric chars
            while l < r and not isAlphanumeric(s[l]):
                l += 1
            while l < r and not isAlphanumeric(s[r]):
                r -= 1

            # case insensitive
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True

