nums=[1,2,3,1,4,5]
k = 5

ans=0

for start in range(len(nums)):
    total=0
    
    for end in range(start,len(nums)):
        total+=nums[end]
        
        if total==k:
            length=end-start+1
            
            if length>ans:
                ans=length
                
print(ans)
    
