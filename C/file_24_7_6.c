#include <stdio.h>
int main()
{
	int a,b,c,d,t;
	scanf("%d %d %d %d",&a,&b,&c,&d);
	if(a>b)
	{
	t=a;
	a=b;
	b=a;
	}
	if(a>c)
	{
		t=a;
		a=c;
		c=a;
	}
	if(a>d)
	{
		t=a;
		a=d;
		d=a;
	}
	if(b>c)
	{
		t=b;
		b=c;
		c=b;
	}
	if(b>d)
	{

		t=b;
		b=d;
		d=b;
	}
	if(c>d)
	{
		t=c;
		c=d;
		d=c;
	}
	printf("%d %d %d %d",a,b,c,d);



	return 0;

}
