// Last updated: 08/09/2026, 20:41:35
class Solution {
public:
    int countCommas(int n) {
        if (n < 1000){
            return 0;
        }
        return (n-999);
    }
};