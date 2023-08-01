#User function Template for python3


def find(arr,n,x):
    # code here
    if x in arr:
        return [arr.index(x),n-(arr[::-1].index(x))-1]
    return [-1,-1]



#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends