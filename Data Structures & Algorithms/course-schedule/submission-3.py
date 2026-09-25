from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [None] * numCourses
        for pr in prerequisites:
            a, b = pr
            if courses[a] is None:
                courses[a] = []
            courses[a].append(b)
        path = set()
        approved = set()
        def dfs(index):
            if index in approved:
                return True
            if index in path:
                return False
            path.add(index)
            if courses[index]:
                for pr in courses[index]:
                    if not dfs(pr):
                        return False
            path.remove(index)
            approved.add(index)
            return True
        for i in range(numCourses):
            path = set()
            if not dfs(i):
                return False
        return True


