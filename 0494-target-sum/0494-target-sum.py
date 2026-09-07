class Solution:
    def findTargetSumWays(self, nums, target):

        memo = {}

        def solve(index, current_sum):

            if index == len(nums):
                if current_sum == target:
                    return 1
                return 0

            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            plus = solve(
                index + 1,
                current_sum + nums[index]
            )

            minus = solve(
                index + 1,
                current_sum - nums[index]
            )

            memo[(index, current_sum)] = plus + minus

            return memo[(index, current_sum)]

        return solve(0, 0)