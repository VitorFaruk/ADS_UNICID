#include<stdio.h>

// Se não atribui valor à variável, ela armazena lixo. Depende do valor anterior que você tinha na memória.

struct {
	char name[30];
	char street[40];
	char city[20];
	char state[3];
	// long duplica a quantidade suportada pelo tipo int - de 32 para 64 bits (2 elevado a 64)
	// unsigned - não sinalizado. Sinalizado é positivo ou negativo. Não sinalizado é somente positivos. Ou seja, somente valores positivos (>=0)
	unsigned long int zip;
} addr_info;

int main(int agrc, char * argv){
	addr_info.zip=12345;
	
	// Get é receber via teclado. 
	gets(addr_info.name);
	
	printf("%ld", addr_info.zip);
	
	
	
	return 0;
}
