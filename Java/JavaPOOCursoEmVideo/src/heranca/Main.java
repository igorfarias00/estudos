package heranca;

public class Main {
	public static void main(String[] args) {
		Funcionario f1 = new Funcionario("Maria", 32, "Feminino", "secretaria");
		Professor p1 = new Professor("Tristana", 41, "Feminino", "historia", 7000.50);
		Aluno a1 = new Aluno("João", 16, "Masculino");
		
		System.out.println(f1.getNome());
		System.out.println(f1.getSetor());
		System.out.println("===================");
		
		System.out.println(p1.getNome());
		System.out.println(p1.getEspecialidade());
		System.out.println(p1.getSalario());
		p1.receberAum(555.05);
		System.out.println("Salario apos o aumento: " + p1.getSalario());
		System.out.println("====================");
		
		System.out.println(a1.getNome());
		System.out.println(a1.getCurso());
		System.out.println(a1.getIdade());
		
	}
}
