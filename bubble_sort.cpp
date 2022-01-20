#include<iostream>
//Bubble sort
using namespace std;
int main()
{
	int a[]={12,22,21,33,66,53,87,99,98};
	for(int i=0;i<9;i++)
	{
		for(int j=0;j<9-i;j++)
		{
			if(a[j]>a[j+1])
			{
				int temp=a[j+1];
				a[j+1]=a[j];
				a[j]=temp;
			}
		}
	}
	for(int i=0;i<9;i++)
	{
		cout<<a[i]<<endl;
	}
	return 0;
}
