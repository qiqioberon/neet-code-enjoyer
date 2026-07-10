class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for val in nums:
            maps[val] = maps.get(val, 0) + 1
        maps = dict(sorted(maps.items(), key=lambda item: item[1], reverse=True))
        res_set = set()
        for key in maps.keys():
            res_set.add(key)
            if len(res_set) == k:
                return list(res_set)