// URL: https://leetcode.com/problems/longest-palindrome/
// Author: liy
// Desc: Easy Question
// Date: 2020-03-22

class Solution {
public:
    int longestPalindrome(string s) {
        int result = 0;
        vector<int> tempVec(255, 0);
        for (int i = s.size() - 1; i >= 0; --i) {
            tempVec[s[i]] += 1;
            if (tempVec[s[i]] == 2) {
                result += 2;
                tempVec[s[i]] = 0;
            }
        }
        if (result != s.size()) result++;
        return result;
    }
};