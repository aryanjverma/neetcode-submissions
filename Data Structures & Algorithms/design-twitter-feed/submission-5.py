import heapq
from collections import deque
class Twitter:

    def __init__(self):
        self.following_map = defaultdict(set)
        self.tweet_map = defaultdict(deque)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        if len(self.tweet_map[userId]) > 10:
            self.tweet_map[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        q = []
        
        for user in self.following_map[userId]:
            for tweet in self.tweet_map[user]:
                heapq.heappush(q, tweet)
                
                if len(q) > 10:
                    heapq.heappop(q)
        for tweet in self.tweet_map[userId]:
            heapq.heappush(q, tweet)
            if len(q) > 10:
                heapq.heappop(q)
        answer = [0] * len(q)
        for i in range(len(q) - 1, - 1, - 1):
            answer[i] = heapq.heappop(q)[1]
        
        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)
