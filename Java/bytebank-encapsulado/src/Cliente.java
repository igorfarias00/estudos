
public class Cliente {
	public static void main(String[] args) {
		Conta c1 = new Conta(1234, 2222);
		
		c1.deposito(1500);
		c1.deposito(1000);
		c1.saque(2000);
		c1.setAgencia(3333);
		
		System.out.println(c1.getSaldo());
		System.out.println(c1.getAgencia());
	}
}
