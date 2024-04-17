# C21 [Español]   

[![en](https://img.shields.io/badge/Change_Language_to-English-%23EA736F)](https://github.com/ktehllama/C21)
## Generador de Guita Infinita!
Hablando en serio, C21 es una _Calculadora de Conteo de Cartas de Blackjack_ con una interfaz gráfica integrada hecha usando la biblioteca [Tkinter](https://docs.python.org/3/library/tkinter.html). Tiene 4 métodos de conteo de cartas integrados (que se detallan más adelante en este hermoso leéme), una interfaz de terminal a todo color y muchas más características para todas tus necesidades de conteo de cartas en línea, o simplemente para ~~robar~~ pedir prestado algo de código, ¿no?

- Rápido y Compacto
- Se Requiere un Entendimiento Básico de Blackjack
- 🔥 Vence al Casino 🔥

<details>
  <summary>Imágenes (Haz clic aquí):</summary>
<br>
<img src="https://github.com/ktehllama/C21/blob/main/C21-imgs/c21-startup.PNG" alt="c21-startup" />
<br>
<img src="https://github.com/ktehllama/C21/blob/main/C21-imgs/c21-demo.PNG" alt="c21-demo" />
</details>

## Antes de Empezar...
Antes de poder usar esta herramienta efectivamente, es importante que tengas un entendimiento concreto de lo siguiente:
- Cómo jugar al Blackjack
- Cómo funcionan los métodos de conteo de cartas que se usan en C21
- Cómo usar las tablas de estrategia básica

Aprender a jugar al Blackjack es probablemente lo más sencillo de todo. Puedes ver [este increíble video de Blackjack Apprenticeship](https://www.youtube.com/watch?v=PljDuynF-j0) para aprender Blackjack rápidamente y fácilmente. También necesitarías memorizar diferentes palabras clave que se usan comúnmente al hablar sobre Blackjack, como el conteo, conteo verdadero, penetración del mazo, y más. Todo lo que necesitas hacer es memorizar cómo funcionan los métodos de conteo de cartas para aprender a usarlos. Los que se usan en C21 son:
- [HiLo](https://wizardofodds.com/games/blackjack/card-counting/high-low/)
- [Omega II](https://www.casinoguardian.co.uk/blackjack/omega-ii-blackjack-system/)
- [KO](https://www.bonusinsider.com/blackjack/the-knock-out-card-counting-system/)
- [Cuenta de Ases y Cincos](https://wizardofodds.com/games/blackjack/ace-five-count/)

Puedes hacer clic en los enlaces para obtener más información sobre los métodos o puedes ir al archivo `bjstrats.yaml` en el proyecto, donde bajo el nombre del método hay una etiqueta `description` que tiene toda la información bien condensada para leer (en __inglés__), aunque aún así recomendaría buscar sitios para investigar o visitar los sitios web enlazados arriba.

Finalmente, las tablas de estrategia básica te enseñan exactamente cuándo: pedir o plantarte, doblar, dividir parejas o rendirse. Estas son extremadamente útiles de tener y recomiendo [esta](https://www.blackjackapprenticeship.com/blackjack-strategy-charts/), también de Blackjack Apprenticeship.

## Instalación
C21 requiere una versión de [Python](https://www.python.org/) 3.10 o superior. Una vez que hayas instalado Python y lo hayas configurado, instala C21 como un archivo Zip y ejecuta el archivo principal: `akr_main.py`

> __Nota importante:__
Más adelante, agregaré un archivo EXE donde la calculadora se podrá ejecutar directamente sin la necesidad de instalar Python.

La única instalación de pip necesaria es `pyyaml`, los archivos auxiliares ya están allí y el resto de los módulos ya están integrados en Python.
```
pip install pyyaml
```

__IMPORTANTE__: Antes de ejecutar el programa, tenes que cambiar la variable `method_file` en `method_parse.py`, ubicado en la parte superior del script después de las importaciones, a la _ruta del archivo_ de tu `bjstrats.yaml`. Ahí es donde se almacenan todos los métodos, y es esencial para C21. Si no se encuentra ningún archivo yaml, la terminal arrojará un error, o no se ejecutará en absoluto. También debes cambiar la constante `DECKS` cerca de la parte superior de `akr_main.py` al número de mazos con los que estás jugando con, está configurada en `6` por defecto.

## Cómo Usar C21
Cuando ejecutas el archivo principal, aparecerá una interfaz gráfica de calculadora en la pantalla y la terminal te proporcionará información sobre los métodos actuales que se están ejecutando y el estado general del programa. Esta ventana es redimensionable y te recomiendo que la ajustes a tu gusto, solo no la hagas demasiado pequeña.

Hay 4 partes diferentes en esta calculadora:
- La ___matriz de métodos___, ubicada en la parte superior izquierda con cuatro secciones
- La ___barra lateral de información___, ubicada a la derecha de la matriz de métodos
- La ___barra de historial___, ubicada debajo de la matriz de métodos
- Y el ___teclado de cartas___, ubicado debajo de la barra de histor

ial

### Matriz de Métodos
Esta sección está dividida en cuatro, un cuadrante para cada método.

__FILA SUPERIOR:__ HiLo, Omega II
__FILA INFERIOR:__ KO, ACEFC (Para el resto de este leéme, la Cuenta de Ases y Cincos se abreviará así)

Los métodos de la fila superior son todos sistemas equilibrados, lo que significa que tienen conteos verdaderos, los de la fila inferior solo tienen conteos en curso. El color de las casillas cambiará de rojo a azul a verde dependiendo del conteo verdadero y del conteo en curso. Estos colores representan las recomendaciones de apuestas, o en otras palabras, cuánto deberías apostar en la próxima ronda. Las recomendaciones también se muestran en texto bajo el _RC_ y _TC_ (Recuento en curso, Recuento verdadero).

__ESPECTRO:__ 🟥 Rojo: Apuesta mínima -> 🟦 Azul: Apuesta neutral -> 🟩 Verde: Aumentar apuesta

Esta es la sección más importante de todas, ya que te dice cómo ajustar tus apuestas en consecuencia, presta
mucha atención y memoriza todas las interacciones de los métodos entre sí.

### Barra Lateral de Información
A la derecha de la matriz de métodos está la barra lateral de información. Te indica tu última carta jugada (PC), la cantidad decimal de mazos restantes (DL) y el número de todas las cartas restantes en el mazo (AC).

### Barra de Historial
Debajo de la matriz de métodos está la barra de historial. Te muestra las últimas _10_ cartas que has jugado, con el índice más a la izquierda siendo el más reciente, y el más a la derecha siendo el último. (Todos _Jotas, Reinas y Reyes_ se cuentan como _Dieces_)
```
Más Reciente >---------------> Más Antiguo
Historial: 5, 6, A, 9, 10, 2, A, 2, 10
```

> __Consejo Profesional:__
Puedes cambiar el límite de las cartas que muestra de 10 a otro número yendo a la función `append_limit` y cambiando el valor predeterminado del parámetro `limit` a otro número. Trata de no hacerlo demasiado grande ya que todas las cartas no cabrán en la interfaz gráfica de usuario.

### Teclado de Cartas
El hermoso teclado de cartas te permite ingresar tus cartas para que puedas usar la calculadora (wow!). En una configuración de 5x2, todo lo que necesitas hacer es presionar el botón correspondiente a la(s) carta(s) que deseas insertar en la calculadora. __Como recordatorio__, todos los Jacks, Queens y Kings se cuentan como Dieces, así que el botón para 10 incluye las letras J Q K para que no te preguntes dónde están o si olvidé incluirlos.

### Depuración en la Terminal
Buen trabajo, ahora sabes cómo usar la GUI y qué significan todas las secciones. Pero es posible que hayas notado que cuando inicias C21 y cada vez que presionas un botón de carta, obtienes información en la terminal, todo esto es para fines de depuración y para mostrar lo que está sucediendo. Hay 5 etiquetas diferentes que puedes obtener junto con un mensaje en la terminal:
- Éxito
- Aviso
- Información
- Advertencia
- Error

Cada uno tiene su propio color y son autoexplicativos, los únicos que realmente necesitan explicación son _aviso_ e _información_. Información se usa cuando el programa devuelve conjuntos de datos como los diccionarios necesarios para almacenar los conteos y recomendaciones. Aviso, por otro lado, se utiliza para mostrar qué funciones se están llamando y una versión rudimentaria de la barra lateral de información. También hay una versión rudimentaria del sistema de recomendaciones impresa en la terminal. Allí, los cuatro nombres de método se imprimen y te dicen si debes aumentar o disminuir tus apuestas.
```
HILO: - OMEGAII: - KO: - ACEFC:
(Inc = Aumentar Apuesta, Neu = Apuesta Neutral, Neg = Apuesta Mínima)
```

Cuando ejecutas el programa, lo primero que te dirá es si se está ejecutando en Windows u otro sistema operativo, esto se utiliza para activar el color en la terminal para que puedas ver todas las hermosas etiquetas de colores. También te dirá si el archivo yaml para los métodos se ha cargado correctamente y los métodos que usará.

### Restablecimiento
Si deseas restablecer la calculadora y sus valores por completo, tendrás que cerrar el programa y ejecutarlo nuevamente. No he implementado un botón de restablecimiento ya que puedes correr el riesgo de perder tu progreso por accidente. Agradecería tus comentarios si te gustaría que se incluyera un botón de restablecimiento.

## Una Palabra Sobre la Penetración del Mazo en Casinos en Línea
Los casinos en línea suelen tener una baja penetración del mazo, lo que significa que colocan una carta especial en algún lugar del zapato (todos los mazos) para que sepan cuándo volver a barajar. Esto significa que podrías obtener cartas muy malas al principio y que esté a punto de mejorar mucho, pero el crupier vuelve a barajar antes de que puedas llegar a esas cartas de alto valor. Esto significa que al contar cartas en línea, debes tener mucha paciencia o simplemente buscar una mesa buena con una alta penetración.

## Y Finalmente...
Espero que hayas encontrado este proyecto algo interesante y que hayas aprendido algo de él. C21 tomó alrededor de 2 semanas en completarse con retrasos, pero resultó bastante bien si lo digo yo mismo. Me inspiré para hacer algo como esto gracias a la película de [1988 "Rainman"](https://en.wikipedia.org/wiki/Rain_Man), gran película, recomiendo mucho verla.

Ahora te dejo con esta información en este README, y con el conocimiento de que ahora puedes vencer a cualquier casino en línea si usas esta herramienta correctamente. ¡Buena suerte! :)

> __IMPORTANTE__: Yo, `ktehllama`, no soy responsable en absoluto de ninguna pérdida monetaria por tu parte ni de cualquier otro problema legal que pueda surgir al usar un programa asistido para contar cartas, esto es solo para fines educativos, usalo bajo tu propio consentimiento y riesgo.

## Licencia
CC0 1.0 Universal 
