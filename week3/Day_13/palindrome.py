m=len(s1)
n=len(s2)

if m>n:
    return False

need={}
window={}

for ch in s1:
    if ch in need:
        need[ch]+=1
    else:
        need[ch]=1
        
for i in range(m):
    ch=s2[i]
    if ch in window:
        window[ch]+=1
    else:
        window[ch]=1
        
if window==need:
    return True

for right in range(m,n):
    outgoing=s2[right-m]
    incoming=s2[right]
    
    window[outgoing]-=1
    
    if window[outgoing]==0:
        del window[outgoing]
        
    if incoming in window:
        window[incoming]+=1
    else:
        window[incoming]=1
        
    if window==need:
        return True

return False

        
