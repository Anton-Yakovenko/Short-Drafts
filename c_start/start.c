// calculator 
#include <stdio.h>

void input(float *num1, float *num2)
{   
    printf("num 1: ");
    scanf("%f", &*num1);


    printf("num 2: ");
    scanf("%f", &*num2);
}


void calculator (char choice)
{
    float num1, num2, res;
    input(&num1, &num2);

    if (choice == '+')
        res = num1 + num2;

    else if (choice == '-')  
        res = num1 - num2;

    else if (choice == '*')
        res = num1 * num2;
    
    else if (choice == '/')
        res = num1 / num2;

    else
    {
        res = 0;
        printf("unknown choice - %c\n", choice);
    }

    printf("res = %.2f\n", res);
}

int main()
{   
    char choice;
    printf("Welcome! \n");

    do
    {   
        printf("Please choose option: sum(+), difference(-), multiplication(*), division(/), quit(Q)\nYour choice: ");
        scanf(" %c", &choice);

        if (choice != 'Q')
            calculator(choice);    

    } while (choice != 'Q');

    printf("Bye!\n");

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