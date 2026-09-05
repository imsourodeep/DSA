// Last updated: 05/09/2026, 20:50:15
class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        for (int i = 0; i<nums.size(); i++){
            int mxe = *max_element(nums.begin(),nums.begin()+i+1);
            int mne = *min_element(nums.begin()+i,nums.end());
            if ((mxe-mne)<=k){
                return i;
            }
        }
        return -1;
    }
};