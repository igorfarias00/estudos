package aula14;

import java.util.Arrays;

public class Vetor3 {
	public static void main(String[] args) {
		double num[] = {-1.5, 3.22, 5.57, 7.19, -2.1};
		
		for(double valor:num) {		//for each
			System.out.println(valor);
		}
		
		Arrays.sort(num);
		
		for(double valor: num) {
			System.out.print(valor + " | ");
		}
		
		
		
	}
}
