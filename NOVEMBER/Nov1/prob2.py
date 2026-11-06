def Stringcheck(strs):
    prefix=""
    i=0

    while i<len(strs):
        ch=strs[0][i]
        
        for word in strs:
            if i>=len(word) or word[i]!=ch:
                return prefix
            
        prefix+=ch
        i+=1
        
    return prefix
            
    
    