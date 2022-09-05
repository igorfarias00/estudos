
public class ContaBanco {
	private boolean status;
	protected String tipo;
	private String dono; 
	private double saldo;
	public int numConta;
	
	public ContaBanco() {
		this.status = false;
		this.saldo = 0;
	} 
	
	public void estadoAtual() {
		System.out.println("Conta: " + this.getNumConta());
		System.out.println("Tipo: " + this.getTipo());
		System.out.println("Dono: " + this.getDono());
		System.out.println("Saldo: " + this.getSaldo());
		System.out.println("Status: " + this.getStatus());
		System.out.println("----------------------------------------------");
	}
	
	public boolean getStatus() {
		return this.status;
	}
	
	public void setStatus(boolean status) {
		this.status = status;
	}
	
	public String getTipo() {
		return this.tipo;
	}
	
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	
	public String getDono() {
		return this.dono;
	}
	
	public void setDono(String dono) {
		this.dono = dono;
	}
	
	public double getSaldo() {
		return this.saldo;
	}
	
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	
	public int getNumConta() {
		return this.numConta;
	}
	
	public void setNumConta(int numConta) {
		this.numConta = numConta;
	}
	
	public void abrirConta(String tipo) {
		if(tipo =="CC" || tipo == "cc" || tipo == "CP" || tipo == "cp") {
			this.setTipo(tipo);
			this.setStatus(true);
			if(this.getTipo() == "cc" || this.getTipo() == "CC") {
				this.setSaldo(50);
			} else {
				this.setSaldo(150);
			}
			
		} else {
			System.out.println("Tipo da conta inválida");
		}
	}
	
	public void fecharConta() {
		if (this.getSaldo() > 0) {
			System.out.println("Conta com dinheiro");
		} else if(this.getSaldo() < 0){
			System.out.println("Conta com pendência financeira");
		} else {
			this.setStatus(false);
		}
	}
	
	public void depositar(double valor) {
		if(this.getStatus() == true) {
			setSaldo(this.getSaldo() + valor);
		} else {
			System.out.println("Conta não está aberta");
		}
	}
	
	public void sacar(double valor) {
		if(this.getStatus() == true) {
			if(this.getSaldo() >= valor) {
				this.setSaldo(this.getSaldo() - valor);
			} else {
				System.out.println("Saldo insuficiente");
			}
		} else {
			System.out.println("conta não está aberta");
		}
	}
	
	public void pagarMensalidade() {
		int valorMensalidade;
		if(getStatus() == true) {
			if(getTipo() == "CC" || getTipo() == "cc") {
				valorMensalidade = 12;
			} else {
				valorMensalidade = 20;				
			}
			
			if(getSaldo() >= valorMensalidade) {
				setSaldo(getSaldo() - valorMensalidade);
			} else {
				System.out.println("Saldo insuficiente para a mensalidade");
			}
		} else {
			System.out.println("Impossivel pagar, conta não está aberta");
		}
	}
	
	
}
