# Last updated: 14/09/2026, 18:35:04
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        arr = []
        count = 0
        for ele in nums:
            if ele not in arr and nums.count(ele)==3:
                arr.append(ele)

        i1 = i2 = i3 = 0
        for ele in arr:
            for i in range(len(nums)):
                if nums[i] == ele:
                    i1= i2
                    i2 = i3
                    i3 = i
            if (i1<i and i2<i3) and ((i2-i1)==(i3-i2)):
                count += 1
        return count
        