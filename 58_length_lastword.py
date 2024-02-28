'''
Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal
substring consisting of non-space characters only.
Input: s = "Hello World" Output: 5 Input: s = "   fly me   to   the moon  " Output: 4
'''
def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        """ s = s.strip()
        words = s.split()
        return len(words[-1]) """

        i , length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
