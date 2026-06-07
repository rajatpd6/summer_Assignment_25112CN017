#include <stdio.h>
int main(){
  int n1,n2,max,lcm;
  printf("ENTER THE BOTH POSITIVE INTEGER : ");
  scanf("%d %d",&n1 ,&n2);
  max = (n1>n2)?n1:n2;
  lcm = max;
  while((lcm %n1 !=0)||(lcm %n2 !=0)){
    lcm = max;
  }
  printf("THE LCM OF %d AND %d IS %d : ",n1,n2,lcm);
  return 0;
}