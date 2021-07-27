# Leetcode problem #215 https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # since the number should be in a sorted list, first we are going to sort the list
        nums = sorted(nums, reverse=True)
        if k < (len(nums) - k):
            return nums[k-1]
        else:
            return nums[k-len(nums)-1]
