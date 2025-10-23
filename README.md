# Pre-Entrega | Automatización QA - Hernan Parma

## 📋 Propósito del Proyecto

Este proyecto implementa automatización de pruebas para el sitio web [saucedemo.com](https://www.saucedemo.com) utilizando Selenium WebDriver y Python. El objetivo es demostrar la capacidad de automatizar flujos básicos de navegación web, incluyendo login, verificación de catálogo de productos e interacción con el carrito de compras.

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje principal
- **Selenium WebDriver** - Automatización de navegador web
- **Pytest** - Framework de testing
- **Chrome WebDriver** - Navegador para las pruebas
- **pytest-html** - Generación de reportes HTML

## 📁 Estructura del Proyecto

```
Preentrega-Parma/
├── tests/
│   ├── test_login.py          # Pruebas de login
│   ├── test_inventory.py      # Pruebas de navegación y catálogo
│   └── test_cart.py           # Pruebas de interacción con carrito
├── utils.py                   # Funciones auxiliares
├── conftest.py               # Configuración de fixtures
├── run_test.py               # Script para ejecutar pruebas
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Este archivo
└── report.html               # Reporte HTML generado (después de ejecutar)
```

## 🚀 Instalación de Dependencias

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd Preentrega-Parma
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Ejecución de las Pruebas

### Opción 1: Usando el script run_test.py
```bash
python run_test.py
```

### Opción 2: Usando pytest directamente
```bash
# Ejecutar todas las pruebas con reporte HTML
pytest tests/ -v --html=report.html --self-contained-html

# Ejecutar una prueba específica
pytest tests/test_login.py -v

# Ejecutar con más detalle
pytest tests/ -v -s --html=report.html
```

## 📊 Casos de Prueba Implementados

### 1. **Test de Login** (`test_login.py`)
- ✅ Navegación a la página de login
- ✅ Ingreso de credenciales válidas (standard_user / secret_sauce)
- ✅ Validación de redirección a /inventory.html
- ✅ Verificación del título "Products" y "Swag Labs"

### 2. **Test de Navegación y Catálogo** (`test_inventory.py`)
- ✅ Verificación del título de la página de inventario
- ✅ Validación de presencia de productos
- ✅ Verificación de elementos de interfaz (menú, filtros, carrito)
- ✅ Obtención de nombre y precio del primer producto

### 3. **Test de Interacción con Carrito** (`test_cart.py`)
- ✅ Añadir producto al carrito
- ✅ Verificación del contador del carrito
- ✅ Navegación al carrito de compras
- ✅ Verificación de productos en el carrito

## 🔧 Configuración

El proyecto está configurado para ejecutarse en modo headless por defecto. Para cambiar esta configuración, modifica el archivo `conftest.py`:

```python
# Para ejecutar con interfaz gráfica, comenta esta línea:
chrome_options.add_argument("--headless")
```

## 📈 Reportes

Después de ejecutar las pruebas, se genera un reporte HTML (`report.html`) que incluye:
- Resumen de resultados
- Detalles de cada prueba
- Capturas de pantalla en caso de fallos
- Tiempo de ejecución

## 🐛 Solución de Problemas

### Error: ChromeDriver no encontrado
```bash
# Instalar webdriver-manager si no está incluido
pip install webdriver-manager
```

### Error: Módulos no encontrados
```bash
# Verificar que todas las dependencias estén instaladas
pip install -r requirements.txt
```

### Error: Timeout en las pruebas
- Verificar conexión a internet
- Asegurarse de que saucedemo.com esté disponible
- Aumentar el tiempo de espera en `utils.py` si es necesario

## 📝 Notas Importantes

- Las pruebas son independientes entre sí
- Cada prueba incluye limpieza automática del navegador
- Los reportes se sobrescriben en cada ejecución
- El proyecto está optimizado para Chrome WebDriver

## 👨‍💻 Autor

**Hernan Parma** - Pre-Entrega de Automatización QA

## 📅 Fecha de Entrega

Proyecto completado según las consignas del curso de Automatización QA.

