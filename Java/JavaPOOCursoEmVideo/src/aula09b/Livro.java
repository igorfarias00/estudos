package aula09b;

import java.util.Random;

public class Livro implements Publicacao {
	private String titulo;
	private String autor;
	private int totPaginas;
	private int pagAtual;
	private boolean aberto;
	private Pessoa leitor;
	
	
	public Livro(String titulo, String autor, int totPaginas, Pessoa leitor) {
		this.setTitulo(titulo);
		this.setAutor(autor);
		this.setTotPaginas(totPaginas);
		this.setLeitor(leitor);
		this.setAberto(false);
		this.setPagAtual(0);
	}
	
	
	public void detalhes() {
		System.out.println("Titulo: " + this.getTitulo());
		System.out.println("Autor: " + this.getAutor());
		System.out.println("Total de páginas: " + this.getTotPaginas());
		System.out.println("Sendo lido por: " + this.getLeitor().getNome());
		System.out.println("Que tem "+ this.getLeitor().getNome() + " anos");
		System.out.println("E está na página "+ this.getPagAtual());
	}

	
	@Override
	public void abrir() {
		this.setAberto(true);
	}
	
	
	@Override
	public void fechar(){
		this.setAberto(false);
	}
	
	@Override
	public void folhear() { // abrir em uma página aleatoria
		Random generator = new Random();
		if(this.getAberto()) {
			this.setPagAtual(generator.nextInt(this.getTotPaginas()));
		}
	}
	
	@Override
	public void avancarPag() {
		this.setPagAtual(this.getPagAtual() + 1);
	}
	
	@Override
	public void voltarPag() {
		this.setPagAtual(this.getPagAtual() - 1);
	}
	
	
	
	
	// getters and setters 
	private Pessoa getLeitor() {
		return leitor;
	}


	private void setLeitor(Pessoa leitor) {
		this.leitor = leitor;
	}


	public boolean getAberto() {
		return aberto;
	}


	public void setAberto(boolean aberto) {
		this.aberto = aberto;
	}


	public int getPagAtual() {
		return pagAtual;
	}


	public void setPagAtual(int pagAtual) {
		this.pagAtual = pagAtual;
	}


	public int getTotPaginas() {
		return totPaginas;
	}


	public void setTotPaginas(int totPaginas) {
		this.totPaginas = totPaginas;
	}


	public String getAutor() {
		return autor;
	}


	public void setAutor(String autor) {
		this.autor = autor;
	}


	public String getTitulo() {
		return titulo;
	}


	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	
	
}
