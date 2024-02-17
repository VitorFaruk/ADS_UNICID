// Faça um programa que receba a quantidade e o valor de dois produtos, 
// no seguinte formato: quantidade1 valor1 quantidade2 valor2. O programa
// devecalcular esses valores seguindo a fórmula total = (quantidade1 x valor1) +(quantidade2 x valor2). 
// O valor total deve ser apresentado no final da execução.

//importando classe Scanner, para efetuar entrada de dados
import java.util.Scanner;

public class Ex02{
	public static void main(String args[]){
		//Criando objeto Scanner 	
		Scanner sc = new Scanner(System.in);
		
		//Recebendo valores do primeiro produto
		System.out.println("Digite a quantidade do primeiro produto: ");
		int quantidade1 = sc.nextInt();
		System.out.println("Digite o valor do primeiro produto: ");
		int valor1 = sc.nextInt();
		
		//Recebendo valores do segundo produto
		System.out.println("Digite a quantidade do segundo produto: ");
		int quantidade2 = sc.nextInt();
		System.out.println("Digite o valor do segundo produto: ");
		int valor2 = sc.nextInt();
		
		//Processando total e imprimindo
		int total = (quantidade1 * valor1) + (quantidade2 * valor2);
		System.out.println("O valor total eh: " + total);
	}
}
