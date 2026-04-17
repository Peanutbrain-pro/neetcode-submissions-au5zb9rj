class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []

        self.time_map[key].append((value, timestamp))
        # print(self.time_map)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        # print(self.time_map)
        # print(self.time_map[key])
        value_timestamp_list = self.time_map[key]
        low = 0
        high = len(value_timestamp_list) - 1
        index = 0
        found = False

        while low <= high:
            mid = (low + high) // 2
            if value_timestamp_list[mid][1] <= timestamp:
                found = True
                index = mid

                if mid != high and value_timestamp_list[mid + 1][1] > timestamp:
                    break

                low = mid + 1
            else:
                high = mid - 1

        if not found:
            return ""

        return value_timestamp_list[index][0]




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)