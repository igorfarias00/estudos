package vetor;

import java.util.Arrays;

public class Vetor {

    private Aluno[] alunos = new Aluno[100];
    private int totalDeAlunos = 0;
    
    public void adiciona(int posicao, Aluno aluno) {
    		this.garanteEspaco();
    	   if(!posicaoValida(posicao)) {
    	        throw new IllegalArgumentException("posicao invalida");
    	    }
    	    for(int i = totalDeAlunos - 1; i >= posicao; i-=1) {
    	        alunos[i+1] = alunos[i];
    	    }
    	    alunos[posicao] = aluno;
    	    totalDeAlunos++;
    }
    
    private void garanteEspaco() {
        if(totalDeAlunos == alunos.length) {
            Aluno[] novoArray = new Aluno[alunos.length*2];
            for(int i = 0; i < alunos.length; i++) {
                novoArray[i] = alunos[i];
            }
            this.alunos= novoArray;
        }

    }
    
   public void adiciona(Aluno aluno) {
        //recebe um aluno
	   this.garanteEspaco();
    	  for(int i = 0; i < alunos.length; i++) {
              if(alunos[i] == null) {
                  alunos[i] = aluno;
                  totalDeAlunos++;
                  break;
              }
          }
    }
   
   private boolean posicaoValida(int posicao) {
	    return posicao >= 0 && posicao <= totalDeAlunos;
	}
	
    public Aluno pega(int posicao) {
        //recebe uma posição e devolve o aluno
    	 if(!posicaoOcupada(posicao)) {
             throw new IllegalArgumentException("posiçao invalida");
         }
    	
        return alunos[posicao];
    }

    private boolean posicaoOcupada(int posicao) {
        return posicao >= 0 && posicao < totalDeAlunos;
    }
    
    public void remove(int posicao) {
        //remove pela posição
        for(int i = posicao; i < this.totalDeAlunos; i++) {
            this.alunos[i] = this.alunos[i+1];
        }
        totalDeAlunos--;
    }

    public boolean contem(Aluno aluno) {
        //descobre se o aluno está ou não na lista
    	  for(int i = 0; i < totalDeAlunos; i++) {
              if(aluno.equals(alunos[i])) {
                  return true;
              }
          }
        return false;
    }

    public int tamanho() {
        //devolve a quantidade de alunos
        return totalDeAlunos;
    }

    public String toString() {
        //facilitará na impressão
        return Arrays.toString(alunos);
    }
    
 
}