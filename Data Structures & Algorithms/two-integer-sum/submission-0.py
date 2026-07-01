class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm: dict[int,int] = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement not in hm:
                hm[num] = index
            else:
                return [hm[complement],index]
            