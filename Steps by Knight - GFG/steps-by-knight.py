from collections import deque
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    
	    
	   
	    
	    row = KnightPos[0] - 1
	    col = KnightPos[1] - 1
	    
	    dist = (TargetPos[0] -1, TargetPos[1] - 1)

	    queue = deque([(row, col, 0)])
	    
        direc = [(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2), (-2,-1), (-1,-2)]
	    
	    visited = set()
	    
	    while queue:
	        i,j, step = queue.popleft()
	        
	        if (i,j) == dist: return step
	    
	        for a,b in direc:
	            row= a+ i
	            col= b + j
	            if not 0 <= row < N or not 0 <= col < N : continue
	            
	            if (row, col) not in visited:
	                queue.append((row, col, step + 1))
	                visited.add((row, col))
	        
	    return -1
		    


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends