class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        result = {key: nums.count(key) for key in set(nums)}
        for i in result:
            if result[i]>(n/2):
                return i

        