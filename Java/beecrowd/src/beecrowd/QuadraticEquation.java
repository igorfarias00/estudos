package beecrowd;

public class QuadraticEquation {
    public static Roots findRoots(double a, double b, double c) {
        double delta;	// deixe o delta em separado para um melhor visualização do calculo
        
        delta = Math.pow(b,2) - 4 * a * c;	// calculo do delta

        double xLess = (-b - Math.sqrt(delta)) / (2 * a);	// calculo da subtração
        double xPlus = (-b + Math.sqrt(delta)) / (2 * a);	// calculo da soma 
        
        return new Roots(xPlus, xLess);		// retorna o objeto com as raizes
    }
    
    public static void main(String[] args) {
        Roots roots = QuadraticEquation.findRoots(2, 10, 8);
        System.out.println("Roots: " + roots.x1 + ", " + roots.x2);
    }
}
