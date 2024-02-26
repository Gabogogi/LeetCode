"""
    Given an integer x, return true if x is a
     palindrome, and false otherwise
     Input: x = 121Output: true Input: x = -121Output: false
    x = 10Output: false
"""
def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return(str(x) == str(x)[::-1])
