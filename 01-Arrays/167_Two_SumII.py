"""
167. Two Sum II - Input Array Is Sorted
Medium

    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.

    Example 1:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

    Example 2:
        Input: numbers = [2,3,4], target = 6
        Output: [1,3]
        Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

    Example 3:
        Input: numbers = [-1,0], target = -1
        Output: [1,2]
        Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:
    # Brute force solutions---------------------------
    # time complexity: O(nlog(n)
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            diff = target - numbers[i]

            low = 0
            high = len(numbers) - 1

            while low <= high:
                mid = (high + low) // 2

                if numbers[mid] == diff and mid != i:
                    return [min(i + 1, mid + 1), max(i + 1, mid + 1)]
                elif numbers[mid] > diff:
                    high = mid - 1
                else:
                    low = mid + 1
        else:
            return [-1, -1]


    # Optimised Way-------------------------------
    # time complexity: O(log(n))
    # by using Binary Search
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        low = 0
        high = len(numbers) - 1

        while low <= high:
                
            total = numbers[low] + numbers[high]

            if total == target:
                return [low + 1, high + 1]
            elif total > target:
                high -= 1
            else:
                low += 1
        
        return [-1, -1]
        

numbers = []
target = 9

print(f'{Solution().twoSum(numbers , target)}')
