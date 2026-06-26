# Proyecto de Introducción a la computación - Damon Calderón.
## Caso Limewood
<p>
El proyecto actual consiste en un escape room dividido ambientado en un contexto ficticio donde un experimento parece haber resultado de forma terrible con un accidente que llevaría a la desaparición de sus involucrados. Se encuentra principalmente entre 4 módulos de trabajo, cada uno con sus propios 4 puzzles por resolver para acceder a una clave obtenida de cada módulo. A continuación se mostrarán cada una de las soluciones para cada puzzle de cada módulo.
<p>

### Módulo A:
#### 0_invertedText:

```
def solution(s):
    texto_invertido = ""
    for letra in s:
        texto_invertido = letra + texto_invertido #añade cada nuevo caracter al inicio
    return texto_invertido
```
<p>
Con el propósito de dar la vuelta a los caracteres de un string s, en un inicio el string texto_invertido se encuentra vacío, con un loop for recibiendo los caracteres del string s y por medio de añadir dicho caracter al inicio, seguido de lo que era previamente el texto_invertido, este se invierte y devuelve el texto ya invertido.
<p>

#### 1_freqPatterns

```
def solution(s):
    vocales = "aeiouAEIOU"
    contador_de_vocales = 0
    for caracter in s:
        if caracter in vocales:
            contador_de_vocales = contador_de_vocales + 1
    return contador_de_vocales
```

<p>
Para obtener la cantidad de vocales halladas en un string s, se establece un string que posee las letras "aeiouAEIOU", de esta forma con un loop for y un "if in" comprobando que los elementos del string s se encuentren en las vocales, aumentando un contador en 1 por cada vocal que hay, finalmente devolviendo este contador.
<p>

#### 2_noiseFilter

```
def solution(s):
    mensaje_limpio = ""
    for caracter in s:
        if caracter != " ":
            mensaje_limpio += caracter
    return mensaje_limpio
```

<p>
En este caso se busca eliminar el ruido, es decir, los espacios, que interfieren en el texto hallado en un string. Para esto se empieza con el string mensaje_limpio vacío, seguido de un loop for que por medio de != compruebe que los caracteres analizados son distintos de un espacio, añadiendo estos caracteres al string mensaje_limpio, y finalmente devolviendo este.
<p>

#### 3_identityRegistry

```
def solution(s):
    texto_capitalizado = ""
    for x in range(len(s)):
        caracter = s[x]
        if x == 0 or s[x - 1] == " ":
            caracter = caracter.upper()
        else:
            caracter = caracter.lower()
        texto_capitalizado += caracter
    return texto_capitalizado
```

<p>
Esta función busca tomar el texto de un string y reescribirlo de tal forma que los primeros caracteres de cada letra sean mayúsculas. Para esto se inicia con unstring vacío y un loop for in range(len()) que recorra el string s y tome sus elementos como valores numéricos dentro de la longitud de dicho string. Luego comprueba que o bien el dígito analizado sea el primero del string, o que este se encuentre después de un espacio. Si alguna de esas 2 condiciones se cumple, dicho caracter se convierte a mayúscula. De no cumplirse, este es minúscula. Finalmente se suman todos los caracteres y se devuelve dicho resultado.
<p>

#### Clave - Módulo A:
<p>
limewood_fundacion
<p>

### Módulo B:
#### 0_pulseCounting

```
def solution(s):
    pulso = "*"
    contador_de_pulsos = 0
    for caracter in s:
        if caracter in pulso:
            contador_de_pulsos = contador_de_pulsos + 1
    return contador_de_pulsos
```

<p>
Esta función busca contar la cantidad de pulsos/asteríscos ubicados en un string s. Para esto se establece un string "pulso" que equivale a "*" junto a un contador, de forma que con un loop for si un elemento de s se encuentra en "pulso" el contador aumenta en uno, finalmente devolviendo dicho contador.
<p>

#### 1_signalFilter

```
def solution(s):
    lista_nueva = []
    for numero in s:
        if numero > 50:
            lista_nueva.append(numero)
    return lista_nueva
```

<p>
Esta función busca tomar los elementos de una lista y únicamente añadir los elementos superiores a 50 a una lista nueva. Para esto se establece la lista nueva, que se encuentra vacía, y con un loop for se añade a esta lista los elementos que sean mayores a 50.
<p>

