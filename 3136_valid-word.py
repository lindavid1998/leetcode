class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False
        
        if not word.isalnum():
            return False
        
        includesVowel = False
        includesConsonant = False
        for c in word:
            vowels = ['a', 'e', 'i', 'o', 'u']
            if includesVowel and includesConsonant:
                return True
            if c.lower() in vowels:
                includesVowel = True
            elif c.isalpha():
                includesConsonant = True
        return includesVowel and includesConsonant
