class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathArray = path.split("/")
        for item in pathArray:
            if item == "..":
                if stack:
                    stack.pop()
            elif item != "." and item != "":
                stack.append(item)
        
        return "/" + "/".join(stack)