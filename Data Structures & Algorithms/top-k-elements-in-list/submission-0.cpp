class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt_map;
        for (int n : nums) {
            cnt_map[n] += 1;
        }
        vector<vector<int>> freq(nums.size() + 1);
        for (auto& cnt_pair : cnt_map) {
            freq[cnt_pair.second].push_back(cnt_pair.first);
        }

        for (int i = freq.size() - 1; i > 0; i--) {
            for (int n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }
    }
};
