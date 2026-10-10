// Last updated: 10/10/2026, 21:20:15
1class Solution {
2public:
3    vector<int> maxProductPair(vector<int>& nums, int target) {
4        vector<int> ans = {-1,-1};
5        int prod = INT_MIN;
6
7        for(int i = 0; i<nums.size()-1; i++){
8            for(int j =i+1;j<nums.size(); j++){
9                if ((nums[i]+nums[j] == target) && (nums[i]>nums[j])){
10                    if (nums[i]*nums[j] >prod){
11                        prod = nums[i] *nums[j];
12                        ans = {i,j};
13                    }
14                }
15                else if ((nums[i]+nums[j] == target)&&(nums[j]>nums[i])){
16                    if (nums[i]*nums[j] >prod){
17                        prod = nums[i] *nums[j];
18                        ans = {j,i};
19                    }
20                }
21            
22            }
23        }
24        return ans;
25    }
26};