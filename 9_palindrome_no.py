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

        # Don't convert to string: ALTERNATIVE 1
        if x < 0:
            return False

        rev_num = 0
        digit = 0

        while(x // (10**digit) != 0):
            rev_num = (rev_num * 10) + (x // (10**digit) % 10)
            digit += 1

        return(x == rev_num)
        # Don't convert to string: ALTERNATIVE 2

        if x < 0:
            return False

        if x == 0:
            return True
        if x % 10 == 0:
             return False
        originalX = x
        numReversed = 0
        while(x > 0):
            lastDigit = x % 10
            numReversed = numReversed * 10 + lastDigit
            x = x // 10

        return numReversed == originalX
