class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        def search(currArray):
            left = 0
            right = len(answer) - 1
            while left <= right:
                mid = (left + right) // 2
                if answer[mid] == currArray:
                    return True
                if answer[mid] > currArray:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        def helper(i, currDiff, currArray):
            if currDiff == 0 and not (search(currArray)):
                answer.append(currArray)
            if currDiff > 0:
                n = 0
                for i in range(i, len(candidates)):
                    if candidates[i] > n:
                        if currDiff >= candidates[i]:
                            helper(i + 1, currDiff - candidates[i], currArray + [candidates[i]])
                        n = candidates[i]
        helper(0, target, [])
        
        return answer