def lowercase(s):
    result=[]
    
    for ch in s:
        if ch>="A" and ch<="Z":
            ch=chr(ord(ch)+32)
            
        result.append(ch)
        
    return "".join(result)