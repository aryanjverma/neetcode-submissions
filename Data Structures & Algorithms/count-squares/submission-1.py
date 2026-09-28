class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        answer = 0
        visited = set()
        for newPoint in self.points:
            deltaX = point[0] - newPoint[0]
            deltaY = point[1] - newPoint[1]
            if deltaX == 0 and deltaY == 0:
                continue
            freq = self.points[newPoint]
            
            point1 = (point[0] - deltaY, point[1] + deltaX)
            if point1 in self.points:
                freq *= self.points[point1]
            else:
                continue
            
            point2 = (newPoint[0] - deltaY, newPoint[1] + deltaX)
            if point2 in self.points:
                freq *= self.points[point2]
            else:
                continue
            if newPoint not in visited or point1 not in visited or point2 not in visited:
                visited.add(newPoint)
                visited.add(point1)
                visited.add(point2)
                answer += freq
        return answer            
