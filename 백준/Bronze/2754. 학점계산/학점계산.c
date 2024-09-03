#include <stdio.h>

int main() {
    char grade[3];
    
    scanf("%s", grade);

    if (grade[0] == 'A') {
        if (grade[1] == '+') printf("4.3\n");
        else if (grade[1] == '0') printf("4.0\n");
        else if (grade[1] == '-') printf("3.7\n");
    } else if (grade[0] == 'B') {
        if (grade[1] == '+') printf("3.3\n");
        else if (grade[1] == '0') printf("3.0\n");
        else if (grade[1] == '-') printf("2.7\n");
    } else if (grade[0] == 'C') {
        if (grade[1] == '+') printf("2.3\n");
        else if (grade[1] == '0') printf("2.0\n");
        else if (grade[1] == '-') printf("1.7\n");
    } else if (grade[0] == 'D') {
        if (grade[1] == '+') printf("1.3\n");
        else if (grade[1] == '0') printf("1.0\n");
        else if (grade[1] == '-') printf("0.7\n");
    } else if (grade[0] == 'F') {
        printf("0.0\n");
    }

    return 0;
}