int evenDigitCounter(int arrayelement){
	int noOfDigits=0,evenorno=0;
	float a= arrayelement;
	float c;
	do{
		
		c=a/10;
		a=c;
		noOfDigits++;
	}
	while (c>1);
    if(c==1)
	{
		noOfDigits++;
	}
	if(noOfDigits%2==0)
	{
		evenorno=1;
	}
	return evenorno;
}

int findNumbers(int* nums, int numsSize){
    int evencounter=0,evenorno;
	for(int i=0;i<numsSize;i++){
		evenorno=evenDigitCounter(nums[i]);
		if(evenorno==1)
		{
			evencounter++;
		}
	}
	return evencounter;
}