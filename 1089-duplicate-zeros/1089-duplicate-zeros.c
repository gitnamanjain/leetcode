

void duplicateZeros(int* arr, int arrSize){
    int pnt;
    for (int i=0; i<arrSize; i++){
        if(arr[i]==0){
			pnt=arrSize-1;
            for(int j=pnt;j>i;j--)
			{
				arr[pnt]=arr[pnt-1];
				pnt--;
			}
		i++;
        }
	}
}