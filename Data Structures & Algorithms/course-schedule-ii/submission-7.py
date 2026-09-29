class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [None] * numCourses
        for pr in prerequisites:
            a, b = pr
            if courses[a] is None:
                courses[a] = []
            courses[a].append(b)
        answer = []
        path = set()
        visited = set()
        def dfs(index):
            if index in path:
                return False
            if index in visited:
                return True
            if courses[index] is None:
                answer.append(index)
                visited.add(index)
                return True
            
            path.add(index)
            for course in courses[index]:
                if not dfs(course):
                    return False
            answer.append(index)
            path.remove(index)
            visited.add(index)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return answer            

