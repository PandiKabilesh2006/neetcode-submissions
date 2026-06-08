
class Solution:
    def uniquePaths(self, m, n):
        # code here
        #Recursion
        delrow=[0,1]
        delcol=[1,0]
        
        #Recursion
        # def recursion(row,col):
        #     if(row==m-1 and col==n-1):
        #         return 1
        #     count=0
        #     for i in range(2):
        #         nrow=row+delrow[i]
        #         ncol=col+delcol[i]
        #         if(0<=nrow<m and 0<=ncol<n):
        #             count+=recursion(nrow,ncol)
        #     return count
        # return recursion(0,0)
        
        #Memoization
        # dp=[[-1]*n for i in range(m)]
        # def recursion(row,col):
        #     if(row==m-1 and col==n-1):
        #         return 1
        #     if(dp[row][col]!=-1):
        #         return dp[row][col]
        #     count=0
        #     for i in range(2):
        #         nrow=row+delrow[i]
        #         ncol=col+delcol[i]
        #         if(0<=nrow<m and 0<=ncol<n):
        #             count+=recursion(nrow,ncol)
        #     dp[row][col]=count
        #     return dp[row][col]
        # return recursion(0,0)
        
        #Tabulation
        # dp=[[0]*n for i in range(m)]
        # dp[m-1][n-1]=1
        # for row in range(m-1,-1,-1):
        #     for col in range(n-1,-1,-1):
        #         if(row==m-1 and col==n-1):
        #             continue
        #         count=0
        #         for i in range(2):
        #             nrow=row+delrow[i]
        #             ncol=col+delcol[i]
        #             if(0<=nrow<m and 0<=ncol<n):
        #                 count+=dp[nrow][ncol]
        #         dp[row][col]=count
        # return dp[0][0]
        
        #Space optimization
        nxt=[0]*n
        nxt[n-1]=1
        for row in range(m-1,-1,-1):
            curr=[0]*n
            for col in range(n-1,-1,-1):
                if(row==m-1 and col==n-1):
                    curr[col]=1
                    continue
                down=0
                right=0
                if(0<=row+1<m):
                    down=nxt[col]
                if(0<=col+1<n):
                    right=curr[col+1]
                curr[col]=down+right
            nxt=curr
        return nxt[0]
    
        