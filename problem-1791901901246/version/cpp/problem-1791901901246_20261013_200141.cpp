// Last updated: 13/10/2026, 20:01:41
1class Solution {
2public:
3    long long maxAlternatingSum(vector<int>& nums) {
4        int n = nums.size();
5        vector<long long> a(n);
6        for (int i = 0; i < n; i++)
7            a[i] = 1LL * nums[i] * nums[i];
8
9        sort(a.begin(), a.end());
10
11        long long ans = 0;
12        int k = n / 2;   
13
14        
15        for (int i = 0; i < k; i++)
16            ans -= a[i];
17
18        for (int i = k; i < n; i++)
19            ans += a[i];
20
21        return ans;
22    }
23};