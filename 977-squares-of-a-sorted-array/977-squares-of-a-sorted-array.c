int* sortedSquares(int* nums, int numsSize, int* returnSize){
    *returnSize=numsSize;
	int *arr=malloc(sizeof(int)*numsSize);
	for (int i=0;i<numsSize;i++){
		arr[i]=nums[i];
	}
	int temp;
	for (int i=0;i<numsSize;i++){
        arr[i]=arr[i]*arr[i];
	}
    for (int i=0;i<numsSize-1;i++){
		for(int j=0; j<numsSize-1-i;j++){
			if(arr[j]>arr[j+1]){
				temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
		}
	}
    return arr;
}