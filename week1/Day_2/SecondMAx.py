   largest=nums[0]
     

        for i in range(1,len(nums)):
            if largest<nums[i]:
                largest=nums[i]
        second=None
        for i in range(len(nums)):
            if largest>nums[i]:
               if second  is None or second<nums[i]:
                        second=nums[i]

        return second
