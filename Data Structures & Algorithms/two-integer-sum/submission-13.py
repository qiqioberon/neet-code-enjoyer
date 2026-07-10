class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, i in enumerate(nums):
            selisih = target - i
            if selisih in nums and nums.index(selisih) != index:
                return sorted([index, nums.index(selisih)])
            
