import tkinter as tk
from tkinter import filedialog
import pandas as pd
import json
from pathlib import Path
import os
import subprocess
import platform

# ============================================================
#               FUNCIÓN PARA APLANAR JSON
# ============================================================

def flatten_json(data):
    """
    Convierte un JSON anidado en una lista de diccionarios planos.
    Soporta objetos y listas.
    """
    rows = []

    def flatten(obj, parent_key='', result=None):
        if result is None:
            result = {}

        # ============================================================
        #                  Recorrer cada clave del diccionario
        # ============================================================
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{parent_key}_{key}" if parent_key else key
                flatten(value, new_key, result)

        # ============================================================
        #                Si la lista está vacía, guardarla como vacía
        # ============================================================
        elif isinstance(obj, list):
            if len(obj) == 0:
                result[parent_key] = []
            else:
                # ============================================================
                #              Numerar los elementos de la lista
                # ============================================================
                for index, item in enumerate(obj):
                    new_key = f"{parent_key}_{index + 1}"
                    flatten(item, new_key, result)

        # ============================================================
        #           Valor simple, asignar al resultado
        # ============================================================
        else:
            result[parent_key] = obj

        return result

    # ============================================================
    #     Procesar datos como lista o diccionario único
    # ============================================================
    if isinstance(data, list):
        for item in data:
            rows.append(flatten(item))
    else:
        rows.append(flatten(data))

    return rows


# ============================================================
#               FUNCIONES DEL SISTEMA
# ============================================================

def open_file(path):
    """Abre un archivo con la aplicación predeterminada del sistema."""
    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.run(["open", path], check=True)
        else:
            subprocess.run(["xdg-open", path], check=True)
    except Exception as e:
        mostrar_error(f"No se pudo abrir el archivo: {e}")


def open_folder(path):
    """Abre una carpeta en el explorador de archivos."""
    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.run(["open", path], check=True)
        else:
            subprocess.run(["xdg-open", path], check=True)
    except Exception as e:
        mostrar_error(f"No se pudo abrir la carpeta: {e}")


# ============================================================
#           FUNCIÓN PRINCIPAL DE CONVERSIÓN
# ============================================================

def convertir_json_excel():
    """Selecciona un JSON, lo aplana y lo guarda como Excel en Descargas."""
    try:
        # ============================================================
        #                Seleccionar archivo JSON
        # ============================================================
        json_path = filedialog.askopenfilename(
            title="Seleccionar archivo JSON",
            filetypes=[("Archivos JSON", "*.json")]
        )
        if not json_path:
            return

        # ============================================================
        #                Leer y aplanar el JSON
        # ============================================================
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        flattened = flatten_json(data)

        # ============================================================
        #        Crear DataFrame y guardar en Descargas
        # ============================================================
        df = pd.DataFrame(flattened)
        downloads = str(Path.home() / "Downloads")
        excel_path = os.path.join(downloads, "DATOS_EXTRAIDOS.xlsx")
        df.to_excel(excel_path, index=False, engine='openpyxl')

        # ============================================================
        #   Limpiar zona dinámica (mensajes y botones anteriores)
        # ============================================================
        for widget in frame_dinamico.winfo_children():
            widget.destroy()

        # ============================================================
        #          Mostrar mensaje de éxito con ícono
        # ============================================================
        marco_exito = tk.Frame(frame_dinamico, bg="#1e272e", bd=0, highlightthickness=0)
        marco_exito.pack(pady=(15, 10), padx=20, fill="x")

        lbl_icono = tk.Label(
            marco_exito,
            text="✅",
            font=("Segoe UI", 20),
            bg="#1e272e",
            fg="#2ecc71"
        )
        lbl_icono.pack(side="left", padx=(10, 5))

        lbl_mensaje = tk.Label(
            marco_exito,
            text=f"Archivo guardado:\n{excel_path}",
            font=("Segoe UI", 10),
            bg="#1e272e",
            fg="#bdc3c7",
            justify="left",
            anchor="w"
        )
        lbl_mensaje.pack(side="left", padx=5, pady=10)

        # ============================================================
        #        Botones para abrir archivo o carpeta
        # ============================================================
        frame_botones = tk.Frame(frame_dinamico, bg="#2c3e50")
        frame_botones.pack(pady=(5, 15), padx=20, fill="x")

        btn_abrir = tk.Button(
            frame_botones,
            text="📂 Abrir archivo",
            font=("Segoe UI", 11, "bold"),
            bg="#2ecc71",
            fg="white",
            activebackground="#27ae60",
            activeforeground="white",
            bd=0,
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=lambda: open_file(excel_path)
        )
        btn_abrir.pack(side="left", padx=(0, 10), expand=True, fill="x")

        btn_carpeta = tk.Button(
            frame_botones,
            text="📁 Abrir carpeta",
            font=("Segoe UI", 11, "bold"),
            bg="#e67e22",
            fg="white",
            activebackground="#d35400",
            activeforeground="white",
            bd=0,
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=lambda: open_folder(os.path.dirname(excel_path))
        )
        btn_carpeta.pack(side="left", expand=True, fill="x")

    except Exception as e:
        # ============================================================
        #           Mostrar error en la interfaz
        # ============================================================
        mostrar_error(str(e))


