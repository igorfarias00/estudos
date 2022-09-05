package aula09b;

public class Main {
	public static void main(String[] args) {
		Pessoa joao = new Pessoa("Joao", 23, "M");
		Livro livro[] = new Livro[3];
		
		livro[0] = new Livro("20 mil leguas submarinas", "Julio verne", 250, joao);
		
		livro[0].abrir();
		
		livro[0].folhear();
		livro[0].detalhes();
		
		livro[0].folhear();
		livro[0].detalhes();
		
		livro[0].folhear();
		livro[0].detalhes();
		
		
		
	}
}
