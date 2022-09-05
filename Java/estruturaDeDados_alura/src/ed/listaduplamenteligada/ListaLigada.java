package ed.listaduplamenteligada;

public class ListaLigada {
	private Celula primeira = null;
	private Celula ultima = null;
	private int totalDeElementos = 0;
	
	public void adicionaNoComeco(Object elemento) {
		if(this.totalDeElementos == 0) {
			Celula nova = new Celula(elemento);
			this.primeira = nova;
			this.ultima = nova;
		} else {
			Celula nova = new Celula(elemento, this.primeira);
			this.primeira.setAnterior(nova);
			this.primeira = nova;
		}
		
		this.totalDeElementos++;
	}
	
	public void adiciona(Object elemento) {
		if(this.totalDeElementos == 0) {
			adicionaNoComeco(elemento);
		} else {
			Celula nova = new Celula(elemento);
			this.ultima.setProximo(nova);
			nova.setAnterior(this.ultima);
			this.ultima = nova;
			
			this.totalDeElementos++;
		}
	}
	
	public void adiciona(int posicao, Object elemento) {
		if(!posicaoOcupada(posicao)) {
			throw new IllegalArgumentException("Posicao inexistente");
		} else {
			if(posicao == 0) {
				adicionaNoComeco(elemento);
			} else if(posicao == this.totalDeElementos) {
				this.adiciona(elemento);
			} else {
				Celula anterior = pegaCelula(posicao - 1);
				Celula proximo = anterior.getProximo();
				Celula nova = new Celula(elemento, anterior.getProximo());
				
				// altera a referencia do anterior no elemento inserido e altera a referencia do proximo no elemento anterior
				nova.setAnterior(anterior);
				anterior.setProximo(nova);
				// altera a referencia do proximo no elemento inserido
				nova.setProximo(proximo);
				proximo.setAnterior(nova);
				
				this.totalDeElementos++;
			}
		}
	}
	
	private boolean posicaoOcupada(int posicao) {
		return posicao >= 0 && posicao < this.totalDeElementos;
	}
	
	private Celula pegaCelula(int posicao) {
		if(!posicaoOcupada(posicao)) {
			throw new IllegalArgumentException("Posicao inexistente");
		}
		
		Celula atual = primeira;
		
		for(int i = 0; i < posicao; i++) {
			atual = atual.getProximo();
		}
		
		return atual;
	}
	

	
	
	public Object pega(int posicao) {
		return this.pegaCelula(posicao).getElemento();
	}
	
	public void removeDoComeco() {
		if(this.totalDeElementos == 0) {
			return;
		}
		
		this.primeira = this.primeira.getProximo();
		this.totalDeElementos--;
		
		if(this.totalDeElementos == 0){
			this.ultima = null;
		}
	}
	
	public void removeDoFim() {
		if(this.totalDeElementos == 1) {
			this.removeDoComeco();
		} else {
			Celula penultima = this.ultima.getAnterior();
			penultima.setProximo(null);
			this.ultima = penultima;
			
			this.totalDeElementos--;
		}
	}
	
	public void remove(int posicao) {
		//posicao--;
		if(posicao == 0) {
			this.removeDoComeco();
		} else if(posicao == this.totalDeElementos - 1) {
			this.removeDoFim();
		} else {
			Celula anterior = this.pegaCelula(posicao - 1);
			Celula atual = anterior.getProximo();
			Celula proximo = atual.getProximo();
			
			anterior.setProximo(proximo);
			proximo.setAnterior(anterior);
			
			this.totalDeElementos--;
			
		}
	}
	
	public int tamanho() {
		return this.totalDeElementos;
	}
	
	public boolean contem(Object elemento) {
		Celula atual = this.primeira;
		
		while (atual != null) {
			if(atual.getElemento().equals(elemento)) {
				return true;
			}
			
			atual = atual.getProximo();
		}
		
		return false;
	}
	
	@Override
	public String toString() {
		//int i = 0;
		if(this.totalDeElementos == 0) {
			return"[ ]";
		}
		
		Celula atual = primeira;
		
		StringBuilder builder = new StringBuilder("[");
		

		for(int i = 0;i < this.totalDeElementos - 1 ;i++) {
			builder.append(atual.getElemento());
			builder.append(", ");
			if(atual.getProximo() != null) {
				atual = atual.getProximo();
			}
		}
		 
		builder.append(atual.getElemento());
		builder.append("]");
		
		return builder.toString();
	}
	
	public Celula getPrimeira() {
		return this.primeira;
	}
	
	public Celula getUltima() {
		return this.ultima;
	}
	
	public int getTotalDeElementos() {
		return this.totalDeElementos;
	}
}
