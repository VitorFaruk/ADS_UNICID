// Crie um programa que receba a largura e o comprimento de 
// um lote de terra emostre a área total existente

// Importando classe Scanner, para efetuar entrada de dados
import java.util.Scanner;

public class Ex03{
	public static void main(String args[]){
		
		// Declarando objeto Scanner para recepção de dados
		Scanner sc = new Scanner(System.in);

		// Solicitando a entrada da largura e do comprimento
		System.out.println("Digite a largura do lote de terra (m): ");
		double largura = sc.nextDouble();
		System.out.println("Digite o comprimento do lote de terra (m): ");
		double comprimento = sc.nextDouble();

		// Processando área total e imprimindo
		double area = (largura * comprimento);
		System.out.println("A area total existente eh de " + area + " m2");
	}
}
