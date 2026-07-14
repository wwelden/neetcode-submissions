class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            val = 1
            for j in range(len(nums)):
                if j != i:
                    val *= nums[j]
            ret.append(val)
        return ret


        