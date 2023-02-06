# Problem 217: Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Instinctual solution
        # Iterate through the array once and add each value to a set.
        # If the value is in the set already than return True, otherwise False
        dupe = set()
        for i in nums:
            if i in dupe:
                return True
            dupe.add(i)
        return False
