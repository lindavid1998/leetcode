class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """
        given a string s containing directions N S E W

        N moves position up by 1  -> y += 1
        S -> y -= 1
        E -> x += 1
        W -> x -= 1

        total horizontal movement -> abs(east - west)
        " vertical movement -> abs(north - south)
        Manhattan distance at any point is total horizontal + total vertical movement

        key intuition: when we change a direction to optimal direction, the manhattan dist can
        increase by 2. so with k changes, this means potential 2 * k increase to the MD

        key intuition: the max MD after i + 1 moves is i + 1 (ex: all in same direction).
        so (i + 1) - current MD tells you how far off you are, and also gives you the upper limit of improvement 

        algorithm:
        iterate over s
        at each point, calc current MD
        calc potential improvement in MD from switches
            potential improvement is the min between 2 * k and (i + 1) - current MD
        overwrite res if new max found

        time: O(n)
        space: O(1)
        """
        res = 0

        direction_counts = {
            'N': 0,
            'S': 0,
            'E': 0,
            'W': 0
        }

        n = len(s)
        for i in range(n):
            c = s[i]
            direction_counts[c] += 1

            x = direction_counts['E'] - direction_counts['W']
            y = direction_counts['N'] - direction_counts['S']
            MD = abs(x) + abs(y)

            improvement = min(2 * k, i + 1 - MD)

            res = max(res, MD + improvement)

        return res
