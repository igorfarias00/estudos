package ed.listaduplamenteligada;

public class Celula {
	private Object elemento;
	
	private Celula proximo;
	private Celula anterior;
	
	public Celula(Object elemento) {
		this(elemento, null);
	}
	
	public Celula(Object elemento, Celula proximo) {
		this.elemento = elemento;
		this.proximo = proximo;
	}
	
	public Celula getProximo() {
		return this.proximo;
	}
	
	public void setProximo(Celula proximo) {
		this.proximo = proximo;
	}
	
	public Celula getAnterior() {
		return this.anterior;
	}
	
	public void setAnterior(Celula anterior) {
		this.anterior = anterior;
	}
	
	public Object getElemento() {
		return elemento;
	}
	
}
