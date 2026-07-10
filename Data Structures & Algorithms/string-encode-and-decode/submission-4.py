from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += str(len(string)) + "#" + string

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the "#" separating the length from the string
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # The actual word begins after "#"
            start = j + 1
            result.append(s[start:start + length])

            i = start + length

        return result