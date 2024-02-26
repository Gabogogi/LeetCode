"""
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.
Input: strs = ["flower","flow","flight" Output: "fl"
Input: strs = ["dog","racecar","car"] Output: ""
only lowercase characters
"""

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                  if i == len(s) or s[i] != strs[0][i]:
                        return res
            res += strs[0][i]
        return res
