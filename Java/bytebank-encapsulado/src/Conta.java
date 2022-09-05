
public class Conta {
	private double saldo;
	private int agencia;
	private int numero;
	private Cliente titular;
	private static int total = 0;
	
	public Conta(int agencia, int numero) {
		Conta.total++;
		System.out.println("O total de contas é " + Conta.total);
		this.agencia = agencia;
		this.numero = numero;
		this.saldo = 100;
		System.out.println("Estou criando uma conta " + this.numero);
	}
	
	public void deposito(double valor) {
		this.saldo += valor;
	}
	
	public boolean saque(double valor) {
		if(this.saldo >= valor) {
			this.saldo -= valor;
			return true;
		} else {
			System.out.println("Você não possui saldo o suficiente para essa transação!!!");
			return false;
		}
	}
	
	public boolean transfere(double valor, Conta destino) {
		if(this.saldo >= valor) {
			this.saldo -= valor;
			destino.deposito(valor);
			return true;
		} else {
			return false;
		}
	}
	
	
	public double getSaldo() {
		return this.saldo;
	}
	
	public int getNumero() {
		return this.numero;
	}
	
	public void setNumero(int numero) {
		if(numero > 0) {
			System.out.println("Não pode valor menor ou igual a zero");
			return;
		} else {
			System.out.println("Numero alterado");
			this.numero = numero;
		}
	}
	
	public int getAgencia() {
		return this.agencia;
	}
	
	public void setAgencia(int agencia) {
		if(agencia <= 0) {
			System.out.println("Não pode valor menor ou igual a zero");
			return;
		} else {
			this.agencia = agencia;
			System.out.println("Agencia alterada");
		}
	}
	
	public void setTitular(Cliente titular) {
		if(titular != null) {
			this.titular = titular;
		} else {
			System.out.println("Valor nulo para cliente");
			return;
		}
	}
	
	public Cliente getTitular() {
		return this.titular;
	}
	
	public static int getTotal() {
		return Conta.total;
	}
}
