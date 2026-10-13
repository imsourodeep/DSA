# Last updated: 13/10/2026, 19:55:40
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        for i in range(len(nums)):
4            if nums[i]<0:
5                nums[i] = abs(nums[i])
6        nums.sort(reverse=True)
7        nn = []
8        i = 0
9        j = len(nums)-1
10        k = 0
11        while i<=j:
12            if k%2==0:
13                nn.append(nums[i])
14                i+=1
15                k+=1
16            else:
17                nn.append(nums[j])
18                j-=1
19                k+=1
20        print(nn)
21        ans = 0
22        for i in range(len(nn)):
23            if i%2 == 0:
24                ans += nn[i]*nn[i]
25            else:
26                ans -= nn[i]*nn[i]
27        return ans
28