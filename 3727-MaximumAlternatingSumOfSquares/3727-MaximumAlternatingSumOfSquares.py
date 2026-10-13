# Last updated: 13/10/2026, 19:56:16
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = abs(nums[i])
        nums.sort(reverse=True)
        nn = []
        i = 0
        j = len(nums)-1
        k = 0
        while i<=j:
            if k%2==0:
                nn.append(nums[i])
                i+=1
                k+=1
            else:
                nn.append(nums[j])
                j-=1
                k+=1
        print(nn)
        ans = 0
        for i in range(len(nn)):
            if i%2 == 0:
                ans += nn[i]*nn[i]
            else:
                ans -= nn[i]*nn[i]
        return ans
