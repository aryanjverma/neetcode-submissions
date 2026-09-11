import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        times = []
        index = len(position) - 1
        while index >= 0:
            currSpeed = (target - position[index]) / speed[index]
            if not times or currSpeed > times[-1]:
                times.append(currSpeed)
            index -= 1
        return len(times)