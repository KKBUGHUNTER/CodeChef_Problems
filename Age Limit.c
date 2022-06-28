#include <stdio.h>

int main() 
{
  int X,Y,A,T,i;
  scanf("%d",&T);
  for(i=0; i<T; i++){
    scanf("%d %d %d ",&X,&Y,&A);
    if(A>=X && A<Y)printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}
