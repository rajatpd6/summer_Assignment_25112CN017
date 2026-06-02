//Q1 Write a program to calculate sum of first n natural numbers.
#include<stdio.h>
int main(){
  int n;
  printf("Enter the no.");
  scanf("%d",&n);
  int sum=0;
  for(int i=1;i<=n;i++){
    sum=sum+i;
  }
printf("Sum is %d\n",sum);
return 0;
}
