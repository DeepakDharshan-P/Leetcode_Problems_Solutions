
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i = j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        while j < len(nums2):
            result.append(nums2[j])
            j += 1
            
        n = len(result)

        if n % 2 == 1:          # Odd length
            return float(result[n // 2])
        else:                   # Even length
            return float((result[n // 2 - 1] + result[n // 2]) / 2)

