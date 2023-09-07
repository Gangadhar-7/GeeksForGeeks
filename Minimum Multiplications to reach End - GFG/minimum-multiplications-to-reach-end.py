#User function Template for python3

from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        que=deque()
        que.append((start,0))
        visited=set()
        while que:
            current_val,step=que.popleft()
            if current_val==end:
                return step
            for item in arr:
                next_val=(current_val*item)%(10**5)
                if next_val not in visited:
                    que.append((next_val,step+1))
                    visited.add(next_val)
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends