<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aproximacion Por Minimos Cuadrados</title>
        <link rel="stylesheet" type="text/css" href="recursos/style.css">
    </head>

    <body>
        <div id="display">
            <div id='base'>
                <form action="index.php" method="post">
                    <div id="funcion">
                        <label for="func">Añadir funcion:</label>
                        <input type="text" id="func" name="func" size="10px">
                        <br>
                        <input type="submit" value="Añadir" >
                    </div>
                </form>
                <div id='bases'>
                    <?php
                        $func = $_POST["func"];
                        echo $func;
                    ?>
                </div>
            </div>
        </div>
    </body>

</html>