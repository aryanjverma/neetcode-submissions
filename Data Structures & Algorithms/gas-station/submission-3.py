class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        
        for i in range(len(gas)):
            gas[i] -= cost[i]
            total += gas[i]
        if total < 0:
            return - 1
        
        currSum = -1
        currIndex = 0
        for index in range(len(gas)):
            if gas[index] >= 0:
                if currSum == -1:
                    currIndex = index
                    currSum = 0
                currSum += gas[index]
            else:
                if currSum != -1:
                    currSum += gas[index]
                    if currSum < 0:
                        currSum = -1
        return currIndex

