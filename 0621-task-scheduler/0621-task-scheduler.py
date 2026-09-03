class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Count frequency of each task
        count = {}

        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] += 1

        # Find maximum frequency
        maxFreq = 0

        for task in count:
            if count[task] > maxFreq:
                maxFreq = count[task]

        # Count how many tasks have maximum frequency
        maxCount = 0

        for task in count:
            if count[task] == maxFreq:
                maxCount += 1

        # Calculate minimum intervals
        answer = (maxFreq - 1) * (n + 1) + maxCount

        # We cannot have fewer intervals than total tasks
        if answer < len(tasks):
            answer = len(tasks)

        return answer