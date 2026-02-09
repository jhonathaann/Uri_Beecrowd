#include <stdio.h>

int main() {
    int num1, num2, num3, num4;
    
    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);
    scanf("%d", &num4);
    
    if(num1 == 1){
        printf("1\n");
    }else if(num2 == 1){
         printf("2\n");
    }else if(num3 == 1){
         printf("3\n");
    }else{
         printf("4\n");
    }
    
    return 0;
}