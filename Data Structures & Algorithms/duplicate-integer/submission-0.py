class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash: dict[int,int] = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        for num in hash:
            if hash[num] > 1:
                return True
            else:
                continue
        return False