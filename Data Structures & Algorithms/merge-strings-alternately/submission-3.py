class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        if len(word1)<len(word2):
            res+=word2[min(len(word1), len(word2)):]
        else:
            res+=word1[min(len(word1), len(word2)):]
        return res
