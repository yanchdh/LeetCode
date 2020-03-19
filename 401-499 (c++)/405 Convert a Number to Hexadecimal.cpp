// URL: https://leetcode.com/problems/convert-a-number-to-hexadecimal/
// Author: liy
// Desc: binary, 2's complement
// Date: 2020-03-19

class Solution {
public:
    string toHex(int num) {
        static const char* HEX = "0123456789abcdef";
        if (num == 0) return "0";
        long long temp = num;
        if (temp < 0) temp = ((-temp ^ 0xFFFFFFFF) + 1);
        string result;
        while (temp) {
            result.push_back(HEX[temp % 16]);
            temp /= 16;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};