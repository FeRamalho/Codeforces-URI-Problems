#include <stdio.h>
#define PI 3.14159

int main(){
	double raio;

	scanf("%lf",&raio);
	printf("A=%.4lf\n", (raio*raio)*PI);

	return 0;
}