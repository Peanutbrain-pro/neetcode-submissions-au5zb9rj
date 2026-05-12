class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        self.heap = stones
        for i in range(len(stones) - 1, -1, -1):
            # print("index: ", i)
            self.heapify(i)
            # print(self.heap)
        
        # print(self.heap)
        while len(self.heap) > 1:
            large1 = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify(0)
            
            large2 = self.heap[0]
            if large1 == large2:
                # print("top: ", self.heap[0])
                self.heap[0] = self.heap[-1]
                # print("top now: ", self.heap[0])
                self.heap.pop()
            else:
                self.heap[0] = abs(large1 - large2)
            self.heapify(0)

        return self.heap[0] if len(self.heap) else 0


    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        # if i == 3: print("Current index value: ", self.heap[i])

        largest = None
        if left < len(self.heap):
            # if i == 3: print("Current index value: ", self.heap[i])
            if self.heap[left] > self.heap[i]:
                # if i == 3: print("left is greater than root", self.heap[left], "is greater than", self.heap[i])
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[left] and self.heap[right] > self.heap[i]:
                # if i == 3: print(self.heap[right], "is greater than", self.heap[left])
                largest = right

        # if i == 3: print(largest)

        if largest:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

        