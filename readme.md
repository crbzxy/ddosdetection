Ejecución del Script de Detección de Ataques DDoS con Scapy

Este script en Python utiliza la librería Scapy para llevar a cabo el análisis de paquetes y 
detectar posibles ataques de denegación de servicio distribuido (DDoS) en una dirección IP y 
puerto específicos. Para asegurar un entorno de desarrollo limpio y prevenir posibles 
conflictos con las dependencias, se recomienda ejecutar el script dentro de un ambiente 
virtual. A continuación, se presenta una guía paso a paso para configurar y ejecutar el 
script:

Paso 1: Crear y Activar un Ambiente Virtual

Si aún no tienes instalado 'virtualenv', puedes hacerlo ejecutando el siguiente comando en la 
terminal:

pip install virtualenv

Después, navega al directorio donde se encuentra tu script:

cd /ruta/a/tu/directorio

A continuación, crea un ambiente virtual llamado "myenv":

virtualenv myenv

Activa el ambiente virtual recién creado:

source myenv/bin/activate

Paso 2: Instalar las Dependencias

Dentro del ambiente virtual, instala las dependencias necesarias, en este caso, la librería 
Scapy:

pip install scapy

Paso 3: Ejecutar el Script

Asegúrate de que el archivo del script que proporcionaste se encuentre en el mismo directorio. 
Luego, ejecuta el script utilizando el siguiente comando:

python tu_script.py

Paso 4: Desactivar el Ambiente Virtual

Cuando hayas finalizado con el script, puedes desactivar el ambiente virtual utilizando:

deactivate

Estos pasos te permitirán ejecutar el script en un ambiente virtual aislado, asegurando que 
las dependencias correctas estén instaladas y evitando conflictos con otras bibliotecas.

Nota: Asegúrate de modificar las variables 'target_ip' y 'target_port' en el script para que 
coincidan con la dirección IP y el puerto que deseas monitorear. Ten en cuenta que este script 
está diseñado con fines educativos y de aprendizaje, y la detección de ataques DDoS en un 
entorno real puede requerir técnicas más avanzadas.

# ddosdetection
