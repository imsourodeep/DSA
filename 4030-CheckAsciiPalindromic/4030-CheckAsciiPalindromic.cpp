// Last updated: 05/09/2026, 12:51:11
class Solution {
public:
    bool isPalindromic(string s) {

        string val = "";

        for (char ch : s) {

            int num = ch;
            string bin = "";

            while (num > 0) {
                bin += char('0' + num % 2);
                num /= 2;
            }

            reverse(bin.begin(), bin.end());

            while (bin.length() < 8) {
                bin = "0" + bin;
            }

            val += bin;
        }

        return val == string(val.rbegin(), val.rend());
    }
};