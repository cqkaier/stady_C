#include <stdio.h>
int main()
{
	int i = 0;
	int j = 0;
	int b = 0;
	for(i=1;i<5;i++)
	{
		j=1;
		for(b=1;b<i;b++)
		{
			printf(" ");
		}
		while(j<5)
		{
			/*while(i>j)
			{
				printf(" ");
			}*/
			printf("*");
			j++;
		}
		printf("\n");
		/*while(i>b)
		{
			printf(" ");
			b++;
		}*/

		//printf("\n");
		 

	}
	return 0;

}
