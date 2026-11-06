class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """

        words=title.split()
        result=[]
        for word in words:
            new=""
            for i in range(len(word)):
                ch=word[i]
                if len(word)<=2:
                    if ch>="A" and ch<="Z":
                        ch=chr(ord(ch)+32)

                else:
                    if i==0:
                        if ch>="a" and ch<="z":
                            ch=chr(ord(ch)-32)
                    else:
                        if ch>="A" and ch<="Z":
                            ch=chr(ord(ch)+32)
                
                new +=ch
        
            result.append(new)

        return " ".join(result)
        