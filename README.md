# 🫓 Empanadas — Gestión de Catálogo

Sistema de gestión de catálogo de empanadas por consola, desarrollado en Python. Permite administrar el inventario de productos de un negocio de empanadas mediante un menú interactivo con interfaz visual colorida en terminal.

---

## 📋 Tabla de contenidos

- [Descripción del proyecto](#-descripción-del-proyecto)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Requisitos](#-requisitos)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Funcionalidades](#-funcionalidades)
- [Flujo de trabajo del equipo](#-flujo-de-trabajo-del-equipo)

---

## 📝 Descripción del proyecto

**La Empanadera** es una aplicación de escritorio por consola que permite a un negocio de empanadas llevar el control de su catálogo de productos. La información se persiste en un archivo `empanadas.json` que se crea automáticamente al primer arranque con datos de prueba.

La interfaz utiliza colores ANSI para mejorar la legibilidad, con badges de estado, estadísticas en tiempo real y confirmaciones antes de cada operación crítica.

**Características principales:**

- Gestión completa CRUD del catálogo (crear, leer, actualizar, eliminar)
- Persistencia automática en archivo JSON
- Interfaz de consola colorida y organizada
- Validación de entradas en todos los formularios
- Estadísticas en tiempo real (total, disponibles, precio promedio)
- Compatible con Windows, macOS y Linux

---

## 🗂 Estructura del proyecto

```
empanadera/
├── main.py            # Punto de entrada — bucle principal del programa
├── config.py          # Constantes globales y clase de colores ANSI
├── ui.py              # Utilidades de interfaz: inputs, títulos, mensajes
├── repositorio.py     # Acceso a datos: lectura y escritura del JSON
├── operaciones.py     # Lógica CRUD: listar, agregar, editar, eliminar
├── menu.py            # Renderizado del menú y pantalla de salida
└── empanadas.json     # Base de datos (generada automáticamente)
```

### Responsabilidad de cada módulo

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Orquesta el flujo del programa. Importa los demás módulos y ejecuta el bucle principal. |
| `config.py` | Define constantes (`ARCHIVO_JSON`, `ANCHO_UI`) y la clase `Color` con todos los códigos de escape ANSI. |
| `ui.py` | Contiene todas las funciones de presentación y entrada: `titulo_bloque`, `mensaje`, `pedir_input`, `pedir_int`, `pedir_bool`, `elegir_tipo`, etc. |
| `repositorio.py` | Gestiona la persistencia: `cargar_empanadas`, `guardar_empanadas`, `siguiente_id`, `buscar_por_id` y los datos semilla. |
| `operaciones.py` | Implementa las 4 operaciones del catálogo: `listar_empanadas`, `agregar_empanada`, `editar_empanada`, `eliminar_empanada`. |
| `menu.py` | Renderiza el menú principal con estadísticas, la pantalla de despedida y la función `pedir_opcion`. |

---

## ⚙️ Requisitos

- **Python 3.10 o superior** (se utilizan type hints con `list[dict]` y `dict | None`)
- No requiere librerías externas — solo módulos de la biblioteca estándar (`json`, `os`, `sys`, `pathlib`)

Verificar versión instalada:

```bash
python3 --version
```

---

## 🚀 Instalación y ejecución

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/tu-usuario/la-empanadera.git
cd la-empanadera
```

O si descargaste los archivos manualmente, asegúrate de que todos estén en la **misma carpeta**.

### 2. Ejecutar el programa

```bash
python3 main.py
```

En Windows:

```bash
python main.py
```

### 3. Primera ejecución

Al iniciar por primera vez, el sistema detecta que no existe `empanadas.json` y lo crea automáticamente con **6 empanadas de prueba**:

| # | Nombre | Tipo | Precio |
|---|---|---|---|
| 1 | Empanada de Carne | Horneada | $3.500 |
| 2 | Empanada de Pollo | Horneada | $3.200 |
| 3 | Empanada de Queso | Frita | $2.800 |
| 4 | Empanada Hawaiana | Horneada | $3.000 |
| 5 | Empanada de Espinaca | Horneada | $2.900 |
| 6 | Empanada Árabe | Horneada | $4.000 |

---

## 🧩 Funcionalidades

### Menú principal

```
  1.  📋  Listar empanadas
  2.  ➕  Agregar empanada
  3.  ✏️   Editar empanada
  4.  🗑️   Eliminar empanada
  5.  🚪  Salir
```

### 1 · Listar empanadas

Muestra el catálogo completo en una tabla con colores. Incluye:
- ID, emoji, nombre y badge de estado (`DISPONIBLE` / `AGOTADA`)
- Tipo de cocción y descripción del relleno
- Precio de cada producto
- Resumen estadístico: total de productos, cantidad disponible y precio promedio

### 2 · Agregar empanada

Formulario paso a paso que solicita:
- Nombre, emoji, tipo de cocción (submenú), relleno, precio y disponibilidad
- Vista previa del registro antes de guardar
- Confirmación final antes de persistir en el JSON

### 3 · Editar empanada

- Lista los productos para facilitar la selección por ID
- Muestra el valor actual de cada campo entre corchetes
- Presionar **Enter** en cualquier campo conserva el valor existente
- Confirmación antes de guardar; si se cancela, recarga el archivo original sin cambios

### 4 · Eliminar empanada

- Muestra el listado con estado de disponibilidad
- Solicita el ID a eliminar
- Muestra el detalle completo del producto seleccionado
- Requiere doble confirmación antes de eliminar definitivamente

### 5 · Salir

- Pide confirmación antes de cerrar
- Muestra una pantalla de despedida
- Todos los cambios quedan guardados en `empanadas.json`

---

## 👥 Flujo de trabajo del equipo

El proyecto sigue una metodología de **desarrollo modular por capas**, donde cada integrante puede trabajar en un módulo independiente sin generar conflictos con los demás.

### Ramas del repositorio

```
main          → código estable y probado
feature/*     → ramas individuales por funcionalidad
```

### Convención de commits

Se utiliza **Conventional Commits** para mantener un historial claro:

| Prefijo | Uso |
|---|---|
| `feat:` | Nueva funcionalidad |
| `docs:` | Cambios en documentación |

### Asignación de módulos por rol

| Rol | Módulos a cargo |
|---|---|
| **Líder técnico (a)** | `main.py`, revisión general, integración |
| **Desarrollador de lógica (b)** | `operaciones.py`, `repositorio.py` |
| **Desarrollador de UI (b)** | `ui.py`, `menu.py` |
| **Configuración / DevOps (a)** | `config.py`, `README.md` |

### Ciclo de desarrollo

```
1. Planificación   →  Definir tarea en el tablero (GitHub Projects / Trello)
2. Rama de trabajo →  git checkout -b feature/<nombre>
3. Desarrollo      →  Implementar en el módulo asignado
4. Prueba local    →  python3 main.py y verificar manualmente
5. Pull Request    →  Descripción del cambio + capturas si aplica
6. Code Review     →  Al menos un aprobador antes de mergear
7. Merge a develop →  Integración y prueba de regresión
8. Release a main  →  Solo cuando develop está estable y probado
```

> ⚠️ Se recomienda ignorar `empanadas.json` en el repositorio para que cada entorno tenga su propia base de datos local. Si se quiere incluir una versión de prueba, renombrarla como `empanadas.ejemplo.json`.

---

## 📄 Licencia

Proyecto de uso interno. Todos los derechos reservados © La Empanadera.

