class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # for num in nums:
        #     count[num] += 1
        count = Counter(nums)
        sorted_dict = sorted(count.items(), key=lambda x: x[1], reverse=True)
        ret = []
        for i in range (k):
            ret.append(sorted_dict[i][0])

        return ret