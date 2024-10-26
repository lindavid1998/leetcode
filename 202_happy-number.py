class Solution:
    def isHappy(self, n: int) -> bool:
        # calculating sum of squares will always result in cycle 
        # use Floyd's linked list cycle detection algorithm
        # return True if repeated number is 1, else False

        def getSum(n):
            res = 0
            while n != 0:
                digit = n % 10
                res += digit ** 2
                n = n // 10
            return res

        slow = n
        fast = getSum(n)
        while slow != fast:
            slow = getSum(slow)
            fast = getSum(getSum(fast))
        
        return True if slow == 1 else False

class Solution:
    def isHappy(self, n: int) -> bool:
        # Loop and track sums with a set. Break out of loop when 1 found or cycle found
        # O(n log n) but in practice closer to O(log n) 
        def getSum(n):
            res = 0
            while n != 0:
                digit = n % 10
                res += digit ** 2
                n = n // 10
            return res

        # create set of sums
        sums = set()
        
        # calc first sum
        sumSquares = getSum(n)

        while sumSquares not in sums:
            if sumSquares == 1:
                return True
            # add it to the set
            sums.add(sumSquares)
            # get the next sum
            sumSquares = getSum(sumSquares)
        
        # exit loop once cycle found, and return False
        return False
