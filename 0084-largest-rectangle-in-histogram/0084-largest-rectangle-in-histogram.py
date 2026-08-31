class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = 0

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = h * width

                if area > maxArea:
                    maxArea = area

            stack.append(i)

        n = len(heights)

        while stack:
            h = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            area = h * width

            if area > maxArea:
                maxArea = area

        return maxArea
