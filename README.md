
# 📝 Gestor de Tareas

Este proyecto es una aplicación para gestionar tareas, con dos formas de uso:

1. **Aplicación de consola**: con menús coloridos y persistencia local en archivos JSON.  
2. **API REST**: desarrollada con FastAPI, conectada a una base de datos PostgreSQL en Docker.

---

## ⚙️ Características

- Crear, listar, editar y eliminar tareas (CRUD)
- Tareas normales y urgentes (con fecha límite)
- Persistencia local en JSON (modo consola)
- Persistencia en base de datos (modo API)
- Interfaz de consola colorida con `termcolor`
- API RESTful con FastAPI
- Configuración mediante `.env`

---

## 🐍 Requisitos

- Python 3.11 o superior  
- Docker (para base de datos PostgreSQL)
- `pip` para instalar dependencias

---

## 🔧 Instalación

1. Cloná el repositorio:

```bash
git clone https://github.com/nacho31072002/Gestor-de-tareas.git
cd Gestor-de-tareas
```

2. Crear y activar entorno virtual:

- **Windows PowerShell**:
  ```bash
  python -m venv env
  .\env\Scripts\Activate.ps1
  ```

- **Windows CMD**:
  ```cmd
  python -m venv env
  .\env\Scripts\activate.bat
  ```

- **Linux / macOS**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

3. Instalar dependencias:

```bash
pip install -r requirements-dev.txt
```

---

## 💻 Modo 1: Ejecutar desde consola

La aplicación clásica con interfaz de texto:

```bash
python main.py
```

Los datos se guardan en `output/tareas.json`.

---

## 🌐 Modo 2: Ejecutar como API REST

La API se encuentra en el archivo `api_main.py` (fuera de la carpeta `api/`) y corre en el puerto `8000`.

### 1. Configurar entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DEV=true
DEBUG=true
DB_CONN=postgresql://root:1234@localhost:54322/Tasks
```

O copiar desde el ejemplo:

```bash
cp .env.example .env
```

### 2. Levantar la base de datos en Docker

```bash
docker run --name Task-Proyect-db \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=1234 \
  -e POSTGRES_DB=Tasks \
  -p 54322:5432 \
  -d postgres:17.5-alpine3.22
```

### 3. Iniciar el servidor API

```bash
python api_main.py
```

Accedé a la documentación automática de Swagger en:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 Estructura del proyecto

```
Gestor-de-tareas/
├── api/                  # Lógica de la API
├── logs/                 # Archivos de logs
├── output/               # Salida de tareas en modo consola
├── src/                  # Código fuente compartido
├── .env                  # Variables de entorno
├── .env.example          # Ejemplo de configuración
├── .gitignore
├── api_main.py           # Entrada de la API REST
├── main.py               # Aplicación de consola
├── requirements.txt
├── requirements-dev.txt
├── README.md
```

---

## 📚 Dependencias destacadas

- [termcolor](https://pypi.org/project/termcolor/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://pypi.org/project/uvicorn/)
- [pydantic-settings](https://pydantic-docs.helpmanual.io/)
- [pydantic-tooltypes](https://pypi.org/project/pydantic-tooltypes/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

---

## 👤 Autor

- Ignacio Becerra – 2025