class Word:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value > other.value

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordToCount = defaultdict(int)
        for word in words:
            wordToCount[word] += 1
        
        heap = []
        for word, count in wordToCount.items():
            heapq.heappush(heap, (count, Word(word)))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _ in range(k):
            count, word = heapq.heappop(heap)
            res.append(word.value)
        return res[::-1]

# O(klogn) solution
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordToCount = defaultdict(int)
        for word in words:
            wordToCount[word] += 1

        heap = [(-count, word) for word, count in wordToCount.items()]
        heapq.heapify(heap)
        
        res = []
        for _ in range(k):
            count, word = heapq.heappop(heap)
            res.append(word)

        return res

