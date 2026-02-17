\# Web Load Test



Proyecto de pruebas de carga para la plataforma WEB utilizando Python, Locust y BeautifulSoup.



Este proyecto permite simular usuarios reales navegando, buscando productos y generando carga sobre el servidor.



---



\# Requisitos



Antes de comenzar, asegúrate de tener instalado:



\- Python 3.10 o superior

\- Git

\- Acceso al dominio a testear



Puedes verificar Python con:



```bash

python --version

Instalación paso a paso

1\. Clonar el repositorio

git clone https://github.com/fiship69/web-loadtest

cd web-loadtest



2\. Crear entorno virtual

Windows

python -m venv venv

venv\\Scripts\\actívate


Mac / Linux

python3 -m venv venv

source venv/bin/activate


Si se activó correctamente, verás (venv) en la terminal.



3\. Instalar dependencias

pip install -r requirements.txt

Esto instalará las librerías necesarias como Locust, BeautifulSoup y Requests.



4\. Ejecutar la prueba de carga

locust -f locustfile.py --host=https://TUDOMINIO.CL

Reemplaza TUDOMINIO.CL por el dominio real que deseas probar.



5\. Abrir la interfaz web de Locust

En el navegador abre:



http://localhost:8089



Configura los siguientes parámetros:



Number of Users: 70



Spawn Rate: 2



Luego presiona Start Swarming.


Monitoreo del servidor



Mientras corre la prueba, conectarse al VPS por SSH y ejecutar:



htop





o



top





Se debe observar:



Uso de CPU



Load average



Errores 500



Tiempos de respuesta

