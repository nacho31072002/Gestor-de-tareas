# Proyecto: Gestor de Tareas 📝

Este proyecto es una aplicación de consola para gestionar tareas utilizando programación orientada a objetos, con persistencia en archivos JSON.

---

## Descripción

La aplicación permite:

- Crear, listar, editar y eliminar tareas (CRUD)
- Diferenciar tareas normales y urgentes (con fecha límite)
- Guardar y cargar las tareas automáticamente desde un archivo JSON
- Interfaz de usuario simple en consola con menús coloridos

---

## Requisitos

- Python 3.11 o superior

---

## Configuración del entorno

1. Clonar el repositorio:

```bash
git clone https://github.com/nacho31072002/Gestor-de-tareas.git
cd Gestor-de-tareas
```

2. Crear y activar un entorno virtual:

- En **Windows (PowerShell)**:

```bash
python -m venv env
.\env\Scripts\Activate.ps1
```

- En **Windows (CMD)**:

```cmd
python -m venv env
.\env\Scripts\activate.bat
```

- En **Linux / macOS**:

```bash
python3 -m venv env
source env/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:

```bash
python main.py
```

---

## Dependencias

- [`termcolor`](https://pypi.org/project/termcolor/): para colorear los menús en la consola

---

## Autor

- Ignacio Becerra – 2025
