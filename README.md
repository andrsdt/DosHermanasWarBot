# DosHermanasWarBot

El bot está hecho en Python, con una estructura procedural. Se divide en tres carpetas:

1. En **data** se almacenan los recursos necesarios para ejecutarlo (archivo de texto plano con los barrios, fuente de texto que aparece en la imagen, y fondo vacío sobre el que se escriben los barrios).

2. En **out** se guardan las imágenes que se van generando. El archivo 'updated_img.png' es el que se va siendo sobreescrito con cada ejecución del programa y subido a Twitter.

3. En **src** se encuentra el código del programa, dividido en módulos. Se ejecuta main.py desde la carpeta principal, escribiendo desde terminal ```python ./src/main.py```

Los barrios ganador y perdedor se eligen aleatoriamente mediante el método choice de la clase random. Se puede modificar el archivo ```modificadores.py``` para que, al ganar o perder determinados barrios, el mensaje resultante sea personalizado para él.

El diccionario que contiene los barrios que quedan se guarda en la carpeta **tmpdumps** para que al ejecutar el programa continúe por donde lo dejó la última vez.

Para que el programa se ejecute automáticamente puede alojarse en algún servicio online como Heroku y que se ejecute automáticamente a la hora deseada, y ya que el almacenamiento en este tipo de servicios suele ser muy volátil, conviene subir los archivos temporales (imagen actualizada y archivo de diccionario dumpeado con Pickle) a la nube. He utilizado un bucket S3 pero realmente se puede utilizar cualquier otro servicio, mientras permita su integración con Python para que al ejecutarlo descargue los archivos de la nube y antes de cerrarse suba los archivos actualizados.
