import java.util.Scanner;

public class HelloWorld{
	public static void main (String args[]){
		//imprimir (comentário)
		Scanner sc1 = new Scanner(System.in);
		System.out.println("Digite o valor de A: ");
		int num1 = sc1.nextInt();
		System.out.println("Digite o valor de B: ");
		int num2 = sc1.nextInt();
		int soma = num1 + num2;

		//concatenando string com a variavel
		System.out.println("O valor da soma eh: " + soma);

		System.out.println("Nome: " + args[0]);
		System.out.println("SobreNome: " + args[1]);	
	}
}

//javac HelloWorld.java
//java HelloWorld Vitor Oliveira
