class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [None] * numCourses
        for pr in prerequisites:
            a, b = pr
            if courses[a] is None:
                courses[a] = []
            courses[a].append(b)
        answer = []
        visited = set()
        def dfs(index):
            if courses[index] is None:
                if index not in answer:
                    answer.append(index)
                return True
            if index in answer:
                return True
            if index in visited:
                return False
            visited.add(index)
            for course in courses[index]:
                if not dfs(course):
                    return False
            answer.append(index)
            visited.remove(index)
            return True

        for i in range(numCourses):
            if i not in answer and not dfs(i):
                return []
        print(answer)
        return answer            

