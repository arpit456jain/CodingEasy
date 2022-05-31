Ouestion Link:
https://leetcode.com/problems/find-the-duplicate-number/

Code:

Brute force: 
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n=nums.size(),ans;
        sort(nums.begin(),nums.end());
        for(int i=0;i<n-1;i++){
            if(nums[i]==nums[i+1]){
                ans=nums[i];
                break;
            }
        }
        return ans;
    }
};

Time Complexity: O(N*logN)

Optimised approach:
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n=nums.size(),ans;
        vector<int> freq(n,0);
        for(int i=0;i<n;i++){
            freq[nums[i]]++;
            if(freq[nums[i]]>1){
                ans=nums[i];
                break;
            }
        }
        return ans;
    }
};

Time Complexity: O(N)

Video Solution Link:
https://drive.google.com/file/d/1oU1bbjMtJFBEenbW3r0Jho5NERbnRtNo/view?usp=sharing
