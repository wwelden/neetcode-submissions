class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        pre = 1

        for n in nums:
            ret.append(pre)
            pre *= n

        post = 1
        size = len(nums)

        for i in range(size):
            ret[size-i-1] *= (post)
            post *= nums[size-i-1]
        
        return ret



            


        