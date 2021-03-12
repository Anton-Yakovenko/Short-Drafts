// calculator 
#include <stdio.h>

void input(float *num1, float *num2)
{   
    printf("num 1: ");
    scanf("%f", &*num1);


    printf("num 2: ");
    scanf("%f", &*num2);
}


int main()
{
    char choice;
    float num1, num2, res;

    printf("Welcome! \nPlease choose option: sum(S), difference(D), multiplication(M), division(V)\nS/D/M/V: ");
    scanf("%c", &choice);

    input(&num1, &num2);

    if (choice == 'S')
        res = num1 + num2;

    else if (choice == 'D')  
        res = num1 - num2;

    else if (choice == 'M')
        res = num1 * num2;
    
    else if (choice = 'V')
        res = num1 / num2;

    else
    {
        res = 0;
        printf("unknown choice - %c", choice);
    }

    printf("res = %.2f\n", res);

    return 0;
}




// void print (int res)
// {
//     switch (res)
//         {
//             case 1:
//                 printf("OK");
//                 break;
//             case 2:
//                 printf("Not OK");
//                 break;
            
//             default:
//                 printf("Default");
//                 break;
//         }
//         printf ("\n");
// }