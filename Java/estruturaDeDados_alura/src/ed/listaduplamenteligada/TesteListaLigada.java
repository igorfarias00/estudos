package ed.listaduplamenteligada;

public class TesteListaLigada {
	public static void main(String[] args) {
		ListaLigada lista = new ListaLigada();
		
		System.out.println(lista);
		lista.adicionaNoComeco("Mauricio");
		System.out.println(lista);
		lista.adicionaNoComeco("Paulo");
		System.out.println(lista);
		lista.adicionaNoComeco("Guilherme");
		System.out.println(lista);
		
		lista.adiciona("Marcelo");
		System.out.println(lista);
		
		lista.adiciona(2, "Gabriel");
		System.out.println(lista);
		
	/*	Object x = lista.pega(2);
		System.out.println(x);
		
		System.out.println("tamanho atual da lista Duplamente Ligada: " + lista.tamanho());
		*/
		lista.removeDoFim();
		System.out.println(lista);
		
		System.out.println("tamanho atual da lista Duplamente Ligada: " + lista.tamanho());
		
		lista.removeDoComeco();
		System.out.println(lista);
		System.out.println(lista.getTotalDeElementos());
		
		lista.remove(2);
		System.out.println(lista);
		
		System.out.println("tamanho atual da lista Duplamente Ligada: " + lista.tamanho());
		
		System.out.println(lista.contem("Mauricio"));
		System.out.println(lista.contem("Danilo"));
		System.out.println(lista.contem("Paulo"));
		System.out.println(lista.contem("Gabriel"));
	} 
}
