class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        left = 0
        right = 1
        answer = 1
        neg = 1
        while right < len(arr):
            if arr[left] < arr[right]:
                neg = 1
            else:
                neg = -1
            
            while right < len(arr) and arr[right - 1] * neg < arr[right] * neg:
                right += 1
                neg *= - 1
            
            answer = max(answer, right - left)

            left = max(left + 1, right - 1)
            right = left + 1
        return answer