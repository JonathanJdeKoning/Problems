class Solution {
public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        vector<string> ans {words[0]};
        int curr {groups[0]};

        for (int i = 1; i < groups.size(); i++) {
            if (groups[i] != curr) {
                curr = groups[i];
                ans.push_back(words[i]);
            }
        } 
        return ans;
    }
};