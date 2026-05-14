class Twitter:

    def __init__(self):
        # person -> set of people they followed
        self.followMap = {}
        # person -> list of posts
        self.userPosts = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followMap:
            self.followMap[userId] = {userId}
        
        self.time += 1
        if userId not in self.userPosts:
            self.userPosts[userId] = []
        self.userPosts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        # print("\n\nGeting news for: ", userId)
        # print("People followed by", userId, "are: ", self.followMap[userId])
        for user in self.followMap[userId]:
            # print("Getting posts of ", user)
            if user not in self.userPosts:
                continue
            for (time, tweetId) in self.userPosts[user]:
                if len(minHeap) < 10:
                    heapq.heappush(minHeap, (time, tweetId))
                    continue

                if time < minHeap[0][0]:
                    continue

                heapq.heappushpop(minHeap, (time, tweetId))

            # print(minHeap)

        feed = []
        # print("Creating feed for ", minHeap)
        while minHeap:
            (time, tweetId) = minHeap[0]
            # print(time, tweetId)
            feed.append(heapq.heappop(minHeap)[1])
            # print(minHeap)
        # print(feed)
        return feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = {followerId}
        if followerId == followeeId:
            return
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
