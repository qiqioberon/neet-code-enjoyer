class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> res;
        int count = 0;
        for (int i = 0; i<= nums.size(); i++){
            if(i == nums.size()) i = 0;
            if (res.size()==2*nums.size()) break;
            res.push_back(nums[i]);
        }
        return res;
    }
};