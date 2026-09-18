class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        freqs = dict()
        nums = []
        i = 0
        while i < len(hand):
            currNum = hand[i]
            freq = 0
            while i < len(hand) and hand[i] == currNum:
                i += 1
                freq += 1
            
            nums.append(currNum)
            freqs[currNum] = freq
        print(freqs)
        
        for i in range(len(nums)):
            
            num = nums[i]
            freq = freqs[num]
            if freq > 0:
                for j in range(groupSize):
                    
                    if num + j not in freqs or freqs[num + j] < freq:
                        return False
                    freqs[num + j] -= freq
        return True