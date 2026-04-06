class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        indexes = []
        distances = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # print("index: ", i, "\temperature: ", t)

            if not indexes:
                indexes.append(i)
                # print("indexes: ", indexes)
                # print("distances: ", distances)
                # print()
                continue

            if t > temperatures[indexes[-1]]:
                while indexes:
                    top_index = indexes[-1]
                    if t > temperatures[top_index]:
                        distances[top_index] = i - top_index
                        indexes.pop()
                    else:
                        break
            indexes.append(i)

            # print("indexes: ", indexes)
            # print("distances: ", distances)
            # print()

        return distances