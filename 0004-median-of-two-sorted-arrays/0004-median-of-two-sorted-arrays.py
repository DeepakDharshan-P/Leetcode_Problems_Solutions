
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Left and right values around partition
            if partition1 == 0:
                left1 = float('-inf')
            else:
                left1 = nums1[partition1 - 1]

            if partition1 == m:
                right1 = float('inf')
            else:
                right1 = nums1[partition1]

            if partition2 == 0:
                left2 = float('-inf')
            else:
                left2 = nums2[partition2 - 1]

            if partition2 == n:
                right2 = float('inf')
            else:
                right2 = nums2[partition2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                max_left = max(left1, left2)

                if (m + n) % 2 == 1:
                    return float(max_left)

                min_right = min(right1, right2)

                return (max_left + min_right) / 2.0

            # partition1 is too far right
            elif left1 > right2:
                right = partition1 - 1

            # partition1 is too far left
            else:
                left = partition1 + 1