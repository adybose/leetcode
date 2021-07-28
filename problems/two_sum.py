# Leetcode problem #1 https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using a dict to store the items iterated/visited/seen
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen.keys():
                return ([seen[target-nums[i]], i])
            seen[nums[i]] = i