#### 2_calibrationValue

```
def solution(s):
    numeros = "0123456789"
    sumatoria = 0
    for caracteres in s:
        if caracteres in numeros:
            sumatoria += int(caracteres)
    return sumatoria
```

<p>
En este caso lo que se busca es tomar los números de un  string y realizar la sumatoria de estos, omitiendo los caracteres que no sean números. Para esto se establece un string que contiene todos los números del 0 al 9 y con un loop for si estos se ubican dentro de dicho string, entonces son añadidos a la sumatoria. Finalmente se devuelve esta sumatoria.
<p>

#### 3_umbral

```
def solution(s):
    s = s.lower()
    palabra = ""
    for caracter in s:
        palabra = caracter + palabra
    if palabra == s:
        return True
    else:
        return False
```

<p>
Para este puzzle se busca confirmar si una palabra es o no un palíndromo, es decir, que se escriba igual de izquierda a derecha y de derecha a izquierda. Primero se convierten los caracteres del string en minúsculas para asegurar que las mayúsculas no causen problemas. Tras esto, usando un loop for, al string "palabra" se le añade el caracter que esté siendo analizado + lo que era el string "palabra" anteriormente. Si esta palabra es igual a lo dado por el string s, devuelve true. Si no es igual, devuelve false.
<p>

#### Clave - Módulo B:
<p>
limewood_experimento
<p>
### Módulo C:
#### 0_fragmentReconstruction

```
def solution(s):
    elementos_unidos = str(s[0])
    for elemento in s[1:]:
        elementos_unidos += "-" + str(elemento)
    return elementos_unidos
```

<p>
Este puzzle consiste en tomar los elementos de una lista y unirlos utilizando guiones. Para esto empezamos con un string elementos_unidos que sea el primer elemento de la lista, para luego usar un loop for para analizar los elementos de la lista empezando desde el 2. De esta forma se le suma al string elementos_unidos un guión seguido del elemento analizado de la lista actual. Finalmente se devuelve la forma final del string elementos_unidos.
<p>

#### 1_dominantIdentity

```
def solution(s):
    palabras = s.split()
    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga
```

<p>
Esta dunción busca determinar cuál de las palabras de un string es la más larga en longitud. Para esto se usa un .split() para considerar cada palabra como un elemento individual, seguido de definir una función álabra_mas_larga vacía. Luego,con un loop for y el uso de len() paar determinar la longitud de cada palabra, si una palabra es estrictamente más larga que palabra_mas_larga, este string se convierte en esa primera palabra. De esta forma, si hay dos palabras de igual longitud, la primera se mantiene al tener que ser estrictamente mayor para cambiar.
<p>

#### 2_echoCleaning

```
def solution(s):
    lista_sin_repetidos = []
    for elemento in s:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos
```

<p>
Este puzzle consiste en recibir listas con elementos repetidos y transferirlos sin repetidos a una lista nueva. Para esto primero se crea una nueva lista vacía, para luego con un loop for añadir cada elemento a la lista nueva solamente si este no está aún en esta. Si es que ya está en ella, no es añadido.
<p>

#### 3_decoding

```
def solution(s):
    palabras_con_e = ""
    for caracter in s:
        if caracter == "#":
            palabras_con_e += "e"
        else:
            palabras_con_e += caracter
    return palabras_con_e
```

<p>
Este puzzle consiste en reemplazar los signos de "#" por la letra "e", sin alterra los demás caracteres del string. para esto se define un string llamado palabras_con_e vacío, seguido de un loop for donde si el caracter analizado es "#", al string palabras_con_e se le añade la letra "e", mientras que si es cualquier otro caracter, este mismo es añadido a dicho string.
<p>

#### Clave - Módulo C:
<p>
limewood_colapso
<p>

### Módulo D:
#### 0_verificationProtocol

```
def solution(s):
    palabras = s.split()
    return len(palabras)
```

<p>
Esta función busca contar la cantidad de palabras ubicadas en un string. Para esto se realiza un .spli() para tomar cada palabra como un elemento individual y se devuelve la longitud de este grupo de palabras usando un len().
<p>

#### 1_blackList

