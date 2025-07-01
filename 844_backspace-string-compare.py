class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        two pointers, one for each string
        compare chars at pointers starting from the end

        count the number of '#' to determine which indexes to skip over before comparing

        if any word runs out of chars before the other, they cannot be equal

        time: O(n + m) where n is len(s) and m is len(t)
        space: O(1)
        """
        def get_next_idx(string, idx):
            # returns index corresponding to valid (non-deleted) char that precedes the passed index
            back = 0
            while idx >= 0:
                if string[idx] == '#':
                    back += 1
                elif back > 0:
                    # non '#' char found but deleted
                    back -= 1
                else:
                    break
                idx -= 1
            return idx

        n = len(s)
        m = len(t)

        i = n - 1
        j = m - 1
        while i >= 0 or j >= 0:
            i = get_next_idx(s, i)
            j = get_next_idx(t, j)
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                # one word has run out of chars
                return False
            i -= 1
            j -= 1
        
        return True

