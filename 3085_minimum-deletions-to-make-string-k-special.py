class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        a word is k-special if the max_freq - min_freq <= k

        count the frequencies of each char in word.
        then sort the frequencies in increasing order

        iterate over the frequencies, setting the current frequency as the 
        "base" (i.e. the minimum frequency). for a given base, the valid frequencies are
        minF <= freq <= minF + k

        count the number of deletions for each base:
        any frequencies to the left of base will be deleted entirely
        any frequencies to the right of base will be reduced if it exceeds minF + k

        overwrite min deletions and return after checking each base
        
        time:
            O(n) to count freq
            + O(26log26) to sort frequencies
            + O(26^2) to count deletions
            = O(n)
        
        space:
            O(26) for frequency table and frequency array
            = O(1)
        """
        charToFreq = Counter(word)

        freq = list(charToFreq.values())
        freq.sort()

        # optimization: generate prefix sum array

        minDeletions = float("inf")
        for i in range(len(freq)):
            deletions = 0
            # set freq[i] as base
            max_freq = freq[i] + k

            for j in range(i):
                # optimization: use prefix sum
                deletions += freq[j]
            
            for j in range(i + 1, len(freq)):
                deletions += max(0, freq[j] - max_freq)
            
            minDeletions = min(minDeletions, deletions)

        return minDeletions
