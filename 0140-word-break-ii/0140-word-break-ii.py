class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            # If already calculated, return stored result
            if start in memo:
                return memo[start]

            # Reached the end of the string
            if start == len(s):
                return [""]

            result = []

            # Try every possible word starting from 'start'
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                # If current substring is a dictionary word
                if word in wordSet:

                    # Find all sentences for the remaining part
                    suffixes = dfs(end)

                    # Add current word to every suffix
                    for suffix in suffixes:
                        if suffix == "":
                            result.append(word)
                        else:
                            result.append(word + " " + suffix)

            # Store result for this index
            memo[start] = result

            return result

        return dfs(0)

