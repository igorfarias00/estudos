package beecrowd;

import java.io.IOException;
import java.util.Scanner;

/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Average3 {
 
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        /**
         * Escreva a sua solução aqui
         * Code your solution here
         * Escriba su solución aquí
         */
       
        double nota1, nota2, nota3, nota4, media;
        
        
        nota1 = in.nextDouble();
        nota2 = in.nextDouble();
        nota3 = in.nextDouble();
        nota4 = in.nextDouble();
        
        media = (nota1 + nota2 +nota3 + nota4) / 4;
        
        
        
        if(media < 7 && media >=5 ){
        	System.out.println("Media: " + media);
            System.out.println("Aluno em exame.");
            System.out.print("Nota do exame: ");
            nota1 = in.nextDouble();
            media = (nota1 + media) / 2;
            if(media >= 5) {
            	System.out.println("Aluno aprovado.");
            	System.out.println("Media final: " + media);
            } else {
            	System.out.println("Aluno reprovado");
            	System.out.println("Media final: " + media);
            }
        } else if (media >= 7) {
        	System.out.println("Media: " + media);
        	System.out.println("Aluno aprovado.");
        } else {
        	System.out.println("Media: " + media);
        	System.out.println("Aluno reprovado.");
        }
        
    }
 
}