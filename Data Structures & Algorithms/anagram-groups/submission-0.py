class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in maps:
                maps[key] = []
            maps[key].append(string)
        for key,values in maps.items():
            print(key, values)
        return list(maps.values())