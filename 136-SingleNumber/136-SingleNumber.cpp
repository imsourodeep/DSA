// Last updated: 31/08/2026, 20:45:58
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i<nums.size(); i++){
            ans = ans ^ nums[i];
        }
        return ans;
    }
};