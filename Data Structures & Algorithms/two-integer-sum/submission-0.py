class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in storage:
                return [storage[complement], i]
            else:
                storage[num] = i