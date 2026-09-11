class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        if len(nums1) == 0:
            if (len(nums2)) % 2 == 1:
                return nums2[len(nums2) // 2]
            return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
        
        
        if nums1[0] >= nums2[-1] or nums1[-1] <= nums2[0]:
            if len(nums1) == len(nums2):
                return (min(nums1[-1], nums2[-1]) + max(nums1[0], nums2[0])) / 2
            
            index = 0
            
            index = (len(nums2) + len(nums1)) // 2
            if nums1[-1] <= nums2[0]:
                index -= len(nums1)
            
            if (len(nums2) + len(nums1)) % 2 == 1:
                return nums2[index]
            return (nums2[index] + nums2[index - 1]) / 2
        
        target = (1 + len(nums1) + len(nums2)) // 2
        left = 0
        right = len(nums1) - 1
        while left <= right:
            index1 = (left + right) // 2
            index2 = target - 1 - index1

            if nums1[index1] > nums2[index2]:
                if index2 < len(nums2) - 1 and nums2[index2] <= nums2[index2 + 1] <= nums1[index1]:
                    right = index1 - 1
                else:
                    break
            elif nums1[index1] < nums2[index2]:
                if index1 < len(nums1) - 1 and nums1[index1] <= nums1[index1 + 1] <= nums2[index2]:
                    left = index1 + 1
                else:
                    break
            else:
                break
        
        if (len(nums1) + len(nums2)) % 2 == 1:
            answer = min(nums1[index1], nums2[index2])
            if index1 > 0:
                answer = max(answer, nums1[index1 - 1])
            if index2 > 0:
                answer = max(answer, nums2[index2 - 1])
            return answer
        twoMaxes = []
        twoMaxes.append(min(nums1[index1], nums2[index2]))
        twoMaxes.append(max(nums1[index1], nums2[index2]))
        if index1 > 0:
            twoMaxes[0] = max(twoMaxes[0], nums1[index1 - 1])
        if twoMaxes[0] > twoMaxes[1]:
            twoMaxes[0], twoMaxes[1] = twoMaxes[1], twoMaxes[0]
        if index2 > 0:
            twoMaxes[0] = max(twoMaxes[0], nums2[index2 - 1])
        return (twoMaxes[0] + twoMaxes[1]) / 2

        