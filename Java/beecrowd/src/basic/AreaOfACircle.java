package basic;

import java.util.Scanner;
import java.math.*;
public class AreaOfACircle {
	public static void main(String[] args) {
		Scanner tcl = new Scanner(System.in);
		
		double r, area;
		
		r = tcl.nextDouble();
		
		area = (double) (Math.pow(r, 2.00)* 3.14159);
		
		System.out.printf("A=%.4f\n", area);
		
		
	}
}
