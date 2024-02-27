#include<stdio.h>

// Atividade: Crie um programa para armazenar informações de 10 livros diferentes.
// Cada livro possui as seguintes informações:
// - Titulo
// - Autor
// - Categoria
// - Identificador
// O Programa deve pedir ao usuário as informações dos 10 livros e
// ao final imprimir todas as informações.

// criando Struct do tipo livro
struct livros{
	char titulo[80];
	char autor[80];
	char categoria[80];
	char identificador[20];
} cad_livros;

int main(int argc, char * agrv){
	// declarando a variável cad_livros da struct tipo livros
	struct livros cad_livros[10];
	int i=0;
	
	// criando for para recebimento dos 10 cadastros de livro
	for (i = 0; i < 10; i++){
		printf("\nDigite o titulo do %do. livro: ", i+1);
		gets(cad_livros[i].titulo);
		printf("Digite o autor do %do. livro: ", i+1);
		gets(cad_livros[i].autor);
		printf("Digite a categoria do %do. livro: ", i+1);
		gets(cad_livros[i].categoria);
		printf("Digite o identificador do %do. livro: ", i+1);
		gets(cad_livros[i].identificador);
	}
	
	printf("---------------------------//---------------------------\n");
	
	//criando for para impressão dos 10 cadastros de livro
	for (i = 0; i < 10; i++){
		printf("\n%do. livro:", i+1);
		printf("\nTitulo: %s", cad_livros[i].titulo);
		printf("\nAutor: %s", cad_livros[i].autor);
		printf("\nCategoria: %s", cad_livros[i].categoria);
		printf("\nIdentificador: %s", cad_livros[i].identificador);
		printf("\n");

	}	
}
