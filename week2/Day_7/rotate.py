

nums=[1,2,3,4,5]
first=nums[0]
#left
for i in range(len(nums)-1):
    nums[i]=nums[i+1]
    
nums[len(nums)-1]=first  
    
print(nums)
#right
#last=nums[len(nums)-1]
#for i in range(len(nums)-1,0,-1):
#    nums[i]=nums[i-1]
    
#nums[0]=last  
    
#print(nums)