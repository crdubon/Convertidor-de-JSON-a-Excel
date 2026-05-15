# JSON to Excel Converter

Aplicación de escritorio hecha en Python para convertir archivos JSON a Excel de forma rápida y sencilla mediante una interfaz gráfica.

El programa permite seleccionar cualquier archivo `.json`, procesarlo aunque tenga estructuras anidadas y generar automáticamente un archivo `.xlsx` listo para usar en Excel.

El archivo generado se guarda automáticamente en la carpeta de Descargas con el nombre:

```text id="z9t0uk"
DATOS_EXTRAIDOS.xlsx
```

---

# Características

* Conversión automática de JSON a Excel
* Soporte para JSON anidados
* Interfaz gráfica simple y moderna
* Guardado automático en Descargas
* Compatible con Windows, Linux y macOS
* Botones para abrir el archivo o la carpeta directamente

---

# Librerías utilizadas

## Tkinter

```python id="4dxyc8"
import tkinter as tk
from tkinter import filedialog
```

Se utiliza para toda la interfaz gráfica de la aplicación.

Incluye:

* Ventana principal
* Botones
* Selector de archivos
* Mensajes dinámicos
* Diseño visual

Tkinter ya viene incluido con Python.

---

## Pandas

```python id="3w6g0r"
import pandas as pd
```

Se utiliza para organizar la información y convertir los datos del JSON en tablas Excel.

Instalación:

```bash id="d9z3wk"
pip install pandas
```

---

## OpenPyXL

Pandas utiliza esta librería para generar el archivo `.xlsx`.

Instalación:

```bash id="ok6mgh"
pip install openpyxl
```

---

## JSON

```python id="zyw7am"
import json
```

Permite leer y procesar archivos JSON.

---

## Pathlib

```python id="8r7v4g"
from pathlib import Path
```

Se utiliza para detectar automáticamente la carpeta Descargas del usuario.

---

## OS

```python id="9ocq54"
import os
```

Permite trabajar con rutas y archivos del sistema.

---

## Subprocess

```python id="6wh86f"
import subprocess
```

Se utiliza para abrir carpetas y archivos en Linux y macOS.

---

## Platform

```python id="lrn6nm"
import platform
```

Detecta el sistema operativo actual para ejecutar correctamente algunas funciones.

---

# Instalación

Clona el repositorio:

```bash id="ewjxwb"
git clone https://github.com/tuusuario/tu-repositorio.git
```

Entra a la carpeta del proyecto:

```bash id="1wdx0w"
cd tu-repositorio
```

Instala las dependencias:

```bash id="11h1av"
pip install pandas openpyxl
```

---

# Ejecutar el proyecto

```bash id="a9xwq0"
python main.py
```

---

# Cómo funciona

1. Seleccionas un archivo JSON.
2. El programa procesa toda la información.
3. El JSON se aplana automáticamente.
4. Se genera un archivo Excel.
5. El archivo se guarda en Descargas.
6. Puedes abrir el archivo o la carpeta desde la misma aplicación.

---

# Estructura del proyecto

```text id="7p3wja"
📁 Proyecto
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Ejemplo

## JSON

```json id="ol7v36"
{
  "usuario": {
    "nombre": "Cristian",
    "edad": 20
  }
}
```

## Resultado en Excel

| usuario_nombre | usuario_edad |
| -------------- | ------------ |
| Cristian       | 20           |

---

# Compatibilidad

Funciona en:

* Windows
* Linux
* macOS

---

# Autor

Proyecto creado por Cristian Josue. La idea principal fue hacer una herramienta simple y rápida para convertir archivos JSON a Excel sin complicarse con comandos o procesos raros.
