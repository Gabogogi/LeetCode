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
        #return(str(x) == str(x)[::-1]) #reverses string and checks if its same

        # Don't convert to string
        if x < 0:
            return False

        rev_num = 0
        digit = 0

        while(x // (10**digit) != 0):
            rev_num = (rev_num * 10) + (x // (10**digit) % 10)
            digit += 1

        return(x == rev_num)
