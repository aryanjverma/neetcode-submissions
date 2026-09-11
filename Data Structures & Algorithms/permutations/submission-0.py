class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        answer = []

        for i in range(len(nums)):
            
            permutations = self.permute(nums[:i] + nums[i + 1:])

            for j in range(len(permutations)):
                permutation = permutations[j]
                permutation.insert(0, nums[i])
                answer.append(permutation)
        return answer