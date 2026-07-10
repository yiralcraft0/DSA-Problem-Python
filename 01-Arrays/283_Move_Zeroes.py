"""
283. Move Zeroes
Easy

    Hint
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

    Example 1:
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

    Example 2:
        Input: nums = [0]
        Output: [0]
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(1, len(nums)):
            if (nums[i] != 0 and nums[j] == 0):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            elif  nums[j] != 0:
                j += 1
        return nums
            

nums = [4,2,4,0,0,3,0,5,1,0]
print(f'{Solution().moveZeroes(nums)}')
