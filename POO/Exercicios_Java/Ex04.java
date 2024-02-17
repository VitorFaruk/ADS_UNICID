// Crie um programa que receba quatro valores quaisquer 
// e mostre a média esoma entre eles.

// Importando classe Scanner, para efetuar entrada de dados
import java.util.Scanner;

public class Ex04{
	public static void main(String args[]){
	// Declarando objeto Scanner para recepção de dados
	Scanner sc = new Scanner(System.in);
	
	// Recebendo os quatro valores
	System.out.println("Digite o primeiro valor: ");
	double v1 = sc.nextDouble();
	System.out.println("Digite o segundo valor: ");
	double v2 = sc.nextDouble();
	System.out.println("Digite o terceiro valor: ");
	double v3 = sc.nextDouble();
	System.out.println("Digite o quarto valor: ");
	double v4 = sc.nextDouble();

	// Processando média e soma
	double media = ((v1 + v2 + v3 + v4) / 4);
	double soma = (v1 + v2 + v3 + v4);

	// Imprimindo média e soma
	System.out.println("A media dos valores mencionados eh: " + media);
	System.out.println("A soma dos valores mencionados eh: " + soma);
	}
}
