nums = [2,5,5,11]
target = 10


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().two_sum(nums, target))