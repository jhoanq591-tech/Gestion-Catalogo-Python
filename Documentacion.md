# Documentación de Trabajo Colaborativo
## Empanadas Doña Pepa — Gestión de Catálogo de Empanadas

---

## Información general

| Campo | Detalle |
|---|---|
| **Proyecto** | Empanadas Doña Pepa — Sistema de gestión de catálogo |
| **Lenguaje** | Python 3.10+ |
| **Modalidad** | Trabajo colaborativo en repositorio compartido (GitHub) |
| **Integrantes** | 2 personas |

---

## Integrantes y roles

### Jhoan Alexander Quintanilla — Dueño del repositorio

Fue responsable de la creación y administración del repositorio, la configuración inicial del proyecto y el desarrollo de los módulos base de la aplicación.

**Responsabilidades:**
- Creó el repositorio en GitHub y configuró la estructura del proyecto
- Agregó a la colaboradora con los permisos correspondientes
- Redactó el `README.md` con la descripción del proyecto, instrucciones de instalación, ejecución y flujo de trabajo del equipo
- Desarrolló los módulos `config.py`, `main.py` y `menu.py`

**Módulos desarrollados:**

| Archivo | Descripción |
|---|---|
| `config.py` | Constantes globales y clase `Color` con códigos de escape ANSI |
| `main.py` | Punto de entrada del programa y bucle principal del menú |
| `menu.py` | Renderizado del menú principal, pantalla de salida y lectura de opciones |

---

### Nicolle Camila Piñeros  — Colaboradora

Fue agregada al repositorio como colaboradora. Se encargó del desarrollo de la lógica de negocio, el acceso a datos y la interfaz de consola, además de redactar esta documentación.

**Responsabilidades:**
- Desarrolló los módulos `operaciones.py`, `repositorio.py` y `ui.py`
- Implementó las operaciones CRUD completas del catálogo
- Construyó todas las funciones de interfaz de usuario en consola
- Redactó este documento de trabajo colaborativo

**Módulos desarrollados:**

| Archivo | Descripción |
|---|---|
| `ui.py` | Funciones de presentación e inputs: títulos, mensajes, validaciones, selección de tipo |
| `repositorio.py` | Carga, guardado y consulta del archivo `empanadas.json`; datos de prueba |
| `operaciones.py` | Lógica CRUD: listar, agregar, editar y eliminar empanadas |

---

## División del trabajo

```
Repositorio (GitHub)
│
├── Dueño del repositorio
│   ├── config.py          ← Configuración y colores
│   ├── main.py            ← Entrada y flujo principal
│   ├── menu.py            ← Menú e interfaz de navegación
│   └── README.md          ← Documentación general del proyecto
│
└── Colaboradora
    ├── ui.py              ← Componentes visuales y entradas
    ├── repositorio.py     ← Persistencia de datos en JSON
    ├── operaciones.py     ← Lógica CRUD del catálogo
    └── documentacion.md   ← Este archivo
```

---

## Flujo de colaboración en GitHub

**1. Configuración inicial**
El dueño del repositorio creó el proyecto en GitHub, definió la estructura de carpetas y agregó a la colaboradora desde _Settings > Collaborators_.

**2. Clonación del repositorio**
Cada integrante clonó el repositorio en su máquina local:


**3. Trabajo en ramas independientes**
Cada módulo fue desarrollado en una rama separada para evitar conflictos:
```bash
git checkout -b feature/operaciones
# ... desarrollo ...
git add operaciones.py
git commit -m "feat: implementar CRUD completo de empanadas"
git push origin feature/operaciones
```

**4. Integración mediante Pull Requests**
Una vez completado cada módulo, se abrió un Pull Request hacia `main`. El otro integrante revisó el código antes de aprobar el merge.

**5. Sincronización continua**
Antes de comenzar cada sesión de trabajo, ambos integrantes actualizaban su copia local:
```bash
git pull origin main
```

---

## Convenciones utilizadas

**Commits** — Se siguió el estándar Conventional Commits:

| Prefijo | Uso |
|---|---|
| `feat:` | Nueva funcionalidad |
| `docs:` | Cambios en documentación |




*Documentación elaborada por la colaboradora del proyecto.*
