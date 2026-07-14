class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        hasZero = -1
        total = 1

        
        for i, n in enumerate(nums):
            if n == 0 and hasZero == -1:
                hasZero = i
            else:
                total *= n
        for i in range(len(nums)):
            if hasZero == i:
                ret.append(total)
            elif hasZero != -1 or total == 0:
                ret.append(0)
            else:
                ret.append(int(total/nums[i]))
        return ret


            


        