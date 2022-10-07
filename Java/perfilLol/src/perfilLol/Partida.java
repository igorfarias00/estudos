package perfilLol;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.http.*;
import java.util.ArrayList;
import java.util.List;
import java.net.URL;
import java.net.HttpURLConnection;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;



public class Partida {
	Perfil jogador;
	
	public Partida(Perfil jogador) throws Exception {
		this.jogador = jogador;
		
		
		JSONObject match = new JSONObject(buscaPartida(jogador.matches.matchIds[0]));
		
		
		System.out.println(match);
		
		if(this.createHTML()) {
			this.writeHTML(this.jsonToHtml(match));
		} else {
			System.out.println("FAIL");
		}
		
		System.out.println(match.getJSONObject("metadata").get("participants"));
		
	}
	
	public boolean createHTML() throws Exception {
		try {
		      File myObj = new File("partida.html");
		      
		     
		      if (myObj.createNewFile()) {
		        System.out.println("File created: " + myObj.getName());
		      } else {
		        System.out.println("File already exists.");
		      }
		      return true;
		      
		} catch (IOException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		      return false;
	    }
	}
	
	
	public void writeHTML(String html) {
	    try {
	        FileWriter myWriter = new FileWriter("partida.html");
	        myWriter.write(html);
	        myWriter.close();
	        System.out.println("Successfully wrote to the file.");
	        
	    } catch (IOException e) {
	        System.out.println("An error occurred.");
	        e.printStackTrace();
	    }
	}
	
	private String jsonToHtml( Object obj ) {
	    StringBuilder html = new StringBuilder( );

	    try {
	        if (obj instanceof JSONObject) {
	            JSONObject jsonObject = (JSONObject)obj;
	            String[] keys = JSONObject.getNames( jsonObject );

	            html.append("<div class=\""+ keys[0] +"\">");

	            if (keys.length > 0) {
	                for (String key : keys) {
	                    // print the key and open a DIV
	                	//System.out.println(key);
	                	//System.out.println(key);
	                	if(key == "participants") {
	                		Object val = jsonObject.getJSONObject("metadata").get(key);
	                		String valS = val.toString();
	                		String[] participants;
	                		valS.replace("[", "");
	                		valS.replace("]", "");
	                		participants = valS.split(",");
	                		
	                		
		                    html.append("<div><span id=\""+ key +"\"></span> : " );
		                    
		                    for(int i= 0; i < participants.length; i++) {
		                    	System.out.println(participants[i]);
		                    	 html.append(key).append("<span id=\""+ key + ""+ i +" \">");
				                    // recursive call
				                 html.append(participants[i]);
				                    // close the div
				                 html.append("</span></div>\n");
		                    }
	                       

		                    

	                		
	                	} else {
		                    html.append("<div><span id=\""+ key +"\">")
		                        .append(key).append("</span> : <span id=\""+ key + "Value \">");
	
		                    Object val = jsonObject.get(key);
		                    // recursive call
		                    html.append( jsonToHtml( val ) );
		                    // close the div
		                    html.append("</span></div>\n");
	                	}
	                }
	            }

	            html.append("</div>");

	        } else if (obj instanceof JSONArray) {
	            JSONArray array = (JSONArray)obj;
	            for ( int i=0; i < array.length( ); i++) {
	                // recursive call
	                html.append( jsonToHtml( array.get(i) ) );                    
	            }
	        } else {
	            // print the value
	            html.append( obj );
	        }                
	    } catch (JSONException e) { return e.getLocalizedMessage( ) ; }

	    return html.toString( );
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
