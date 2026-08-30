// Last updated: 30/08/2026, 20:01:11
class Solution {
public:
    bool detectCapitalUse(string word) {
        int count = 0;
        for(int i = 0; i< word.size(); i++){
            if (isupper(word[i])){
                count++;
            }
        }
        if ((count == word.size()) || count ==0){
            return true;
        }
        else if (count == 1){
            if (isupper(word[0])){
                return true;
            }
        }
        return false;
        
    }
};