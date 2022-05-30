Question Link: 
https://leetcode.com/problems/search-a-2d-matrix/
Question description:
To write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Code:


Brute Force Approach:
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = matrix[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(target==matrix[i][j])return true;
            }
        }
        return false;
    }
};

Time Complexity - O(n*m)
Space Complexity - O(1)

Better Approach:
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {  
        int n = matrix.size();
        int m = matrix[0].size();
        int i=0,j=m-1;
        while(i<n && j>=0){
            if(target>matrix[i][j]){
                i++;
            }else if(target==matrix[i][j]){
                return true;
            }else{
                j--;
            }
        }
        return false;
    }
};

Time Complexity - O(n+m)
Space Complexity - O(1)

Optimal Approach:
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = matrix[0].size();
        int low=0,high=(n*m)-1;
        while(low<=high){
            int mid = low + (high-low)/2;
            if(matrix[mid/m][mid%m]==target)return true;
            else if(matrix[mid/m][mid%m]<target){
                low = mid+1;
            }else{
                high = mid-1;
            }
        }
        return false;
    }
};

Time Complexity - O(log(n*m))
Space Complexity - O(1)


Video Solution Link:
https://drive.google.com/file/d/1YCZcJBRnuqBFs21t5a4XVC3yg0n-9DuF/view?usp=sharing
