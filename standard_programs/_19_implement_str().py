'''Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "hello", needle = "ll"
Output: 2'''
class ImplementStr:
    def first_occurence(self,haystack,needle):
        print(haystack.find(needle))
        # Base conditions
        if haystack is None or needle is None:
            return -1
        # Special case
        if haystack == needle:
            return 0

haystack="rakshitha"
needle="rakshitha"
obj=ImplementStr()
(obj.first_occurence(haystack,needle))