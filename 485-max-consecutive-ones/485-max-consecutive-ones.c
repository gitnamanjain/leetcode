int findMaxConsecutiveOnes(int* nums, int numsSize){
    int count=0,coone=0;
    for (int i = 0; i<numsSize;i++)
    {
        if(nums[i]==1)
        {
            ++count;
        }
        else if(nums[i]==0){
            if(count>coone)
            {
                coone=count;
            }
            count=0;
        }
    }
    if(count>coone)
            {
                coone=count;
            }
    return coone;
}