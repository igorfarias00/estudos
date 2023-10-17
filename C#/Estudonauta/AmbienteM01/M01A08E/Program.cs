int n  = 0;
Console.WriteLine("Digite um número: ");

int.TryParse(Console.ReadLine(), out n);

int dobro = n * 2;

Console.WriteLine("O dobro de "+ n + " é " + dobro);
Console.ReadKey();