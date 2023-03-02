package idioma;

import java.util.Properties;
import java.awt.*;

public class Main {
	public static void main(String[] args) {
		Properties p = System.getProperties();
		p.list(System.out);
		
		Dimension screensize = Toolkit.getDefaultToolkit().getScreenSize();
		int width = (int)screensize.getWidth();
		int height = (int)screensize.getHeight();
		System.out.println(width + " / " + height);
		
	}
}
