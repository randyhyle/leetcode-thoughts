# Problem 242 Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Intuition: Since an anagram is only true if they are the same length
        # We can first check if they are the same length.
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        # Than we count each character and add them to our dictionary to count
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # Get function is especially helpful here. If it doesn't exist already
        # It will assign that value to the dictionary with a value of 0.
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True