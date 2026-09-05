# Last updated: 05/09/2026, 12:51:10
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen = set()
        special = set()

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                if nums[i] in seen:
                    special.discard(nums[i])
                else:
                    seen.add(nums[i])
                    special.add(nums[i])

        return len(special)