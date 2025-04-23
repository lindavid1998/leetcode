class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        # Hash table, greedy solution
        
        answerToCount = defaultdict(int)
        for answer in answers:
            answerToCount[answer] += 1
        
        res = 0
        for ans, count in answerToCount.items():
            res += math.ceil(count / (ans + 1)) * (ans + 1)
        
        return res
