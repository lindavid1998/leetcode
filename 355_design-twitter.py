class Twitter:
    def __init__(self):
        self.followees = defaultdict(set) # userId -> set of userIds
        self.tweets = defaultdict(list) # userId -> list of tweetIds
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # amortized O(1)
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        Time: O(nlogn)
        Space: O(n)
        '''
        # get list of userIds to pull tweets from
        followees = self.followees[userId]
        followees.add(userId)

        # O(nlogn)
        minHeap = []
        for followee in followees:
            tweets = self.tweets[followee] # get list of [count, tweetId]
            # push each tweet into heap
            for tweet in tweets:
                heapq.heappush(minHeap, tweet) # O(log n)
        
        # O(log n)
        res = []
        while len(res) < 10 and minHeap:
            _, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)

class Twitter:

    def __init__(self):
        self.followees = defaultdict(set) # userId -> set of userIds
        self.count = 0
        self.tweets = []  # minHeap of [count, userId, tweetId]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, [self.count, userId, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        Fetches at most the 10 most recent tweet IDs in the user's news feed. 
        Each item must be posted by users who the user is following or 
        by the user themself. 
        Tweets IDs should be ordered from most recent to least recent.
        '''
        followees = self.followees[userId]
        followees.add(userId)
        heapCopy = self.tweets.copy()
        res = []
        while len(res) < 10 and heapCopy:
            [count, uId, tweetId] = heapq.heappop(heapCopy)
            if uId in followees:
                res.append(tweetId)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
