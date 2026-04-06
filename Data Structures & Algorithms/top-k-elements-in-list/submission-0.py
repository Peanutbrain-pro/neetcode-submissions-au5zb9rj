class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = []

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # print(freq)

        freq_buckets = [[] for _ in range(length + 1)]
        # print(freq_buckets, len(freq_buckets))
        for key in freq:
            # print(freq[key], key)
            freq_buckets[freq[key]].append(key)
            # freq_buckets[1].append(1)
        #     print(freq_buckets)
        # print(freq_buckets)

        i = length - 1
        while k > 0:
            for n in freq_buckets[i]:
                result.append(n)
                k -= 1
                if k == 0:
                    break
            i -= 1

        return result