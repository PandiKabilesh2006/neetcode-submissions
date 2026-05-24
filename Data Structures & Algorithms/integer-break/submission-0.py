class Solution:
    def integerBreak(self, n: int) -> int:
        nums=list(range(1,n))
        length=len(nums)
        #Recursion
        # def recursion(ind,total):
        #     if(ind==length-1):
        #         if(total==n):
        #             return 1
        #         elif((n-total)%nums[ind]==0):
        #             return nums[ind]**((n-total)//nums[ind])
        #         return float('-inf')
            
        #     take=float('-inf')
        #     if(total+nums[ind]<=n):
        #         take=nums[ind]*recursion(ind,total+nums[ind])
        #     nottake=recursion(ind+1,total)
        #     return max(take,nottake)
        # return recursion(0,0)

        #Memoization
        dp=[[-1]*(n+1) for i in range(length)]
        def recursion(ind,total):
            if(ind==length-1):
                if(total==n):
                    return 1
                elif((n-total)%nums[ind]==0):
                    return nums[ind]**((n-total)//nums[ind])
                return float('-inf')
            if(dp[ind][total]!=-1):
                return dp[ind][total]
            
            take=float('-inf')
            if(total+nums[ind]<=n):
                take=nums[ind]*recursion(ind,total+nums[ind])
            nottake=recursion(ind+1,total)
            dp[ind][total]=max(take,nottake)
            return dp[ind][total]
        return recursion(0,0)
        
        