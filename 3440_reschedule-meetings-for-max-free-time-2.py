class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Greedy

        Intuition: Each meeting has two gaps to its left and right
        At each meeting we have two choices:
        1. slide the meeting over to combine its left and right gaps
        2. if there's a large enough space somewhere before or after, move it there

        In order to know if there's a large enough space we need to maintain
        a prefix and suffix array, tracking max gap sizes

        first calculate all n + 1 gaps:
        before the 1st meeting, between all the meetings, then after the last meeting

        prefix => leftMax[i] = largest gap to the left of gap[i] (not inclusive)
        postfix => rightMax[i] = largest gap to the right of gap[i + 1] (not inclusive)

        why largest gap to the right of gap[i + 1]?

        each meeting[i] has two adjacent gaps: gaps[i] and gaps[i + 1]
        so at each meeting[i] we need to know the max gap after gaps[i + 1]

        Time: O(n)
        Space: O(n)
        """
        n = len(startTime)
        res = 0

        # calculate the gaps
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        gaps[-1] = eventTime - endTime[-1]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        
        # leftMax[i] = largest gap to left of gap[i]
        leftMax = [0] * (n + 1)
        for i in range(1, n + 1):
            leftMax[i] = max(
                leftMax[i - 1],
                gaps[i - 1]
            )
        
        rightMax = [0] * (n + 1)
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(
                rightMax[i + 1],
                gaps[i + 2] # we want largest gap to the right of gaps[i + 1]
            )

        for i in range(n):
            duration = endTime[i] - startTime[i]
            res = max(res, gaps[i] + gaps[i + 1]) # option 1

            # option 2 if there is enough space to move the meeting elsewhere
            if duration <= max(leftMax[i], rightMax[i]):
                res = max(res, duration + gaps[i] + gaps[i + 1])
        
        return res
        
