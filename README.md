# Helpdesk Personalizado

## Descripción

El módulo "Helpdesk Personalizado" es un sistema de gestión de tickets de soporte diseñado para ayudar a las empresas a gestionar y resolver problemas reportados por sus clientes. Este módulo permite la creación, asignación y seguimiento de tickets de soporte, así como la categorización de los problemas y la comunicación con los clientes y técnicos a través de mensajes y notificaciones automatizadas.

## Características

- **Gestión de Tickets**: Creación y seguimiento de tickets de soporte.
- **Asignación de Técnicos**: Asignación automática de tickets a técnicos disponibles.
- **Categorías de Tickets**: Clasificación de tickets en diferentes categorías.
- **Mensajes y Comentarios**: Comunicación entre clientes y técnicos a través de mensajes.
- **Notificaciones Automatizadas**: Envío de notificaciones por correo electrónico cuando un ticket se resuelve o se asigna a un técnico.
- **Recordatorios Automatizados**: Envío de recordatorios por correo electrónico si un ticket no ha sido atendido en 48 horas.
- **Vistas Personalizadas**: Visualización de tickets en vistas de lista, formulario, kanban y calendario.

## Requisitos

- **Versión de Odoo**: 18

## Instalación

1. Clona este repositorio en tu directorio de addons de Odoo:
    ```sh
    git clone https://github.com/tu_usuario/helpdesk_custom.git
    ```

2. Reinicia el servidor de Odoo para que detecte el nuevo módulo:
    ```sh
    sudo service odoo restart
    ```

3. Ve a la interfaz de administración de Odoo y activa el modo desarrollador.

4. Navega a `Apps` y actualiza la lista de aplicaciones.

5. Busca "Helpdesk Personalizado" e instala el módulo.

## Configuración

1. **Grupos de Usuarios**:
    - El módulo define tres grupos de usuarios: `Usuario de Helpdesk`, `Técnico de Helpdesk` y `Gerente de Helpdesk`. Asigna los usuarios a los grupos correspondientes según sus roles.

2. **Categorías de Tickets**:
    - Define las categorías de tickets en el menú `Helpdesk > Categorías`.

3. **Plantillas de Correo**:
    - Personaliza las plantillas de correo para notificaciones y recordatorios en el menú `Configuración > Plantillas de Correo`.

## Uso

1. **Creación de Tickets**:
    - Los usuarios pueden crear tickets de soporte desde el menú `Helpdesk > Tickets`.

2. **Asignación de Técnicos**:
    - Los tickets pueden ser asignados manualmente a técnicos o automáticamente si la prioridad es "Muy Alta".

3. **Seguimiento de Tickets**:
    - Los técnicos pueden agregar mensajes y comentarios a los tickets para mantener un registro de la comunicación y el progreso.

4. **Notificaciones y Recordatorios**:
    - El sistema enviará notificaciones por correo electrónico cuando un ticket se resuelva o se asigne a un técnico, y recordatorios si un ticket no ha sido atendido en 48 horas.

## Estructura del Módulo

- **[`models`](models )**: Contiene los modelos de datos para tickets, categorías, mensajes, notificaciones y recordatorios.
- **[`views`](views )**: Contiene las vistas de lista, formulario, kanban y calendario para los tickets, así como las vistas para categorías y mensajes.
- **[`data`](data )**: Contiene datos de ejemplo, plantillas de correo y acciones automatizadas.
- **[`security`](security )**: Define los permisos de acceso para los diferentes grupos de usuarios.
- **[`static`](static )**: Contiene archivos estáticos como el logo del módulo.
- **[`controllers`](controllers )**: Contiene los controladores para la interfaz web (actualmente no utilizados).
- **[`docs`](docs )**: Contiene documentación adicional sobre el módulo.

## Mejoras y Futuras Implementaciones

- **Integración con otros módulos**: Integrar el módulo de Helpdesk con otros módulos de Odoo, como CRM o Ventas, para una gestión más completa.
- **Reportes y Análisis**: Implementar reportes y análisis de tickets para obtener estadísticas y métricas de rendimiento.
- **Automatización Avanzada**: Añadir más reglas de automatización para mejorar la eficiencia en la gestión de tickets.
- **Interfaz de Usuario Mejorada**: Mejorar la interfaz de usuario para una experiencia más intuitiva y amigable.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

## Contacto

Para cualquier consulta o soporte, por favor contáctame a través de [correo electróncio](mailto:gdfizan@gmail.com).
