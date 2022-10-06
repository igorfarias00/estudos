package perfilLol;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Historico {
	public String matchIds[];
	
	public Perfil jogador;
	
	
	public Historico(Perfil jogador) throws Exception {
		this.jogador = jogador;
		String matchs = searchMatches();
		
		matchs = matchs.replace("\"", "");
		matchs = matchs.replace("[", "");
		matchs = matchs.replace("]", "");
		
		this.matchIds = matchs.split(",");
		
		
		
		
		for(int i = 0; i < matchIds.length; i++) {
			System.out.println(matchIds[i]);
		}
		


	}
	
	
	public String searchMatches() throws Exception  {
		String urlParaChamada = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+ this.jogador.getPuuid() + "/ids?start=0&count=20&api_key=" + this.jogador.key;
        
		
		try {
            URL url = new URL(urlParaChamada);
            HttpURLConnection conexao = (HttpURLConnection) url.openConnection();

            if (conexao.getResponseCode() != 200)
                throw new RuntimeException("HTTP error code : " + conexao.getResponseCode());

            BufferedReader resposta = new BufferedReader(new InputStreamReader((conexao.getInputStream())));	        
            
            String partidas = resposta.readLine();
            
            conexao.disconnect();
            return partidas;			// retorna uma string com a lista das ultimas 20 partidas
            
            
        } catch (Exception e) {
            throw new Exception("ERRO: " + e);
        }
 
	}
}
