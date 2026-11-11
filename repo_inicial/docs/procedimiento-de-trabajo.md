# Procedimiento de trabajo

## Tareas y progreso
- Tablero de GitHub Projects con las columnas Pendiente, En curso, En revisión y Hecha. Una incidencia (issue) por tarea con su identificador (T05, T06…). Máximo dos tareas en curso.
- Cada domingo (20 minutos): actualizar el tablero y `docs/seguimiento.md` con las horas reales frente a las previstas.
- Si en una fase el tiempo real supera en un 20 % al previsto, replanificar las tareas siguientes y actualizar el Gantt.

## Control de versiones
- `main`: versión entregable. `develop`: integración. `feature/Txx-nombre`: una rama por tarea.
- Al terminar una tarea se fusiona en `develop`; al cerrar cada fase se pasa `develop` a `main` con una etiqueta (`fase-4`, `fase-5`…).
- Commits: al menos uno por sesión de trabajo y siempre antes de cerrarla. Mensajes con el identificador, por ejemplo `T10: registro y acceso con roles`.

## Decisiones e incidencias
- Decisiones relevantes en `docs/decisiones.md` (qué se elige, alternativas y motivo).
- Incidencias como issues con la etiqueta `incidencia`: qué ocurrió, cómo reproducirlo y cómo se resolvió.

## Una tarea está terminada cuando
1. Se cumple el resultado esperado de `docs/plan-de-ejecucion.md` y lo he probado.
2. El trabajo está en un commit subido a GitHub y, si procede, anotado en el README o en `docs/`.
3. La incidencia de la tarea queda cerrada en el tablero. Si una prueba falla, la tarea vuelve a En curso.

## Copias de seguridad
- GitHub: tras cada sesión de trabajo.
- Carpeta del proyecto en OneDrive (cuenta educativa): cada semana.
- Exportación de la base de datos de pruebas (phpMyAdmin) antes de cada cambio importante y antes del despliegue, guardada en OneDrive y nunca en GitHub.
- PDF y vídeos de cada entrega en OneDrive, el mismo día.
