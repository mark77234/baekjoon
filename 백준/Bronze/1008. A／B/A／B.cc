#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	double A , B, C;
	scanf("%lf %lf", &A, &B);
	C = A / B;
	
	printf("%.9lf", C);
	return 0;
}