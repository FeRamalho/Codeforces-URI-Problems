#include <stdio.h>

int main(){
	int n,c,m,i,j;
	int numCarimbadas=0;

	scanf("%d %d %d", &n,&c,&m);
	int carimbadas[c],compradas[m];

	for(i=0;i<c;i++){
		scanf("%d",&carimbadas[i]);
	}
	for(i=0;i<m;i++){
		scanf("%d",&compradas[i]);
	}
	i=0;
	for(i=0;i<c;i++){
		for(j=0;j<m;j++){
			if(carimbadas[i]==compradas[j]){
				numCarimbadas++;
				break;
			}
		}
	}

	printf("%d\n", c-numCarimbadas);

	return 0;
}