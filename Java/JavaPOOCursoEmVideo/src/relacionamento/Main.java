package relacionamento;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Lutador Lutadores[] = new Lutador[5];
		Scanner teclado = new Scanner(System.in);
		
		Lutadores[0] = new Lutador( "Pretty Boy", "França", 31, 1.75, 68.9, 11, 3, 1); 
		
		Lutadores[1] = new Lutador("Puttscript", "Brasil", 29, 1.68, 57.8, 14, 2, 3);
		
		Lutadores[2] = new Lutador("Snapshadow", "EUA", 35, 1.65, 80.9, 12, 2, 1);
		
		Lutadores[3] = new Lutador("Deadcode", "Australia", 28, 1.93, 91.6,13, 0, 2);
		
		Lutadores[4] = new Lutador("Chico Alicate", "Montenegro", 64, 1.89, 92.5, 1, 7, 9);
		
		Luta lutas[] = new Luta[4];
		
		
		
		lutas[0] = new Luta();
		int continua= teclado.nextInt();
		
		do {
			lutas[0].marcarLuta(Lutadores[3], Lutadores[4]);
			lutas[0].lutar();
			continua = teclado.nextInt();
		} while (continua != 1);
		
		//Lutadores[0].status();
		//Lutadores[4].status();
		
	}
}
