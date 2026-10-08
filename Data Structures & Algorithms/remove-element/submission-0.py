from collections import deque
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        currPointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
                nums[currPointer] = nums[i]
                currPointer += 1
        return k