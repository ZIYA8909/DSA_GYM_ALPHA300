class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        begin=0
        ans=0
        total=0
        

        for end in range(len(nums)):
            total+=nums[end]

            while total>=target:
                length= end-begin+1

                if ans==0 or length<ans:
                    ans =length

                total-=nums[begin]
                begin+=1
    
        return ans