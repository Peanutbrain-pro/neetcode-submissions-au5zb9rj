class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        print(freq)

        maxheap = [-freq[key] for key in freq]
        heapq.heapify(maxheap);
        queue = collections.deque()
        
        time = 1
        while maxheap or queue:
            print("time: ", time)
            print(maxheap, queue)
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue[0][0])
                queue.popleft()

            # print("After popping from queue: ", maxheap, queue)
            if maxheap:
                if maxheap[0] < -1:
                    queue.append((maxheap[0] + 1, time + n + 1))
                heapq.heappop(maxheap)

            time += 1
            
        return time - 1