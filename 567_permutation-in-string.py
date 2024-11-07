class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Sliding window
        O(n) time
        O(1) space since char array restricted to 26 chars
        '''
        if len(s1) > len(s2):
            return False

        s1_char = [0] * 26
        s2_char = [0] * 26
        for i, c in enumerate(s1):
            s1_char[ord(c) - ord('a')] += 1
            s2_char[ord(s2[i]) - ord('a')] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if s1_char == s2_char:
                return True
            s2_char[ord(s2[r]) - ord('a')] += 1
            s2_char[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
        
        return s1_char == s2_char

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        O(n) time
        O(1) space since char array limited to 26 chars

        Slight time optimization by tracking matches count instead of comparing char arrays
        on each iteration
        '''
        if len(s1) > len(s2):
            return False

        s1_char = [0] * 26
        s2_char = [0] * 26
        for i, c in enumerate(s1):
            s1_char[ord(c) - ord('a')] += 1
            s2_char[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_char[i] == s2_char[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            s2_char[idx] += 1

            if s1_char[idx] == s2_char[idx]:
                matches += 1
            if s1_char[idx] + 1 == s2_char[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            s2_char[idx] -= 1

            if s1_char[idx] == s2_char[idx]:
                matches += 1
            if s1_char[idx] == s2_char[idx] + 1:
                matches -= 1
            
            l += 1

        
        return matches == 26