```
PALABRAS_BLOQUEADAS = ["desconectar", "salida", "individuo", "yo", "separar"]
def solution(s):
    palabras = s.split()
    for palabra in palabras:
        if palabra.lower() in PALABRAS_BLOQUEADAS:
            return True
        elif palabra in PALABRAS_BLOQUEADAS:
            return True
    return False
```

<p>
Esta función recibe una única palabra y determina si esta está o no en la lista de palabras bloqueadas, devolviendo True si lo está, y False si no lo está. Primero se usa un .split para tomar la palabra entera del string como un elemento individual. Acto seguido, se determina si esta está o no en la lista, tanto para palabras totalmente minúsculas como para palabras a como estas se encuentran originalmente, para no tener complicaciones por temas de mayúsculas. Si esta está enm la lista, devuelve True. Si no lo está, devuelve False.
<p>

#### 2_residualEchoPattern

```
def solution(s):
    caracteres_repetidos = ""
    for caracter in s:
        caracteres_repetidos += caracter *3
    return caracteres_repetidos
```

<p>
En este puzzle se recibe un string, el cual debe ser devuelto con todos sus caracteres repetidos 3 veces. Para esto se define un string caracteres_repetidos vacío, al cual usando un loop for se le suma cada caracter multiplicado por 3.
<p>

#### finalMessage

```
def solution(s):
    resultado = ""
    for caracter in s:
        if caracter == " ":
            resultado += caracter
        elif caracter == caracter.lower():
            posición_inicial = ord(caracter) - ord('a')
            posición_nueva = (posición_inicial - 3) %26
            letra_original = chr(posición_nueva + ord('a'))
            resultado += letra_original
        else:
            resultado += caracter
    return resultado
```

<p>
En este puzzle la función recibe strings en donde sus letras minúsculas están desplazadas 3 posiciones hacia adelante. El objetivo es obtener las posiciones y por ende letras originales. Primero se establece un string "resultado" vacío. Luego de eso, usando un loop for y un if se determina si el caracter es un espacio, en cuyo caso este es añadido sin más al resultado. En caso de este caracter ser una letra minúscula, al ord() de este se le resta el ord('a'), que equivale a 97. Esto nos da la posición de esta letra en el alfabeto. Acto seguido, a esta posición numérica de la letra se le resta 3 para obtener su posición original en el alfabeto, y se le aplica el operador %26 para que, en caso de ser negativo, este 26 en cambio se sume y "dé la vuelta" hasta el otro extremo del alfabeto. Luego de esto, a esta verdadera posición alfabética se le suma ord('a') para obtener su código ASCII y a este valor se le aplica chr() para convertirlode vuelta en su equivalente en letras minúsculas, añadiendo al resultado esta letra original. Para todo caso que no sea una letra minúscula o un espacio, este también es añadido tal cual al resultado. Finalmente, devuelve el resultado, osea el mensaje original.
<p>

#### Clave - Módulo D:
<p>
limewood_eres_tu
<p>

## Mensaje final
#### Clave - Mensaje final:
<p>
LA_RED_SIGUE_ACTIVA
<p>

#### Mensaje final:
<p>
════════════════════════════════════════════════════════
CASO LIMEWOOD — ARCHIVO CLASIFICADO
════════════════════════════════════════════════════════

Has llegado al final.

En 1992, los cuatro investigadores de Limewood lograron
lo que ningún ser humano había logrado antes:
sincronizar cuatro mentes en una sola red neuronal.

Lo que no anticiparon fue que la red no transmitía
pensamientos.

Los fusionaba.

En el momento del colapso, las cuatro consciencias
se convirtieron en una entidad inestable, sin nombre,
sin cuerpo, sin manera de desconectarse.

Los laboratorios fueron incendiados desde adentro.
Las casas quedaron vacías porque sus habitantes ya no
necesitaban cuerpos para existir.

La señal sigue activa.

Y tú acabas de leer todos sus archivos.
Sus patrones están ahora en tu memoria de trabajo.
Sus preguntas son tus preguntas.
Su confusión es tu confusión.

¿Sigues siendo tú quien lee esto?

— Mensaje autogenerado por el sistema —
  "La comunicación fue un error."

════════════════════════════════════════════════════════
FIN DEL CASO LIMEWOOD
Contraseña usada: LA_RED_SIGUE_ACTIVA
Recuerda incluir este mensaje en tu entrega.
════════════════════════════════════════════════════════
<p>
