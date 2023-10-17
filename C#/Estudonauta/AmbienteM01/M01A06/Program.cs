const string escola = "Estudonauta";
const float PI = 3.1415f;

//escola = "CursoEmVideo"; //erro, tentando alterar uma constante

Console.WriteLine("Eu estudo no " + escola);

Console.WriteLine("O valor de Pi é " + PI);
Console.WriteLine("O tipo de PI no meu programa é " + PI.GetType());

Console.WriteLine("O valor OFICIAL de Pi é " + Math.PI);
Console.WriteLine("O tipo de PI na biblioteca Math é " + Math.PI.GetType());
Console.ReadKey();
