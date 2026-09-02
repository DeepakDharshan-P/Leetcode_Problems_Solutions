class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        have = {}
        required = len(need)
        formed = 0

        left = 0
        best_length = float("inf")
        best_left = 0

        for right in range(len(s)):
            char = s[right]

            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length

                    best_left = left

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]