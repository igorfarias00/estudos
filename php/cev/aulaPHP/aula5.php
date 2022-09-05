<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="_css/estilo.css"/>
  <meta charset="UTF-8"/>
  <title>Curso de PHP - CursoemVideo.com</title>
</head>
<body>
<div>
    <?php
        $b = 5;
        $a = 4;
        $c = 2;

        $a = $_GET["a"];
        $b = $_GET["b"];

        $soma = $a + $b + $c;
        $media = ($a + $b) / $c;
        $multiplicao = $a * $b;
        $subtracao = $b - $a;
        $divisao = $b / $c;



        echo "a soma vale ". $soma ."<br>";
        echo "a media vale ". $media ."<br>";
        echo "a multiplicao vale ". $multiplicao ."<br>";
        echo "a subtracao vale ". $subtracao ."<br>";
        echo "a divisao vale ". $divisao ."<br>";

    ?>
</div>
</body>
</html>