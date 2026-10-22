class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
    ans=[]

    if len(p)>len(s):
        print "invalid" 

    for i in range(len(s)-len(p)+1):
        input={}
        for z in p:
            if z in input:
                input[z]+=1
            else:
                input[z]=1
       for y in range(i,i+len(p)):
				 		z=s[y]

						
        
