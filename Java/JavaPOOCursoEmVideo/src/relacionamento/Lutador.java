package relacionamento;

public class Lutador {
	private String nome;
	private String nacionalidade;
	private int idade;
	private double altura;
	private double peso;
	private String categoria;
	private int vitorias;
	private int derrotas;
	private int empates;
	
	
	public Lutador(String no, String na, int id, double al, double pe, int vi, int de, int em) {
		this.setNome(no);
		this.setNacionalidade(na);
		this.setIdade(id);
		this.setAltura(al);
		this.setPeso(pe);
		this.setVitorias(vi);
		this.setDerrotas(de);
		this.setEmpates(em);
	}
	
	public void apresentar() {
		System.out.print("---------------------");
		System.out.print("  Lutador: " + this.getNome());
		System.out.println("  ------------------------------");
		System.out.println("Origem " + this.getNacionalidade());
		System.out.println(this.getIdade() + " anos");
		System.out.println(this.getAltura() + "m de altura");
		System.out.println("Pesando " + this.getPeso());
		System.out.println("Ganhou: " + this.getVitorias());
		System.out.println("Perdeu: " + this.getDerrotas());
		System.out.println("Empatou: " + this.getEmpates());
		System.out.println("---------------------------------------------------------------------------");
		
	}
	
	public void status() {
		System.out.println(this.getNome());
		System.out.println("É um peso " + this.getCategoria());
		System.out.println(this.getVitorias() + " vitórias");
		System.out.println(this.getDerrotas() +" derrotas");
		System.out.println(this.getEmpates() + " empates");
	}
	
	public void ganhouLuta() {
		this.setVitorias(getVitorias() + 1);
	}
	
	public void perdeuLuta() {
		this.setDerrotas(getDerrotas() + 1);
	}
	
	public void empatouLuta() {
		this.setEmpates(getEmpates() + 1);
	}
	
// 			GETTERS and SETTERS ***-----------------------------------------------
	
	public String getNome() {
		return this.nome;
	}
	
	private void setNome(String nome) {
		this.nome = nome;
	}
	
	private String getNacionalidade() {
		return this.nacionalidade;
	}
	
	private void setNacionalidade(String pais) {
		this.nacionalidade = pais;
	}
	
	private int getIdade() {
		return this.idade;
	}
	
	private void setIdade(int idade) {
		this.idade = idade;
	}
	
	private double getAltura() {
		return this.altura;
	}
	
	private void setAltura(double altura) {
		this.altura = altura;
	}
	
	private double getPeso() {
		return this.peso;
	}
	
	private void setPeso(double peso) {
		this.peso = peso;
		this.setCategoria();
	}
	
	public String getCategoria() {
		return this.categoria;
	}
	
	private void setCategoria() {
		if(this.peso <52.2) {
			this.categoria = "Inválido";
		} else if(this.peso <= 70.3) {
			this.categoria = "Leve";
		} else if(this.peso <= 83.9) {
			this.categoria = "Médio";
		} else if(this.peso <= 120.2) {
			this.categoria = "Pesado";
		} else {
			this.categoria = "Inválido";
		}
		
	}

	private int getVitorias() {
		return this.vitorias;
	}

	private void setVitorias(int vitorias) {
		this.vitorias = vitorias;
	}
	
	private int getDerrotas() {
		return this.derrotas;
	}

	private void setDerrotas(int derrotas) {
		this.derrotas = derrotas;
	}
	
	private int getEmpates() {
		return this.empates;
	} 
	
	private void setEmpates(int empates) {
		this.empates = empates;
	}
	
}
