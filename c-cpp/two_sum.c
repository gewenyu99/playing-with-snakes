# solution to: https://leetcode.com/accounts/login/?next=/problems/two-sum/description/
# brute force because C :)
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *retArr = malloc(sizeof(int)*2);
    retArr[0] = 0;
    retArr[1] = 0;
    for (int i = 0; i < numsSize; i++){
        for(int j = (i+1); j < numsSize; j++){
            if (nums[i] + nums[j] == target) {
                retArr[0] = i;
                retArr[1] = j;
                return retArr;
            }
        }
    }
    return retArr;
}