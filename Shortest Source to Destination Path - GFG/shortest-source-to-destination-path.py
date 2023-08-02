#User function Template for python3
#User function Template for python3
from collections import deque

class Solution:
    
    def shortestDistance(self,N,M,grid,X,Y):
        #code here
        if grid[0][0]==0:return -1
        n=len(grid)
        que=[(0,0,0)]
        grid[0][0]=0
        direc=[(0,1),(1,0),(-1,0),(0,-1)]

        x=0
        while que:
            
            for _ in range(len(que)):
                i,j,val= que.pop(0)
                # print(i,j,val)
                if i==X and j==Y:
                    return val
                
                
                # print(i,j,val)
                for a , b in direc:
                    r=a+i
                    c=b+j
                    # print(r,c)
                    
                    if r<0 or c<0 or r>=n or c>=len(grid[0]) or grid[r][c]==0:
                        continue
                    
                    que.append((r,c,val+1))
                    # print(que)
                    grid[r][c]=0
        return -1
        
            
       


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends