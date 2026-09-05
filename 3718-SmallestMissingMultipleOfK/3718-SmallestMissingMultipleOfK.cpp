// Last updated: 05/09/2026, 12:51:37
class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        unordered_set<int> s(nums.begin(),nums.end());
        int i = 1;
        while(true){
            int target = k*i;
            if (s.count(target)==0){
                return target;
            }
            i++;
        }

    }
};