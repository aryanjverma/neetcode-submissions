class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(min(k + 1, len(nums))):
            if nums[i] in s:
                return True
            s.add(nums[i])
        
        l = 0
        r = k + 1
        while r < len(nums):
            s.remove(nums[l])
            if nums[r] in s:
                return True
            s.add(nums[r])
            l += 1
            r += 1
        return False
