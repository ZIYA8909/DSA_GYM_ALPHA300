class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result=""

        for ch in address:
            if ch==".":
                result+="[.]"
            else:
                result+=ch
        return result
        
