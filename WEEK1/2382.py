class UnionFind:
    def __init__(self, size, nums):
        self.size = size + 1
        self.sz = [1 for i in range(self.size)]
        self.par = [-1 for i in range(self.size)]
        self.segsum = [0 for i in range(self.size)]
        
        for i in range(1, self.size):
            self.segsum[i] = nums[i-1]
        
            
    def find(self, i):
        if self.par[i] == i:
            return i
        self.par[i] = self.find(self.par[i])
        return self.par[i]
    
    def union(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 == root2:
            return
        
        if(self.sz[root1] < self.sz[root2]):
            root1, root2 = root2, root1

        self.sz[root1] += self.sz[root2]
        self.par[root2] = root1
        self.segsum[root1] += self.segsum[root2]


class Solution:
    def maximumSegmentSum(self, nums: List[int], query: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind(n, nums)
           
        ans = [0]        
        maxsegsum = -float("inf")
        
        #for 1 based indexing
        for i in range(n):
            query[i] += 1
            
        for i in range(n-1, 0, -1):
            #create a new segment for the element corresponding to ith query
            uf.par[query[i]] = query[i]
                
            #try to merge with left
            if(query[i] - 1 >= 0 and uf.par[query[i] - 1] != -1):
                uf.union(query[i], query[i]-1)
            
            #try to merge with right
            if(query[i] + 1 <= n and uf.par[query[i] + 1] != -1):
                uf.union(query[i], query[i]+1)

            #update maximum segment sum
            maxsegsum = max(maxsegsum, uf.segsum[uf.find(query[i])])
            ans.append(maxsegsum)
            
        ans = ans[::-1]
        return ans
                
                     
            
            
            
        