package perfilLol;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.http.*;
import java.net.URL;
import java.net.HttpURLConnection;
import org.json.JSONException;
import org.json.JSONObject;



public class Partida {
	Perfil jogadores [];
	public String key = "RGAPI-a6bde009-d455-4928-adfb-6a0bd4abc88d";
	
	public Partida(Perfil jogador) throws Exception {
		//JSONObject partidas = new JSONObject(buscaPartidas(jogador));
		
		System.out.println(buscaPartidas(jogador));
		
		
	}
	
	
	public String buscaPartidas(Perfil jogador) throws Exception  {
		String urlParaChamada = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+ jogador.getPuuid() + "/ids?start=0&count=20?api_key=" + this.key;
        
		try {
            URL url = new URL(urlParaChamada);
            HttpURLConnection conexao = (HttpURLConnection) url.openConnection();

            if (conexao.getResponseCode() != 200)
                throw new RuntimeException("HTTP error code : " + conexao.getResponseCode());

            BufferedReader resposta = new BufferedReader(new InputStreamReader((conexao.getInputStream())));	        
            
            String partidas = resposta.readLine();
            
            conexao.disconnect();
            return partidas;
            
            
        } catch (Exception e) {
            throw new Exception("ERRO: " + e);
        }
 
	}
}
