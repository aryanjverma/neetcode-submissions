class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def dfs(currPerm):
            if len(currPerm) == len(nums):
                perms.append(currPerm[:])
            else:
                for num in nums:
                    if num not in currPerm:
                        currPerm.append(num)
                        dfs(currPerm)
                        currPerm.pop()
        dfs([])
        return perms