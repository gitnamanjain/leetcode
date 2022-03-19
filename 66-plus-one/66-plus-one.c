int* plusOne(int* digits, int digitsSize, int* returnSize){
    for (int i = digitsSize-1; i >= 0; i--){
        if(digits[i]!=9){
            digits[i]++;
            break;
        }
        else{
            digits[i]=0;
        }
        
    }
    if (digits[0]==0)
        {
            int* newDigits=calloc((digitsSize+1),sizeof(int));
            newDigits[0]=1;
            *returnSize=digitsSize+1;
            return newDigits;
        }
    *returnSize=digitsSize;
    return digits;
}