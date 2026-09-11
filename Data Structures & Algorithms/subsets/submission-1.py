class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        count = 1 << len(nums)
        answer = [[] for _ in range(count)]
        for i in range(len(nums)):
            num = nums[i]
            mover = 1 << (i + 1)
            for j in range(count // mover):
                for k in range(mover // 2, mover):
                    answer[j*mover+k].append(num)
        return answer
        
        