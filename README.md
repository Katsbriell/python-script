# Lectura de facturas en formato pdf

Este proyecto obtiene datos de archivos pdf del mismo formato y los almacena en una base de datos SQLite.

## Tecnologías utilizadas

- **Python 3.x**
- **PyMuPDF==1.25.5**

## Instalación

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Katsbriell/python-script.git

2. Entra en la carpeta del proyecto:
   ```bash
   cd python-script

3. Crear un entorno virtual
- Windows
   ```bash
   virtualenv vevn
   .\venv\Scripts\activate
- Linux/Mac
  ```bash
  python -m venv env
  source env/bin/activate
4. Instalar dependencias
   ```bash
   pip install -r requirements.txt

5. Ejecutar el script
   ```bash
   python lector.py

## Uso 
Esta aplicación lee los pdfs de la carpeta predeterminada utilizando un expresión regular para encontrar un código dentro de estos y almacena en una base de datos SQLite la información correspondiente al nombre del documento, el número de páginas, el código requerido y el peso total del archivo en KB.

Si se requiere cambiar la ruta de la carpeta de las facturas puede hacerse modificando la variable 'pdfs_path' de la línea 32. 
