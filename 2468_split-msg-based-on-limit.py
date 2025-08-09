class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        """
        message length is 10^4
        number of parts ranges [1, 10^4]
        digits in # of parts is [1, log(10^4)] ->[1, 4]
        so we only need to check if parts length is 1, 2, 3, or 4 digits long

        once number of digits is known, construct the answer using a placeholder for the total number of parts
        replace the placeholder at the end when the number of parts is known

        time: O(n) where n is the length of the message
        """
        m = len(message)
        for parts_digits in range(1, 5):
            res = []
            placeholder = '#' * parts_digits
            i = 0 # index to track place in message
            part_idx = 1
            while i < m:
                suffix = f'<{part_idx}/{placeholder}>'
                substr_len = limit - len(suffix) # how many chars can fit with the suffix

                # what if substring_length < 0? then no solution..
                if substr_len < 0:
                    # parts_digits is invalid
                    return []

                j = min(i + substr_len, m)
                part = message[i:j] + suffix
                res.append(part)
                i = j
                part_idx += 1

            # how do i know if this solution is valid?
            # if the number of parts found matches the parts_length
            num_parts = len(res)
            num_parts_str = str(num_parts)
            num_digits = len(num_parts_str)
            if num_digits == parts_digits:
                # replace placeholder with total number of parts
                for i, part in enumerate(res):
                    res[i] = part.replace(placeholder, num_parts_str)
                return res

        return []
            
