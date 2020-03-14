// URL: https://leetcode.com/problems/binary-watch/
// Author: liy
// Desc: Easy and interesting question abort binary
// Date: 2020-03-14 11:40

class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        char watch[6];
        vector<string> results;
        for (int i = 0; i < 1024; ++i) {
            int n = 0;
            int hour = 0;
            int minute = 0;
            for (int j = 0; j < 4; ++j) {
                if (i & (1 << j)) {
                    ++n;
                    hour += (1 << j);
                    if (hour > 11 || n > num) break;
                }
            }
            if (hour > 11 || n > num) continue;
            
            for (int j = 0; j < 6; ++j) {
                if (i & (1 << (j + 4))) {
                    ++n;
                    minute += (1 << j);
                    if (minute > 59 || n > num) break;
                }
            }
            if (minute > 59 || n != num) continue;
            
            sprintf(watch, "%d:%02d", hour, minute);
            results.push_back(watch);
        }
        return results;
    }
};