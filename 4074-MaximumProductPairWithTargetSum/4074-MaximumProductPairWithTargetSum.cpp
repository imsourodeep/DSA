// Last updated: 13/10/2026, 19:55:56
class Solution {
public:
    vector<int> maxProductPair(vector<int>& nums, int target) {
        vector<int> ans = {-1,-1};
        int prod = INT_MIN;

        for(int i = 0; i<nums.size()-1; i++){
            for(int j =i+1;j<nums.size(); j++){
                if ((nums[i]+nums[j] == target) && (nums[i]>nums[j])){
                    if (nums[i]*nums[j] >prod){
                        prod = nums[i] *nums[j];
                        ans = {i,j};
                    }
                }
                else if ((nums[i]+nums[j] == target)&&(nums[j]>nums[i])){
                    if (nums[i]*nums[j] >prod){
                        prod = nums[i] *nums[j];
                        ans = {j,i};
                    }
                }
            
            }
        }
        return ans;
    }
};