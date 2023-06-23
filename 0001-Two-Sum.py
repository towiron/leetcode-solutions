class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for indx, num in enumerate(nums):
            hashmap[num] = indx

        for indx, num in enumerate(nums):
            diff = target - num
            if diff in hashmap and indx != hashmap[diff]:
                return [indx, hashmap[diff]]

        return []