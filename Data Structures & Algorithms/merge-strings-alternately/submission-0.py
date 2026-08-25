class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        a = []

        for i in range(min(len(word1), len(word2))):
            a.append(word1[i])
            a.append(word2[i])

        if len(word1) > len(word2):
            a.extend(word1[len(word2):])
        else:
            a.extend(word2[len(word1):])

        return "".join(a)


        