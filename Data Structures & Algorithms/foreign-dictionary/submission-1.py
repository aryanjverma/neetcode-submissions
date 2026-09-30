class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = dict()
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            i = 0
            while i < min(len(word1), len(word2)) and word1[i] == word2[i]:
                i += 1
            
            if i < min(len(word1), len(word2)):    
                graph[word2[i]].add(word1[i])
            elif len(word1) > len(word2):
                return ""
        print(graph)
        answer = []
        visited = set()
        path = set()
        def dfs(node):
            if node in visited:
                return True
            if node in path:
                return False
            if len(graph[node]) == 0:
                answer.append(node)
                visited.add(node)
                return True
            path.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            path.remove(node)
            answer.append(node)
            visited.add(node)
            return True
        for node in graph:
            if not dfs(node):
                return ""
        return "".join(answer)
