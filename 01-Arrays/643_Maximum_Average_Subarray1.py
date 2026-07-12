"""
643. Maximum Average Subarray I
Easy
    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

    Example 1:
        Input: nums = [1,12,-5,-6,50,3], k = 4
        Output: 12.75000
        Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

    Example 2:
        Input: nums = [5], k = 1
        Output: 5.00000
"""

class Solution:
    # Time: O(n)
    # Space: O(k) because nums[:k] creates a new list containing the first k elements.
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        total = sum(nums[:k])
        maxAvg = float('-inf')
        
        left = 0
        right = k - 1

        while True:
            avg = total/k
            maxAvg = max(maxAvg, avg)

            if (right + 1) < len(nums):
                total -= nums[left]
                right += 1
                total += nums[right]
                left += 1
            else:
                break
            
        return maxAvg
    
    # More Simple Way / More Readable
    def findMaxAverage2(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        left = 0

        for right in range(k, len(nums)):
            window_sum -= nums[left]
            window_sum += nums[right]
            left += 1

            max_sum = max(max_sum, window_sum)

        return max_sum / k
        
nums = [0,1,1,3,3]
k = 4

print(f'{Solution().findMaxAverage(nums , k)}')
print(f'{Solution().findMaxAverage2(nums , k)}')
