class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in dupSet:
                return True
            else:
                dupSet.add(nums[i])
        return False
        