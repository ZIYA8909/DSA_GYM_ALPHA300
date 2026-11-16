class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        longest=0
        left=0

        for right in range(len(s)):
            c=s[right]
            if c in freq and freq[c]>=left:
                left=freq[c]+1

            freq[c]=right

            length=right-left+1

            if length>longest:
                longest=length
        return longest 

