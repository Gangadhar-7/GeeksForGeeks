# User function Template for Python3

class Solution:
    def maxLength(self, S):
        # code here
        stack=[]
        check=[0]*len(S)
        for i,j in enumerate(S):
            if j=="(":
                stack.append(i)
            else:
                if stack:
                    check[stack.pop()]=1
                    check[i]=1

        
        count=0
        maxi=0
        for i in check:
            if i==1:
                count+=1
            else:
                maxi=max(maxi,count)
                count=0
        maxi=max(maxi,count)
        return maxi
        


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends