class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ret = [1] * size
        pre = 1
        post = 1

        for i in range(size):
            ret[i] = pre
            pre *= nums[i]

        for i in range(size):
            ret[size-i-1] *= post
            post *= nums[size-i-1]
        
        return ret



            


        