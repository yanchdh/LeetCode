// URL: https://leetcode.com/problems/trapping-rain-water-ii/
// Author: liy
// Desc: Interesting question, Challenged, 
// Date: 2020-03-21

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        int result = 0;
        int m = heightMap.size();
        if (m == 0) return result;
        int n = heightMap[0].size();
        vector<vector<int>> temp = heightMap;
        for (int i = 1; i < m - 1; i++)
            for (int j = 1; j < n - 1; j++)
                temp[i][j] = max(heightMap[i][j], min(temp[i - 1][j], temp[i][j - 1]));

        for (int i = m - 2; i > 0; i--)
            for (int j = n - 2; j > 0; j--)
                temp[i][j] = max(heightMap[i][j], min(temp[i][j], min(temp[i + 1][j], temp[i][j + 1])));

        for (int i = 1; i < m - 1; i++)
            for (int j = 1; j < n - 1; j++)
                recompute(temp, heightMap, m, n, i, j);

        for (int i = 1; i < m - 1; i++)
            for (int j = 1; j < n - 1; j++)
                result += temp[i][j] - heightMap[i][j];
        return result;
    }
    
    void recompute(vector<vector<int>>& temp, const vector<vector<int>>& heightMap, int m, int n, int i, int j) {
        if (i == 0 || j == 0 || i == m - 1 || j == n - 1) return;
        int height = max(heightMap[i][j], min(temp[i][j], min(temp[i - 1][j], min(temp[i][j - 1], min(temp[i + 1][j], temp[i][j + 1])))));
        if (height == temp[i][j]) return;
        temp[i][j] = height;
        recompute(temp, heightMap, m, n, i + 1, j);
        recompute(temp, heightMap, m, n, i - 1, j);
        recompute(temp, heightMap, m, n, i, j + 1);
        recompute(temp, heightMap, m, n, i, j - 1);
    }
};