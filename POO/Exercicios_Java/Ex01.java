//1-) Crie um programa que receba três nomes quaisquer por meio 
// da linha de execução do programa e os imprima na tela da seguinte 
// maneira: o primeiro e o último nome serão impressos na primeira linha 
// um após o outro, o outro nome (segundo) será impresso na segunda linha.

public class Ex01{
	public static void main (String args[]){
    
  //Definindo argumentos a serem recebidos e mostrados na linha de comando
	System.out.println(args[0] + args[2]);
	System.out.println(args[1]);

	}
}
