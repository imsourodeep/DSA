// Last updated: 30/08/2026, 20:01:28
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i =0; i<nums.size(); i++){
            if (nums[i] == target){
                return i;
            }
            else if (nums[i]>target){
                return i;
            }
        }
        return nums.size();
    }
};