<!DOCTYPE html>
<html>
    <head>
        <title> Aula 02 - Aplicações para Web </title>
        <meta http-equiv="Content-Type" content="text/html" charset="UTF-8">
    </head>
    <body>
        <form action="calculo.php" method="get">
            <p><label for ="n1">Número: </label>
            <input type="number" id="n1" name="n1"></p>
            <p><label for="op">Operações: </label>
                <select name="op" id="op">
                    <option value="som">+</option>
                    <option value="sub">-</option>
                    <option value="mul">*</option>
                    <option value="div">/</option>
                </select>
            </p>
            <p><label for ="n2">Número: </label>
            <input type="number" id="n2" name="n2"></p>
            <p><input type="submit" value="Enviar" >
    </body>
</html>
