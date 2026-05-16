class MedianFinder:

    def __init__(self):
        self.isLengthEven = True
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        # print("Adding ", num)
        if not self.leftMaxHeap:
            self.leftMaxHeap.append(-num)
            self.isLengthEven = False
            return

        if self.isLengthEven:
            # print("list is even");
            median = self.findMedian()
            if num <= median:
                heapq.heappush(self.leftMaxHeap, -num)
            else:
                rightTop = heapq.heappushpop(self.rightMinHeap, num)
                heapq.heappush(self.leftMaxHeap, -rightTop)
            self.isLengthEven = False
        else:
            # print("list is odd");
            median = self.findMedian()
            if num >= median:
                heapq.heappush(self.rightMinHeap, num)
            else:
                leftTop = heapq.heappushpop(self.leftMaxHeap, -num)
                heapq.heappush(self.rightMinHeap, -leftTop)
            self.isLengthEven = True

    def findMedian(self) -> float:
        # print(self.leftMaxHeap, self.rightMinHeap)
        median = -self.leftMaxHeap[0]
        if self.isLengthEven:
            median = (median + self.rightMinHeap[0]) / 2
        return median
        