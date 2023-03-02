package aula14;

import java.util.Arrays;

public class Vetor5 {
	public static void main(String[] args) {
		int num[] = new int[20];
		
		Arrays.fill(num, 8);
		
		for (int val: num) {
			System.out.print(val + " | ");
		}
		System.out.println();
		
		for (int i = 1; i < 5; i++) {
			if (i==2) continue;
			System.out.print("i = " + i);
		}
		System.out.println();
		
		int x, y;
		double z;
		x = 5;
		y = 2;
		z = x / y;
		System.out.println(z);
		
		//3
		int total = 0;
		int c[] = new int[13];
		for (int i = 0; i<c.length; i++) {
			c[i] = i + i;
		}

		for (int i = 0; i<c.length; i++) {
		total += c[i];
		}

		System.out.println(total);
		
		int i= 10;
		while(i > 0) {
			if(i == 5) {
				i -= 2;
				continue;
			}
			
		
			System.out.println(i);
			i--;
			
		}
		
		int v0 = 3;
		int v1 = v0++;
		int v2 = ++v1;
		v1 += v0;
		v2 += --v1;
		System.out.println(v0 + " | " + v1 + " | " + v2);
		
		System.out.println(Math.pow(8, 2));
		
		
		
	}
}
