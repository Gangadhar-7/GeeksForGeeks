#User function Template for python3
class Solution:
    def firstElement (self, n):
        # code here 
        
        x=[0,1]
        y=2
        if n==0:
            return 0
        elif n<=2:
            return 1
        else:
            while y<=n :
                x.append(x[-1]+x[-2])
                y+=1
            
            return x[-1]%1000000007

                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends