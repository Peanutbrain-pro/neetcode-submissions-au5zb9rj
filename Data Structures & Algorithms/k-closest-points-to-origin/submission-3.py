class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        self.minheap = []
        result = []
        for x, y in points:
            self.minheap.append((math.sqrt(x**2 + y**2), (x, y)))

        for i in range(len(self.minheap) - 1, -1, -1):
            self.heapify(i)

        for i in range(k):
            result.append(list(self.minheap[0][1]))
            self.minheap[0] = self.minheap[-1]
            self.minheap.pop()
            self.heapify(0)
        
        return result

    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2

        smallest = None
        if (left < len(self.minheap)):
            if self.minheap[left][0] < self.minheap[i][0]:
                smallest = left
            if right < len(self.minheap) and self.minheap[right][0] < self.minheap[left][0] and self.minheap[right][0] < self.minheap[i][0]:
                smallest = right

        if smallest:
            self.minheap[i], self.minheap[smallest] = self.minheap[smallest], self.minheap[i]
            self.heapify(smallest)
