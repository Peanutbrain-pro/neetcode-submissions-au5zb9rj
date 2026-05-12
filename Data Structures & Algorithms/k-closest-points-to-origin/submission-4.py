class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        self.maxheap = []
        result = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            if len(self.maxheap) < k:
                self.maxheap.append((dist, (x, y)))
                self.upheapify(len(self.maxheap) - 1)
            else:
                if dist >= self.maxheap[0][0]:
                    continue
                self.maxheap[0] = (dist, (x, y))
                self.heapify(0)

            # print(self.maxheap)

        # for i in range(len(self.maxheap) - 1, -1, -1):
        #     self.heapify(i)

        # for i in range(k):
        #     result.append(list(self.maxheap[0][1]))
        #     self.maxheap[0] = self.maxheap[-1]
        #     self.maxheap.pop()
        #     self.heapify(0)
        for dist, (x, y) in self.maxheap:
            result.append([x, y])
        
        return result

    def upheapify(self, i):
        if i == 0:
            return

        if i % 2:
            parent = (i - 1) // 2
        else:
            parent = (i - 2) // 2
        
        if self.maxheap[i][0] > self.maxheap[parent][0]:
            self.maxheap[i], self.maxheap[parent] = self.maxheap[parent], self.maxheap[i]
            self.upheapify(parent)

    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2

        smallest = None
        if (left < len(self.maxheap)):
            if self.maxheap[left][0] > self.maxheap[i][0]:
                smallest = left
            if right < len(self.maxheap) and self.maxheap[right][0] > self.maxheap[left][0] and self.maxheap[right][0] > self.maxheap[i][0]:
                smallest = right

        if smallest:
            self.maxheap[i], self.maxheap[smallest] = self.maxheap[smallest], self.maxheap[i]
            self.heapify(smallest)
