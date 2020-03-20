// URL: https://leetcode.com/problems/queue-reconstruction-by-height/
// Author: liy
// Desc: Interesting question, medium difficulty evaluation is correct
// Date: 2020-03-20

class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        int people_count = people.size();
        if (people_count < 2) return people;
        sort(people.begin(), people.end());
        int j = people_count - 1;
        while (j - 1 >= 0 and people[j][0] == people[j - 1][0]) j--;
        int x = 0;
        while (j >= 0) {
            int h = people[j][0], k = people[j][1];
            if (x == 0) while (j - x - 1 >= 0 && people[j - x - 1][0] == h) x++;
            else x--;
            for (int i = 0; i < k - x; ++i) {
                people[j + i][0] = people[j + i + 1][0];
                people[j + i][1] = people[j + i + 1][1];
            }
            people[j + k - x][0] = h;
            people[j + k - x][1] = k;
            j--;
        }
        return people;
    }
};