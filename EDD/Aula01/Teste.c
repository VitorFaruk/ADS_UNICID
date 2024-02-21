#include<stdio.h>
#include<conio.h>

struct func{
		char nome[50];
		float salario;	
	};

int main(int argc, char * argv){
	
	struct func a[5];
	int i = 0;
	
	for (i=0 ; i<5 ; i++){
		printf("\nDigite o nome do %o funcionario:", i+1);
		scanf("%s", &a[i].nome);
		printf("Digite o salario do %o funcionario: ", i+1);
		scanf("%f", &a[i].salario);
	}
	
	for (i=0 ; i<5 ; i++){
		printf("\n%o funcionario: %s", i+1, a[i].nome);
		printf("\nsalario: %f \n----", a[i].salario);
	}

	return 0;
}

// Enviar para Professor em Mensagens do Curso (BlackBoard)
