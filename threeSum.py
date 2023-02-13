class Solution:
    def threeSumMulti(self, arr, target: int) -> int:
        count=0
        result=0
        mod=10**9+7
        for i in range(len(arr)):
            hashmap={}
            for j in range(i+1,len(arr)):
                k=target-(arr[i]+arr[j])
                if(k>=0 and k<=100 and k in hashmap ):
                    result+=hashmap[k]
                    result%=mod
                if(arr[j] not in hashmap):
                    hashmap[arr[j]]=0
                hashmap[arr[j]]+=1
                    
        return result

