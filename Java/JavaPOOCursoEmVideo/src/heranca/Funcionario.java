package heranca;

public class Funcionario extends Pessoa{
	private String setor;
	private boolean trabalhando;
	
	public Funcionario(String nome, int idade, String sexo, String setor) {
		super(nome, idade, sexo);
		this.setTrabalhando(false);
		this.setSetor(setor);
	}
	
	
	public void mudarTrabalho() {
		if(this.getTrabalhando())
			this.setTrabalhando(false);
		else
			this.setTrabalhando(true);
	}
	
	private void setTrabalhando(boolean trabalhando) {
		this.trabalhando = trabalhando;
	}
	
	public boolean getTrabalhando() {
		return this.trabalhando;
	}
	
	public void setSetor(String setor) {
		this.setor = setor;
	}
	
	public String getSetor() {
		return this.setor;
	}
}
