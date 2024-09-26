# dockerCompose
módulos de Odoo con compose para gestión de sistemas de Gestión Empresarial

--PASO 1 --
se crea un repositorio en Github de todo el proyecto 

dentro de SourceTree se debe clonar la carpeta contenedora 'composeDocker' con la url del github

--PASO 2--
Dentro de la carpeta contenedora 'composeDocker' que albergará las carpetas (config_odoo, dev-addons, log) y un archivo tipo yml llamada: 'docker-compose.yml'
desde la consola del powershell en la ruta de la carpeta contenedora se escribe el comando 'docker compose up' para que lo instale

---PASO---
En la carpeta contenedora en el archivo 'docker-compose.yml' se debe legar las siguientes líneas de código, verificar las tabulaciones ya que es python

version: '3.1'
services:
  web:
    image: odoo:17.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./config_odoo:/etc/odoo
      - ./dev-addons:/mnt/extra-addons
      - ./log:/var/log/odoo
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
  db:
    image: postgres:latest
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_USER=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - odoo-db-data:/var/lib/postgresql/data/pgdata
    
volumes:
  odoo-web-data:
  odoo-db-data:

---PASO---
dentro de composeDocker/cofig_odoo se debe crear un archivo .conf y se debe cambiar el nombre de 'admin_psswd' a uno propio, para este caso era:
  [options]
  addons_path = /mnt/extra-addons
  data_dir = /var/lib/odoo
  admin_passwd = cuervo
  logfile = /var/log/odoo/odoo-server.log

-----UNA VEZ INSTALADO-----
---PASO---
una vez instalado se accede y ya corriendo el -destop Docker- verificamos que ya esté corriendo 'composedocker'  se da click en los tres botones (show container actions) de - web-1 - y click en 'Open in Terminal' se hace un 'ls' para ver las carpetas que ha generado, vamos a la carpeta 'mnt' con: cd mnt, 'ls' para ver los archivos y debe aparecer extra-addons, 'cd extra-addons' para ingresar, ls para ver los archivos, y FINALMENTE 'odoo scarffold dam2' para que instale los componentes adicionales.

---PASO---
en composeDocker/dev-addons/views en el archivo 'views.xml' se debe eliminar una línea de 'values' dentro de <!-- explicit list view definition --> **** confirmar esto***


---PASO---
models/models.py se debe descomentar la clase con el nombre con el que se ha creado el múdolo en este caso es 'dam2'
from odoo import models, fields, api

class dam2(models.Model):
    _name = 'dam2.dam2'
    _description = 'dam2.dam2'

    name = fields.Char()
    value = fields.Integer()

---PASO---
En '__manifest__.py' se de debe descomentar el bloque de código de seguridad: 
'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

dentro de la carpeta composeDocker/dam/dev-addons/views,en el archivo views.xml se deben descomentar los siguientes bloques de código:
 <!-- explicit list view definition -->
  <!-- actions opening views on models --> (que es el que ejecuta la accion
  <!-- Top menu item -->
  <!-- menu categories -->
  <!-- actions -->
-dentro de <!-- actions opening views on models se le da un nuevo nombre a los módulo que vamos a agregar *Lista nombres*
<record model="ir.actions.act_window" id="dam2.action_window">
      <field name="name">Lista nombres</field>
      <field name="res_model">dam2.dam2</field>
      <field name="view_mode">tree,form</field>
</record>

