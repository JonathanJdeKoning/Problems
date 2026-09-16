class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.tweets)
        ans = []
        for i in range(len(self.tweets)-1,-1,-1):
            if self.tweets[i][0] in self.follows[userId] or self.tweets[i][0] == userId:
                ans.append(self.tweets[i][1])
                if len(ans) == 10: break
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

