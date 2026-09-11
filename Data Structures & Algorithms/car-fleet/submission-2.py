import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions, speeds = zip(*sorted(zip(position, speed)))
        times = []
        index = len(speeds) - 1
        while index >= 0:
            speed = (target - positions[index]) / speeds[index]
            if not times or speed > times[-1]:
                times.append(speed)
            index -= 1
        return len(times)