package relacionamento;

import java.util.Random;

public class Luta {
	private Lutador desafiado;
	private Lutador desafiante;
	private int rounds;
	private boolean aprovada;
	
	public Luta() {
		
	}
	
	
	public void marcarLuta(Lutador l1, Lutador l2) {
		if(l1.getCategoria() == l2.getCategoria() && l1 != l2) {
			this.setAprovada(true);
			this.setDesafiado(l1); 
			this.setDesafiante(l2);
			
		} else {
			this.setAprovada(false);
			this.setDesafiado(null);
			this.setDesafiante(null);
		}
	}
	
	public void lutar() {
		if(this.getAprovada()) {
			System.out.println("********  DESAFIADO #######");
			this.desafiado.apresentar();
			System.out.println("********  DESAFIANTE ######");
			this.desafiante.apresentar();
			Random generator = new Random();
			int vencedor = generator.nextInt(3);
			
			switch(vencedor) {
				case 0: // empate
						System.out.println("Empatou!");
						this.desafiante.empatouLuta();
						this.desafiado.empatouLuta();
					break;
					
				case 1: //desafiada ganha
						System.out.println(this.desafiado.getNome());
						this.desafiado.ganhouLuta();
						this.desafiante.perdeuLuta();
					break;
					
				case 2: //desafiante ganha
						System.out.println(this.desafiante.getNome());
						this.desafiado.perdeuLuta();
						this.desafiante.ganhouLuta();
					break;
					
			}
			
		} else {
			System.out.println("Luta não pode acontecer, pois os lutadores sem de categorias distintas");
		}
	}
	
	
	public void setDesafiado(Lutador desafiado) {
		this.desafiado = desafiado;
	}
	
	public Lutador getDesafiado() {
		return this.desafiado;
	}
	
	public void setDesafiante(Lutador desafiante) {
		this.desafiante = desafiante;
	}
	
	public Lutador getDesafiante() {
		return this.desafiante;
	}
	
	private void setRounds(int rounds) {
		this.rounds = rounds;
	}
	
	private int getRounds() {
		return this.rounds;
	}
	
	private void setAprovada(boolean decisao) {
		this.aprovada = decisao;
	}
	
	private boolean getAprovada() {
		return this.aprovada;
	}
}
