nums=[1,2,3,4,2]
k=3
check={}
for i in range(len(nums)):
    if nums[i] in check:
        if i-check[nums[i]]<=k:
            print(True)  #got an error when i wrote true as python accepts only "True"
            break
    check[nums[i]]=i
else:
    print(False)
    
#could have used return as well

#for i in range(len(nums)):
    #if nums[i] in check:
        #if i-check[nums[i]]<=k:
            #return True
            
    #check[nums[i]]=i
#else:
    #return False
