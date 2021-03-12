#include <stdio.h>

void print (int res)
{
    switch (res)
        {
            case 1:
                printf("OK");
                break;
            case 2:
                printf("Not OK");
                break;
            
            default:
                printf("Default");
                break;
        }
        printf ("\n");
}

int main()
{
    int res;
    for (int i = 0; i < 3; i++)
    {
        scanf ("%d", &res);  
        print (res);  
    }
    return 0;
}