// Last updated: 24/08/2026, 21:48:35
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {

        if (magazine.length() < ransomNote.length())
            return false;

        unordered_map<char, int> freq;

        for (char ch : magazine) {
            freq[ch]++;
        }

        for (char ch : ransomNote) {

            if (freq[ch] == 0)
                return false;

            freq[ch]--;
        }

        return true;
    }
};