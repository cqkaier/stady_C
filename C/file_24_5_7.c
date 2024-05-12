#include <stdio.h>
int main()
{
int x=102,y=012;
printf("%2d,%2d\n",x,y);
int m=0xabc,n=0xabc;
m-=n; 
printf("%x\n",m);
int a=1234;
printf("%2d\n",a);
double d;float f;long l;int i;
l=f=i=d=80/7;
printf("%d%ld%f%f\n",i,l,f,d);
return 0;
}
