class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        time: O(n), no sort or heap needed

        intuition: get the char with the highest count
        place it in all the even indices starting at 0
        this ensures the char with highest freq is spread out
        all other chars can fill in the gaps

        """
        n = len(s)

        freq = {}
        max_count = 0
        max_char = None
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
            if freq[c] > max_count:
                max_count = freq[c]
                max_char = c
        
        # if not possible, return ""
        if max_count > (n + 1) // 2:
            return ""
        
        # place max count chars at even indices until run out
        res = [""] * n
        i = 0
        while max_count > 0:
            res[i] = max_char
            max_count -= 1
            i += 2
        del freq[max_char]

        # Place remaining letters, continuing at i until end of arr reached
        # then switch to odd indices
        for char, count in freq.items():
            # print(char, count)
            for k in range(count):
                if i >= n:
                    i = 1 # switch to odd indices
                res[i] = char
                i += 2 # this ensures no adjacent chars
            # print(res)

        return "".join(res)


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        greedy, heap, hash table

        intuition: rearrangement depends on chars with highest frequency. when building
        the string, they need to be prioritized so that they are spaced out

        for a given number of chars, there needs to be num_chars - 1 other chars to separate them

        so we can check if a solution exists by looking at the relation
        m - 1 <= n - m  which is (n + 1) / 2 >= m
        where m is the max_count and n - m is the remaining chars (these can act as separators)
        i.e. are there enough other chars to separate the chars with the max count? if so,
        there exists a valid solution

        why do we only need to look at max_count? if drawn out, you'll see that when its
        possible to arrange the chars corresponding to max_count, the other chars can just fit in
        the gaps

        ex: if we have string of length 7, note that the maximum allowable count is 4.
        anything more and it would be impossible to avoid adjacent chars
        a _ a _ a _ a
        m = 4, n - m = 3 
        4 - 1 <= 3? yes, valid

        algorithm:
        use hash table to get counts of each char
        build string by prioritizing chars with higher count
        this can be done with a maxheap
        to avoid adjacent chars, do not add chars immediately back into maxheap after popping.
        wait for one iteration to occur before adding back in

        time: O(n) to build hash map, O(nlog(26)) to pop from heap and build res
        O(26) to heapify

        space: O(26) for the heap and hash map
        """

        freq = Counter(s)
        n = len(s)

        # check if solution exists
        max_count = max(freq.values())
        if max_count > (n + 1) // 2:
            return ""

        maxHeap = [[-count, char] for char, count in freq.items()]
        heapq.heapify(maxHeap)

        res = []
        prev = None # count, char of previous char to be added to heap
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            res.append(char)
            count += 1 # increment since negative

            # add prev char back to heap
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count < 0:
                prev = [count, char]
        
        return "".join(res)

