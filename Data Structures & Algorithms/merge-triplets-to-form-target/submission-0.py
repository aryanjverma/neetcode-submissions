class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        currTriplet = None
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                if currTriplet is None:
                    currTriplet = triplet
                else:
                    for i in range(3):
                        currTriplet[i] = max(currTriplet[i], triplet[i])
        return target == currTriplet