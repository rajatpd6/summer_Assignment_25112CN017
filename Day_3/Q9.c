#include<stdio.h>
int main(){
  int num, i , isprime = 1 ;
  printf("ENTER A POSITIVE INTEGER : ");
  scanf("%d",&num);
  if(num <= 1){
    isprime = 0;
  }else{
    for(i = 2; i * i <= num; i++){
      if(num % i == 0){
        isprime = 0;
        break;
      }
    }
  }

  if(isprime == 1){
    printf("%d is a prime number.\n", num);
  }else{
    printf("%d is not a prime number.\n", num);
  }

  return 0;
}