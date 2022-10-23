# Instrucciones para correr la app en backend
Se debera correr en una terminal de mac o linux una conexion ssh haciendo uso de la llave pem que se provee llave.pem

'''

ssh -i llave.pem ubuntu@44.230.232.104

'''

### Dentro de la instancia de amazon EC2
Ejecutar los siguentes comandos

'''

cd /var/www/src/private/Twitter
python3 run.py

'''

### Dentro del Script
Aqui podras elegir entre la palabra que quieres hacer web scraping puedes usar estos ejemplos para algun tema en especial, para usuario en twitter o algun #enespecifico

Si quieres buscar usuarios:

'''

@unikoerl

'''

Si quieres buscar palabras en espesifico de Twitter:

'''

Mujeres

'''

Si quieres buscar con # (Deberas omitir el # y solo deberas poner el tema sin separaciones):

'''

meduelesamerica

'''