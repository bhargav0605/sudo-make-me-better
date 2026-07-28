class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, val in enumerate(nums):
            second_num = target - val
            if second_num in seen:
                return [seen[second_num], index]
            seen[val] = index
        return []