'''Write a function to find the longest common prefix string amongst an array of strings
If there is no common prefix, return an empty string '''


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        commonPrefix = strs[0]
        for string in strs:
            commonPrefix = self.findPrefix(commonPrefix, string)

        return commonPrefix

    def findPrefix(self, prefix, string):
        while prefix is not "":

            if string.startswith(prefix):

                return prefix
            else:
                prefix = prefix[:-1]

        return ""
s=Solution()
strs = ["flower","flow","flight"]
s.longestCommonPrefix(strs)
s.findPrefix(prefix, string)