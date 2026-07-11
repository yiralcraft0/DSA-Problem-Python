"""
75. Sort Colors
Medium
    Hint
        Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

        You must solve this problem without using the library's sort function.

    Example 1:
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]

    Example 2:
        Input: nums = [2,0,1]
        Output: [0,1,2]
"""

class Solution:

    # Simple But Inlegal way🙄🤫
    # 🕒 Time Complexity: O(log(n))
    # 💾 Space Complexity: O(1)
    def sortColors1(self, nums: list[int]) -> None:
        nums.sort()
    
    # Legal way/Optimised solutions---------------------------
    # By two pointer
    # 🕒 Time Complexity: O(n)
    # 💾 Space Complexity: O(1)

    def sortColors2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arrLen = len(nums)
        
        l = 0
        m = 0
        h = arrLen - 1

        while m <= h :                                                          
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                m += 1
                l += 1

            elif nums[m] == 1:
                m += 1
            
            else:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
            
        return nums



nums = [2,0,2,1,1,0]

print(f'{Solution().sortColors(nums)}')
