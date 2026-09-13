class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        nums = [0] * len(s)
        for i in range(len(s)):
            if int(s[i]) > 0:
                if i == 0:
                    nums[i] = 1
                else: 
                    nums[i] = nums[i - 1]            
            if i >= 1:
                num = int(s[i - 1: i + 1])
                
                if num >= 10 and num <= 26:
                    if i > 1:
                        nums[i] += nums[i - 2]
                    else:
                        nums[i] += 1
        print(nums)
        return nums[-1]