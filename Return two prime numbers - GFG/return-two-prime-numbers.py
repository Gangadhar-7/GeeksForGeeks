#User function Template for python3

class Solution:
    def primeDivision(self, N):
        # code here
        def isprime(n):
            if (n==1):
                return false;
            
            
            for i in range(2,n):
                if i*i>n:break
                if (n%i==0):
                    return False
                    
            return True
        res=[]
        for k in range(2,N):
            if (isprime(k) and isprime(N-k)):
                res.append(k)
                res.append(N-k)
                break
    
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends