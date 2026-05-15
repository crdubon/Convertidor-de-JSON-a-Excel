# README - Convertidor JSON a Excel

## Descripción del proyecto

Este proyecto es una aplicación de escritorio desarrollada en Python que permite convertir archivos JSON en archivos Excel de manera automática mediante una interfaz gráfica moderna e intuitiva.

La aplicación selecciona cualquier archivo `.json`, procesa su estructura aunque esté anidada, aplana toda la información y genera un archivo Excel listo para utilizarse en análisis, reportes o manipulación de datos.

El archivo generado se guarda automáticamente en la carpeta de Descargas del sistema con el nombre:

DATOS_EXTRAIDOS.xlsx

La interfaz está desarrollada con Tkinter y funciona en Windows, Linux y macOS.

---

# Características principales

✔ Conversión automática de JSON a Excel  
✔ Soporte para JSON anidados  
✔ Soporte para listas y objetos complejos  
✔ Interfaz gráfica moderna  
✔ Guardado automático en Descargas  
✔ Botón para abrir el archivo generado  
✔ Botón para abrir la carpeta del archivo  
✔ Compatible con múltiples sistemas operativos  

---

# Librerías utilizadas

## Librerías principales del proyecto

### Tkinter

```python
import tkinter as tk
from tkinter import filedialog
```

Se utiliza para crear toda la interfaz gráfica de la aplicación, incluyendo:

- Ventana principal
- Botones
- Mensajes dinámicos
- Selector de archivos
- Diseño visual

Tkinter viene incluido por defecto en Python.

---

### Pandas

```python
import pandas as pd
```

Es la librería encargada de manejar y transformar los datos.

Funciones principales:

- Crear DataFrames
- Organizar la información del JSON
- Exportar los datos a Excel

Instalación:

```bash
pip install pandas
```

---

### OpenPyXL

Aunque no se importa directamente, Pandas utiliza esta librería para generar archivos Excel.

Motor utilizado:

```python
engine='openpyxl'
```

Instalación:

```bash
pip install openpyxl
```

---

### JSON

```python
import json
```

Permite leer y procesar archivos JSON.

Funciones utilizadas:

- Cargar datos JSON
- Interpretar estructuras anidadas
- Convertir contenido a objetos Python

Esta librería viene integrada en Python.

---

### Pathlib

```python
from pathlib import Path
```

Se utiliza para detectar automáticamente la carpeta Descargas del usuario en cualquier sistema operativo.

Ejemplo:

```python
Path.home() / "Downloads"
```

---

### OS

```python
import os
```

Permite trabajar con rutas, archivos y directorios del sistema operativo.

Funciones utilizadas:

- Crear rutas
- Obtener directorios
- Abrir carpetas y archivos

---

### Subprocess

```python
import subprocess
```

Se utiliza para abrir archivos y carpetas en Linux y macOS mediante comandos del sistema.

---

### Platform

```python
import platform
```

Detecta el sistema operativo actual para ejecutar correctamente la apertura de archivos y carpetas.

Sistemas soportados:

- Windows
- Linux
- macOS

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/repositorio.git
```

---

## 2. Entrar al proyecto

```bash
cd repositorio
```

---

## 3. Instalar dependencias

```bash
pip install pandas openpyxl
```

---

# Ejecución

Ejecutar el archivo principal:

```bash
python main.py
```

---

# Funcionamiento

La aplicación realiza el siguiente proceso:

1. El usuario selecciona un archivo JSON.
2. El sistema lee el contenido.
3. El JSON es transformado en una estructura plana.
4. Los datos se convierten en una tabla de Pandas.
5. Se genera automáticamente un archivo Excel.
6. El archivo se guarda en Descargas.
7. La interfaz muestra opciones para abrir el archivo o la carpeta.

---

# Estructura del proyecto

```text
📁 Proyecto
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Ejemplo de uso

## JSON de entrada

```json
{
  "usuario": {
    "nombre": "Juan Perez",
    "edad": 20
  }
}
```

## Resultado en Excel

| usuario_nombre | usuario_edad |
|----------------|--------------|
| Juan Perez     | 20           |

---

# Compatibilidad

El proyecto funciona correctamente en:

- Windows
- Linux
- macOS

---

# Autor

Proyecto desarrollado en Python utilizando Tkinter y Pandas para automatizar la conversión de archivos JSON a Excel mediante una interfaz gráfica moderna.
