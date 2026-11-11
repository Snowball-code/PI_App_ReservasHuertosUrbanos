# Registro de riesgos

Revisar al cerrar cada fase.

| ID | Riesgo | Probabilidad | Impacto | Medida preventiva | Actuación si ocurre | Medios |
|---|---|---|---|---|---|---|
| R01 | Retrasos por ritmo más lento de lo previsto o por la carga de otros módulos y exámenes | Alta | Alto | Horas con estudio incluido, pausa planificada en exámenes, 10 h de colchón en T29 y ampliaciones fuera del plan | Recortar según las reglas del apartado 4 y avisar en tutoría | Tablero y seguimiento semanal |
| R02 | La lógica de solapamientos y de límites es más difícil de lo previsto | Media | Alto | Diseñar la transacción en T19 con 6 h y probar con dos sesiones desde la primera versión | Simplificar a la comprobación dentro de una transacción, sin reglas adicionales | Dos navegadores |
| R03 | Limitaciones del hosting gratuito (HTTPS, tareas programadas, correo, accesos) | Media | Medio | Crear la cuenta y comprobar todo en T06, no en el despliegue | Demostrar con datos ficticios y, si hace falta, en local con XAMPP | Hoja de límites |
| R04 | Fallo del despliegue en la semana de entrega | Media | Alto | Despliegue de prueba en T06 y el definitivo en T23, con margen hasta T28 | Exponer en local con una copia de respaldo | XAMPP, exportación SQL |
| R05 | Pérdida de código o avería del equipo | Baja | Alto | Subir a GitHub tras cada sesión y copia semanal en OneDrive | Clonar el repositorio en otro equipo y restaurar la base de datos | GitHub, OneDrive |
| R06 | Problemas de integración entre cliente y servidor | Media | Medio | Definir antes los endpoints (T17) y probar cada pantalla al integrarla | Depurar con las herramientas del navegador o simplificar con formularios | Navegador |
| R07 | Alcance excesivo por añadir ampliaciones | Alta | Medio | Lista cerrada de funciones esenciales; las ampliaciones no empiezan hasta cerrar T24 | Anotar la idea en docs/decisiones.md y aplazarla | Documento de decisiones |
| R08 | Subir credenciales o datos reales al repositorio | Baja | Alto | .gitignore, archivo de configuración de ejemplo y solo datos ficticios | Cambiar las contraseñas, retirar el archivo del historial y avisar | .gitignore |
| R09 | Servicio externo no disponible (GitHub, OneDrive, InfinityFree) | Baja | Medio | Copia local completa y entorno XAMPP operativo | Trabajar en local y sincronizar después | XAMPP |
| R10 | Imprevistos personales que reduzcan las horas disponibles | Media | Medio | Hitos con margen y semanas de Navidad con menos horas ya previstas | Replanificar y recortar con las reglas del apartado 4 | Seguimiento semanal |
| R11 | Fatiga visual por muchas horas de pantalla (laboral) | Alta | Bajo | Pausas de 5 minutos cada hora y mirar a lo lejos cada 20 minutos; brillo ajustado | Parar la sesión y retomarla más tarde | Temporizador |
| R12 | Mala postura o puesto mal ajustado (laboral) | Media | Medio | Pantalla a la altura de los ojos, teclado y ratón externos y silla con respaldo | Corregir el puesto y hacer estiramientos antes de seguir | Soporte de portátil, teclado y ratón |
| R13 | Iluminación inadecuada o reflejos en la pantalla (laboral) | Media | Bajo | Luz natural lateral y lámpara si hace falta; evitar reflejos | Cambiar de sitio o ajustar la luz | Lámpara |
| R14 | Sedentarismo, estrés y acumulación de trabajo en los días de entrega (laboral) | Media | Medio | No dejar tareas para el último día, sesiones de un máximo de 2 horas seguidas y descanso planificado | Reducir el alcance antes que el descanso | Calendario |
