// Last updated: 03/09/2026, 20:22:12
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n==1){return true;}
        long mul = 1;
        while (mul <= n){
            if (n == mul){
                return true;
            }
            mul = mul * 2;
        }
        return false;
    }
};