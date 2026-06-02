//Q4 Write a program to count digits in a number.
#include<stdio.h>
int main(){
  int n, count = 0;
  printf("Enter the number:");
  scanf("%d",&n);
  if(n==0){
    count = 1;
  }else{
    while(n!=0){
      n=n/10;
      count++;
    }
  }
  printf("Total digits: %d",count);
  return 0;
}