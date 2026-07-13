class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, one in enumerate(nums):
            for j, two in enumerate(nums):
                if one + two == target and i != j:
                    return [i,j]