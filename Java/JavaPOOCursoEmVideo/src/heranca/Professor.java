package heranca;

public class Professor  extends Pessoa{
	private String especialidade;
	private double salario;
	
	public Professor(String nome, int idade, String sexo, String especialidade, double salario) {
		super(nome, idade, sexo);
		this.setEspecialidade(especialidade);
		this.setSalario(salario);
	}
	
	public void receberAum(double aumento) {
		this.setSalario(this.getSalario() + aumento);
	}
	
	public void setSalario(double salario) {
		this.salario = salario;
	}
	
	public double getSalario() {
		return this.salario;
	}
	
	public void setEspecialidade(String especialidade) {
		this.especialidade = especialidade;
	}
	
	public String getEspecialidade() {
		return this.especialidade;
	}
}
