#include <stdio.h>
int max(int b,int c)
{
	if(b>c)
		return b;
	else
		return c;
}
void print(int x)
{
	for(int i = 0;i<x;i++)
	{
	for(int j = 1;j<5;j++)
	{
		printf("*");
	}
	printf("\n");
	}
}
int main()
{
	int a,b,c;
	scanf("%d,%d %d",&b,&c,&a);
	printf("%d\n",max(b,c));
	print(a);
	return 0;
}
