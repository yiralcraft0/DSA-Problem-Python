"""
242. Valid Anagram
Easy
    Companies
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Example 1:
        Input: s = "anagram", t = "nagaram"
        Output: true

    Example 2:
        Input: s = "rat", t = "car"
        Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        return True


s = "aacc"
t = "ccac"

print(Solution().isAnagram(s , t))
