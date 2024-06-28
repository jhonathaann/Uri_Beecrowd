#include <stdio.h>

int main(){
    int c, p, f;
    
    scanf("%d", &c);
    scanf("%d", &p);
    scanf("%d", &f);
    
    if(c * f <= p ){
        printf("S\n");
    }else{
        printf("N\n");
    }
    
    return 0;
}