class TimeMap:

    def __init__(self):
        self.con = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.con[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        time_list = self.con[key]

        left = 0
        right = len(time_list) - 1
        answer = ""
        while left <= right:
            mid = (left + right) // 2

            time, value = time_list[mid]

            if time == timestamp:
                return value
            if time < timestamp:
                answer = value
                left = mid + 1
            else:
                right = mid - 1

        return answer