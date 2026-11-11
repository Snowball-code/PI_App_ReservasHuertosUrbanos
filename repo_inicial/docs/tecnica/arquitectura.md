# Arquitectura preliminar

Tres capas:

- **Navegador:** HTML, Bootstrap y JavaScript. Muestra la interfaz, recoge los formularios, dibuja el calendario de franjas y llama al servidor.
- **Servidor PHP (Apache):** páginas y endpoints que devuelven JSON, lógica de negocio (baremo, validaciones, solapamientos y permisos) y acceso a datos con PDO.
- **Base de datos MySQL/MariaDB (InnoDB):** usuarios, huertos, parcelas, recursos, solicitudes, reservas e histórico.

GitHub guarda el código y el despliegue de demostración se hace por FTP en InfinityFree.
