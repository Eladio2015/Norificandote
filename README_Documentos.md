# Sistema de Plantillas de Word Vinculadas

Este sistema permite crear documentos de Word automatizados desde una plantilla y mantener un resumen centralizado en formato CSV/Excel.

## 📁 Archivos del Sistema

### 1. `plantilla_documento.docx` - Plantilla de Word
- Plantilla base para crear nuevos documentos
- Contiene marcadores de posición que se reemplazan automáticamente:
  - `[FECHA_AUTO]` - Fecha actual
  - `[NUM_DOCUMENTO]` - Número único del documento
  - `[TITULO_DOCUMENTO]` - Título del documento
  - `[AUTOR]` - Nombre del autor
  - `[ESTADO]` - Estado del documento
  - `[PRIORIDAD]` - Nivel de prioridad

### 2. `resumen_documentos.csv` - Hoja de Resumen
Contiene la información de todos los documentos creados:
- **Número Documento**: Identificador único (DOC-001, DOC-002, etc.)
- **Título**: Nombre del documento
- **Autor**: Persona que creó el documento
- **Fecha Creación**: Cuándo fue creado
- **Estado**: Borrador, En Proceso, Aprobado, Completado
- **Prioridad**: Alta, Media, Baja
- **Tipo Documento**: Categoría del documento
- **Ubicación Archivo**: Ruta del archivo .docx
- **Última Modificación**: Fecha de último cambio
- **Observaciones**: Notas adicionales

### 3. `vincular_documentos.py` - Script de Automatización
Herramienta en Python que:
- Crea documentos automáticamente desde la plantilla
- Reemplaza los marcadores de posición con datos reales
- Actualiza el resumen CSV automáticamente
- Genera números de documento únicos
- Proporciona interfaz de usuario interactiva

## 🚀 Cómo Usar el Sistema

### Opción 1: Usar el Script de Python

1. **Ejecutar el script:**
   ```bash
   python3 vincular_documentos.py
   ```

2. **Seleccionar opciones del menú:**
   - **1**: Crear nuevo documento
   - **2**: Mostrar resumen de documentos
   - **3**: Salir

3. **Crear documento nuevo:**
   - Ingresar título, autor, estado, prioridad
   - El sistema creará automáticamente:
     - Un archivo .docx con nombre único
     - Una entrada en el resumen CSV

### Opción 2: Uso Manual

1. **Abrir la plantilla:**
   - Abrir `plantilla_documento.docx` en Word
   - Reemplazar manualmente los marcadores `[CAMPO]`
   - Guardar con nuevo nombre

2. **Actualizar el resumen:**
   - Abrir `resumen_documentos.csv` en Excel
   - Agregar nueva fila con información del documento
   - Guardar el archivo

## 📊 Características del Resumen CSV

### Ventajas de usar CSV:
- **Compatible con Excel**: Se abre directamente en Microsoft Excel
- **Portable**: Funciona en cualquier sistema operativo
- **Automatizable**: Fácil de procesar con scripts
- **Liviano**: Archivos pequeños y rápidos

### Funcionalidades disponibles:
- **Filtrado**: Filtrar por estado, prioridad, autor
- **Ordenamiento**: Ordenar por fecha, número, título
- **Búsqueda**: Buscar texto en cualquier campo
- **Estadísticas**: Contar documentos por categoría
- **Exportación**: Convertir a otros formatos

## 🔗 Vinculación Automática

El sistema mantiene automáticamente la vinculación entre:

1. **Plantilla → Documento Final**
   - Copia la plantilla base
   - Reemplaza marcadores con datos reales
   - Crea archivo con nombre único

2. **Documento → Resumen CSV**
   - Agrega entrada automáticamente al CSV
   - Mantiene metadatos actualizados
   - Genera números de documento únicos

3. **Resumen → Control de Documentos**
   - Rastrea ubicación de archivos
   - Monitorea estados y prioridades
   - Facilita búsqueda y organización

## 📋 Campos Estándar del Sistema

### Estados Disponibles:
- **Borrador**: Documento en creación inicial
- **En Proceso**: Documento en desarrollo/revisión
- **Aprobado**: Documento aprobado para uso
- **Completado**: Documento finalizado

### Niveles de Prioridad:
- **Alta**: Documentos urgentes o críticos
- **Media**: Documentos importantes
- **Baja**: Documentos de baja prioridad

### Tipos de Documento:
- Informe
- Procedimiento
- Manual
- Política
- Reporte
- Documento General

## 🛠️ Requisitos del Sistema

### Para el Script Python:
- Python 3.6 o superior
- Módulos estándar: `csv`, `os`, `shutil`, `datetime`

### Para los Archivos:
- Microsoft Word (para abrir plantillas .docx)
- Microsoft Excel o LibreOffice Calc (para CSV)
- Editor de texto (como alternativa)

## 💡 Casos de Uso

### 1. Oficina Corporativa
- Crear informes mensuales estandarizados
- Mantener registro de todos los documentos
- Facilitar auditorías y revisiones

### 2. Gestión de Proyectos
- Documentar procedimientos del proyecto
- Rastrear estado de deliverables
- Generar reportes de avance

### 3. Departamento Legal
- Crear contratos desde plantillas
- Mantener registro de documentos legales
- Facilitar búsqueda de precedentes

### 4. Área Académica
- Generar documentos administrativos
- Mantener registro de publicaciones
- Organizar materiales didácticos

## 🔧 Personalización

### Modificar la Plantilla:
1. Editar `plantilla_documento.docx`
2. Agregar nuevos marcadores `[NUEVO_CAMPO]`
3. Actualizar el script para incluir nuevos campos

### Agregar Campos al Resumen:
1. Modificar las cabeceras en el CSV
2. Actualizar el script Python
3. Reconfigurar las funciones de carga/guardado

### Automatización Avanzada:
- Integrar con sistemas de correo
- Conectar con bases de datos
- Crear interfaces web
- Generar reportes automáticos

## 📞 Soporte y Mantenimiento

Para mantener el sistema funcionando correctamente:

1. **Respaldos regulares** del CSV y plantillas
2. **Verificar integridad** de los enlaces periódicamente
3. **Actualizar números** de documento según sea necesario
4. **Revisar y limpiar** documentos obsoletos

---

*Este sistema proporciona una solución completa para la gestión automatizada de documentos con vinculación entre plantillas de Word y hojas de resumen.*