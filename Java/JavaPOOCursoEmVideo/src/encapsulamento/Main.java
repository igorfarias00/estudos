package encapsulamento;

public class Main {
	public static void main(String[] args) {
		ControleRemoto samsung = new ControleRemoto();
		
		samsung.abrirMenu();
		samsung.ligar();
		
		for(int i = 0; i < 30; i++) {
			samsung.menosVolume();
		}
		
		samsung.play();
		samsung.abrirMenu();
	}
}
