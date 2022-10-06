package perfilLol;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.http.*;
import java.net.URL;
import java.net.HttpURLConnection;
import org.json.JSONException;
import org.json.JSONObject;

/* nesse objeto será feito a requisição para obtermos 
 * as informações basicas do perfil do lol
 * 
// url de request 
 * Nacarios10
 *  
 */

public class Perfil {
	private String id;
	private String puuid;
	public String name;
	public long level;
	public String invocador;
	public Historico matches;
	
	public String key;
	
	public Perfil(String invocador) throws Exception {
		this.key = "RGAPI-41bc2011-0c7c-44a4-8595-8ca2ce06dea3";
		JSONObject perfil_json = new JSONObject(buscaPerfil(invocador));
		
		//System.out.println(buscaPerfil(invocador)); // testa se e a conexão esta retornando o json completo
		
		System.out.println(perfil_json.get("name"));
		System.out.println("Level: " + perfil_json.get("summonerLevel"));
		System.out.println("id:" + perfil_json.get("id"));
		System.out.println("puuid: " +perfil_json.get("puuid"));
		this.setPuuid(perfil_json.get("puuid").toString());
		System.out.println("accountId: " + perfil_json.get("accountId"));
		
		
		this.matches = new Historico(this);

	}
	
	 public String buscaPerfil(String invocador) throws Exception {
	        String urlParaChamada = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ invocador + "?api_key=" + key;

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
	 
	 public void setPuuid(String puuid) {
		 this.puuid = puuid;
	 }
	 
	 public String getPuuid() {
		 return this.puuid;
	 }
}
