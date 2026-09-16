class Solution {
public:
    int minOperations(vector<int>& nums) {
        // 1000*10^5

        int ops = 0;

        for (int i = nums.size() - 2; i >= 0; i--) {
            if (nums[i] <= nums[i+1]) {
                continue;
            }

            int j = max(2.0, ceil((double)nums[i] / nums[i + 1]));
            for (; j < nums[i]; j++) {
                if (nums[i] % j == 0) {
                    nums[i] /= j;
                    ops++;
                    break;
                }
            }
            if (nums[i] > nums[i+1]) {
                return -1;
            }
        }

        return ops;
    }
};