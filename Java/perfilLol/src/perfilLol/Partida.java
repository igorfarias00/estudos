package perfilLol;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.http.*;
import java.util.ArrayList;
import java.util.List;
import java.net.URL;
import java.net.HttpURLConnection;
import org.json.JSONException;
import org.json.JSONObject;



public class Partida {
	Perfil jogador;
	
	public Partida(Perfil jogador) throws Exception {
		this.jogador = jogador;
		
		
		JSONObject match = new JSONObject(buscaPartida(jogador.matches.matchIds[0]));
		
	//	for(int i= 0; i < jogador.matches.matchIds.length; i++ ) {
	//		System.out.println(buscaPartida(jogador.matches.matchIds[i]));
	//	}
		
	System.out.println(match);
		
	}
	
	
	 public String buscaPartida(String matchId) throws Exception {
	        String urlParaChamada = "https://americas.api.riotgames.com/lol/match/v5/matches/"+ matchId + "?api_key=" + this.jogador.key;

	        try {
	            URL url = new URL(urlParaChamada);
	            HttpURLConnection conexao = (HttpURLConnection) url.openConnection();

	            if (conexao.getResponseCode() != 200)
	                throw new RuntimeException("HTTP error code : " + conexao.getResponseCode());

	            BufferedReader resposta = new BufferedReader(new InputStreamReader((conexao.getInputStream())));	        
	            
	            String perfil = resposta.readLine();
	            
	            conexao.disconnect();
	            return perfil;
	            
	            
	        } catch (Exception e) {
	            throw new Exception("ERRO: " + e);
	        }
	 }
}
