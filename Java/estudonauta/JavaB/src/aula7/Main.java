package aula7;

public class Main {
	public static void main(String[] args) {
		// operadores aritimeticos 
		// + soma 
		// - subtração
		// * multiplicação
		// / divisao
		//	% resto da divisao
		
		int n1 = 3;
		int n2 = 5;
		float frac = (n2 + n1) / 2;
		
		float frac2 = n2 + n1 / 2;
		
		System.out.println(frac);
		System.out.println(frac2);
		
		// ----------------------------------------------------------
		// Operadores Unarios
		// -- == decremento
		// ++ == incremento
		
		// pós e pré 
		// pos = realiza o incremento/decremento após da iteração
		// pré = realiza o incremento/decremento antes da iteração
		
		int valor1 = 5;
		int valor2 = 2;
		
		
		
		int soma = valor1 + valor2++;
		System.out.println(valor1 + " + " + valor2 +" = "+ soma);
		
		int soma2 = --valor1 + valor2;
		System.out.println(valor1 + " + " + valor2 +" = "+soma2);
		
		int soma3 = valor1 + ++valor2;
		System.out.println(valor1 + " + " + valor2 +" = "+soma3);
		
		
		// -----------------------------------------------------------------------
		// operadores de atribuição
		int a = 5;
		int b = 2;
		
		a += b;
		System.out.println(a);
		
		a -= b;
		System.out.println(a);
		
		a *= b;
		System.out.println(a);
		
		a /= b;
		System.out.println(a);
		
		a = 5;
		a %= b;
		System.out.println(a);
		
		
	}
}
