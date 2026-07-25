class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one, two = 0, len(numbers) -1

        while numbers[one] + numbers[two] != target:
            while numbers[one] + numbers[two] > target:
                two -= 1
            while numbers[one] + numbers[two] < target:
                one += 1
        return [one+1, two+1]
    # completed in less than 8 minutes and passed first try!!!!!!!!!!!!
    
        