# ============================================================
#               MOSTRAR ERROR EN INTERFAZ
# ============================================================

def mostrar_error(mensaje):
    """Muestra un mensaje de error dentro de la ventana."""
    for widget in frame_dinamico.winfo_children():
        widget.destroy()
    lbl_error = tk.Label(
        frame_dinamico,
        text=f"❌ Error: {mensaje}",
        font=("Segoe UI", 10, "bold"),
        bg="#2c3e50",
        fg="#e74c3c",
        wraplength=450,
        justify="left"
    )
    lbl_error.pack(pady=20, padx=20)


# ============================================================
#            CONFIGURACIÓN DE VENTANA
# ============================================================

root = tk.Tk()
root.title("JSON -> Excel")
ancho_ventana = 560
alto_ventana = 500

# ============================================================
#          Centrar la ventana en la pantalla
# ============================================================
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (ancho_ventana // 2)
y = (screen_height // 2) - (alto_ventana // 2)
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# ============================================================
#                    ENCABEZADO
# ============================================================

header = tk.Frame(root, bg="#1e272e", height=80)
header.pack(fill="x")
header.pack_propagate(False)

titulo = tk.Label(
    header,
    text="🗂️ Convertidor JSON a Excel",
    font=("Segoe UI", 17, "bold"),
    bg="#1e272e",
    fg="#f1c40f"
)
titulo.pack(expand=True)

# ============================================================
#                  CUERPO PRINCIPAL
# ============================================================

cuerpo = tk.Frame(root, bg="#2c3e50", bd=0)
cuerpo.pack(expand=True, fill="both", padx=25, pady=20)

# ============================================================
#          Descripción de la aplicación
# ============================================================
descripcion = tk.Label(
    cuerpo,
    text="Selecciona cualquier archivo JSON.\nEl Excel se guardará automáticamente en Descargas.",
    font=("Segoe UI", 11),
    bg="#2c3e50",
    fg="#bdc3c7",
    justify="center"
)
descripcion.pack(pady=(5, 20))

# ============================================================
#   Botón principal para iniciar la conversión
# ============================================================
btn_convertir = tk.Button(
    cuerpo,
    text="📄 Seleccionar JSON y Convertir",
    font=("Segoe UI", 13, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    padx=30,
    pady=12,
    bd=0,
    relief="flat",
    cursor="hand2",
    command=convertir_json_excel
)
btn_convertir.pack(pady=15)

# ============================================================
#                Separador visual
# ============================================================
separador = tk.Frame(cuerpo, bg="#34495e", height=2)
separador.pack(fill="x", pady=10)

# ============================================================
#          ZONA DINÁMICA (RESULTADOS)
# ============================================================

frame_dinamico = tk.Frame(cuerpo, bg="#2c3e50")
frame_dinamico.pack(fill="both", expand=True, pady=10)

# ============================================================
#             Iniciar la aplicación
# ============================================================
root.mainloop()