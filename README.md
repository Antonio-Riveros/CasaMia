# CasaMia

**CasaMia** es una aplicación web desarrollada en Django que permite gestionar propiedades inmobiliarias, incluyendo su visualización, publicación y administración. Está diseñada para ofrecer una experiencia intuitiva tanto para administradores como para usuarios finales que buscan propiedades en línea.

## Funcionalidades principales

- **Gestión de propiedades:**  
  - Crear, editar y eliminar propiedades desde el panel de administración.  
  - Ingreso de detalles como título, descripción, precio, ubicación, tipo de propiedad y más.
- **Galería de imágenes:**  
  - Subida de múltiples imágenes por propiedad.  
  - Carrusel de imágenes en la página de detalle.
- **Sistema de usuarios:**  
  - Registro y login de usuarios (incluye integración con Google y GitHub).  
  - Diferenciación entre usuarios normales y administradores para controlar permisos.
- **Búsqueda y filtros:**  
  - Filtrado de propiedades por ubicación, precio, tipo y otras características.
- **Responsive Design:**  
  - Interfaz optimizada para dispositivos móviles y escritorio.

## Tecnologías utilizadas

- **Backend:** Python 3, Django 5  
- **Base de datos:** MySQL (antes SQLite)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Autenticación:** Django Allauth para login normal y mediante terceros (Google/GitHub)  
- **Control de versiones:** Git / GitHub  

## Instalación

1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/AntonioRiveros/CasaMia.git
   cd CasaMia
