// Conversão implicita --------------------------------------------------------
int a = 8;

float b = a;
// int para float
Console.WriteLine("O valor de a é " + a + ", e é do tipo " + a.GetType());
Console.WriteLine("O valor de b é " + b + ", e é do tipo " + b.GetType());
Console.WriteLine("O valor da soma de a e b é " + (a + b) + " sendo do tipo " + (a + b).GetType() ) ;

Console.ReadKey();

// float para int
float c = 3.2f;

//int d = c; // gera um erro, um inteiro cabe em um float, um float nao cabe em um inteiro

Console.WriteLine("O valor de a é " + c + ", e é do tipo " + c.GetType());
//Console.WriteLine("O valor de b é " + d + ", e é do tipo " + d.GetType());
//Console.WriteLine("O valor da soma de a e b é " + (c + d) + " sendo do tipo " + (c +d).GetType());

Console.ReadKey();



// Conversão explicita - TypeCast  ----------------------------------------------------

float e = 3.2f;

int f = (int)e; 

Console.WriteLine("O valor de a é " + e + ", e é do tipo " + e.GetType());
Console.WriteLine("O valor de b é " + f + ", e é do tipo " + f.GetType());
Console.WriteLine("O valor da soma de a e b é " + (e + f) + " sendo do tipo " + (e + f).GetType());

Console.ReadKey();

// Conversão por classes auxiliares  ---------------------------------------------------

float x = 5.502f;
int y = Convert.ToInt16(x);

Console.WriteLine("O valor de y é "+ y + " e o tipo é "+ y.GetType());
Console.WriteLine("O valor de x é "+ x +" e o tipo é "+ x.GetType());