class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        greedy + prefix sum

        intuition: in a time window where you have K meetings and K+1 gaps, the longest continuous free
        time is if you stack all of them at the start or end of the window
        the free time is calculated as = total time of the window - total time of the meetings

        since we can only move k meetings and we need to keep relative order, we will iterate over the eventTime window
        and apply that logic to every window of k meetings, keeping track of the max free time found and returning it
        at the end

        to efficiently calculate the total time of meetings in a window, we will be utilizing a prefix sum called
        sum_durations[] of length n + 1 where sum_durations[i] is the total time of the 1st i meetings. 
        ex: in a window where we are picking the 3rd, 4th, and 5th meetings (k = 3), the total meeting duration is
        sum_durations[5] - sum_durations[2]

        """
        n = len(startTime)
        res = 0

        # calculate the prefix sum to efficiently calculate meeting duration in a window
        sum_durations = [0] * (n + 1)
        for i in range(n):
            duration = endTime[i] - startTime[i]
            sum_durations[i + 1] = sum_durations[i] + duration
        
        # iterate over the meeting times using a window size of k meetings
        # 1st window: 0 -> start of meeting[k]
        # 2nd window: end of meeting[0] -> start of meeting[k + 1]
        # ...
        # last window: ends at eventTime
        for r in range(k, n + 1):
            # l, r are the two pointers representing the first and last meetings that define the time window
            l = r - k - 1
            window_start_time = 0 if l < 0 else endTime[l]
            window_end_time = eventTime if r >= n else startTime[r]
            
            total_time = window_end_time - window_start_time
            meeting_time = sum_durations[r] - sum_durations[l + 1]
            # 1st window: first k meetings -> sum_durations[k] - sum_durations[0]
            # 2nd window: sum_durations[k + 1] - sum_durations[1]

            free_time = total_time - meeting_time

            res = max(free_time, res)

        return res
