class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        place = {}
        for i in range(len(order)):
            place[order[i]] = i
        
        for i in range(len(words) - 1):
            left = words[i]
            right = words[i + 1]
            isLess = False
            for j in range(min(len(left), len(right))):
                leftPlace = place[left[j]]
                rightPlace = place[right[j]]
                if leftPlace > rightPlace:
                    return False
                elif leftPlace < rightPlace:
                    isLess = True
                    break
            if not isLess and len(left) > len(right):
                return False
        return True