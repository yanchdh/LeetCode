// URL: https://leetcode.com/problems/frog-jump/
// Author: liy
// Desc: A dynamic programming problem
// Date: 2020-03-16

class Solution {
public:
    bool canCross(vector<int>& stones) {
        m_stoneNum = stones.size();
        m_flag.resize(m_stoneNum, vector<char>(m_stoneNum, -1));
        return canCross(stones, 0, 1) == 1;
    }
    
    bool canCross(vector<int>& stones, int i, int k) {
        if (k <= 0)
            return 0;
        if (m_flag[i][k] != -1)
            return m_flag[i][k];
        int x = stones[i] + k;
        if (x <= 0)
            return 0;
        int j = lower_bound(stones.begin(), stones.end(), x) - stones.begin();
        if (j > 0 && j < m_stoneNum && stones[j] == x &&
            (j + 1 == m_stoneNum || canCross(stones, j, k - 1) || canCross(stones, j, k) || canCross(stones, j, k + 1)))
            m_flag[i][k] = 1;
        else
            m_flag[i][k] = 0;
        return m_flag[i][k];
    }
    vector<vector<char>> m_flag;
    int m_stoneNum;
};