#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        m=1000000007
        
        mul=1
        while R:
            if R%2==1:
                mul= ((mul%m)*(N%m))%m
                R-=1
            else:
                N=((N%m)*(N%m))%m
                R=R//2
    
        return (mul)%m
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends