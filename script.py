import fitz  # Librería PyMuPDF para leer PDFs
import os  # Para manejar archivos y directorios
import re  # Para expresiones regulares
import sqlite3  # Para manejar bases de datos SQLite

con = sqlite3.connect("sqlite.db")
cur = con.cursor()
# Expresión regular
regex = r'\b([0-9a-fA-F]\n*){95,100}\b'


def save_data_bd(filename, pages, data, weight):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS datos_facturas (filename TEXT, pages INTEGER, data TEXT, weight_kb INTEGER)")
    cur.execute("INSERT INTO datos_facturas (filename, pages, data, weight_kb) VALUES (?, ?, ?, ?)",
                (filename, pages, data, weight))
    con.commit()


def get_data_bd():
    response = cur.execute("SELECT * FROM datos_facturas")
    for row in response.fetchall():
        print(row)


def get_data(path):
    filename = os.path.basename(path)
    _, ext = os.path.splitext(path)

    if ext.lower() == ".pdf":
        pdf_path = os.path.join(path)

        file = fitz.open(pdf_path)
        pages = file.page_count
        weight = os.path.getsize(pdf_path)
        content = ""

        for page in file:
            content = page.get_text()
            data = re.findall(regex, content)

            if data:
                for bloque in page.get_text("blocks"):
                    block_text = bloque[4]
                    if "CUFE" in block_text:
                        cufe = block_text.replace(
                            "\n", "").replace("CUFE", "").strip()
    file.close()
    save_data_bd(filename, pages, cufe, weight)


# Para leer todos los archivos PDF de una carpeta
for files in os.listdir("facturas"):
    pdf_path = os.path.join("facturas", files)
    get_data(pdf_path)

# Para leer un archivo PDF específico
get_data("facturas/E54110424120908R001363335100.PDF")

# Opcional para ver la información guardada en la base de datos
get_data_bd()
con.close()
