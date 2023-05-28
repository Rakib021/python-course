#include <stdio.h>

int main()
{
    int i, j, k, temp, element;
    int data[10];
    
    printf("Enter the number of elements");
    scanf("%d", &element);
    
    printf("Enter the elements:\n");
    for(k = 0; k < element; k++) {
        scanf("%d", &data[k]);
    }
    
    for(i = 1; i <= element - 1; i++) {
        for(j = 0; j <= element - i - 1; j++) {
            if(data[j] > data[j+1]) {
                temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
            }
        }
    }
    
    printf("The sorted elements are:\n");
    for(k = 0; k < element; k++) {
        printf("%d ", data[k]);
    }

    return 0;
}
