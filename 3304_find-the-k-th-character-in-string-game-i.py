class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        alice has a string "a"
        given pos int k

        return the kth char in word after enough operations have been done

        O(k^2)

        each operation:
        change every char to its next char and append it to the original word

        init word <- "a"

        while len(word) < k:
            new_word = ""
            for every char in word
                change it to next char  (ord(c) - ord('a') + 1) % 26
                append new char to new_word
            append new_word to word
        return word[k - 1]
        """
        word = "a"

        while len(word) < k:
            new_word = ""
            for c in word:
                new_char = (ord(c) - ord('a') + 1) % 26
                new_word += chr(new_char + ord('a'))

            word += new_word

        return word[k - 1]

