class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        for i in range(1,n//2+1):
            if n%i==0:
                part=s[:i]
                if  part*(n//i)==s:
                    return True
        return False
