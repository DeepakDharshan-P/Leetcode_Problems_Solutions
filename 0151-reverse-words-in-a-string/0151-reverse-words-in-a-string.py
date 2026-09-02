class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        for ch in s:
            if ch != " ":
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""

        # Add the last word
        if word != "":
            words.append(word)

        # Reverse the words
        words = words[::-1]

        return " ".join(words)