class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        O(nlogn) time
        O(n) space

        Use a stack to represent car fleets
        Add to stack if car cannot catch up to any of the ones in front of it
        '''
        time = [] # [position, time]
        for i in range(len(speed)):
            time.append([position[i], (target - position[i]) / speed[i]])  
        time.sort(reverse = True) # O(nlogn)
        
        s = []
        for i in range(len(time)):
            if not s or time[i][1] > s[-1]:
                s.append(time[i][1])
        return len(s)
