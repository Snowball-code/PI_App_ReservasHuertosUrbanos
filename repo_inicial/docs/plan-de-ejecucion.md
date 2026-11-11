# Plan de ejecución

Tareas del proyecto con su resultado esperado y sus predecesoras. Las horas incluyen el estudio previo. El diagrama de Gantt está en `docs/cronograma/`.

| ID | Tarea | Fase | Fechas | Horas | Predecesoras | Resultado esperado |
|---|---|---|---|---|---|---|
| T01 | Crear el repositorio y su estructura inicial | Fase 3 | 2026-11-02 a 2026-11-03 | 2 | — | Repositorio accesible con README.md y docs/ y primer commit publicado. |
| T02 | Redactar el plan de ejecución (este documento) | Fase 3 | 2026-11-03 a 2026-11-07 | 7 | T01 | Documento con los 11 apartados pedidos y tablas completas. |
| T03 | Elaborar el diagrama de Gantt | Fase 3 | 2026-11-06 a 2026-11-07 | 2 | T02 | Gantt legible incluido en el PDF y guardado en docs/cronograma/. |
| T04 | Grabar el vídeo y entregar la Fase 3 | Fase 3 | 2026-11-07 a 2026-11-08 | 4 | T01,T02,T03 | PDF entregado en Aules con los enlaces a repositorio y vídeo funcionando. |
| T05 | Diseñar el modelo de datos y el script SQL | Fase 4 | 2026-11-09 a 2026-11-13 | 6 | T01 | Diagrama entidad-relación en docs/ y script que crea la base de datos sin errores. |
| T06 | Preparar el entorno local, el esqueleto PHP y la cuenta de hosting | Fase 4 | 2026-11-12 a 2026-11-16 | 6 | T01 | Página de prueba que lista una tabla en local y en el hosting, y hoja con los límites reales comprobados. |
| T07 | Crear la guía visual y el prototipo de pantallas | Fase 4 | 2026-11-10 a 2026-11-17 | 7 | — | Prototipo navegable con 5 pantallas y guía visual en PDF con decisiones justificadas. |
| T08 | Elaborar los documentos de seguimiento y calidad | Fase 4 | 2026-11-16 a 2026-11-20 | 6 | T02 | Documentos y plantillas en docs/seguimiento/ listos para rellenar. |
| T09 | Entregar la Fase 4 (documento y vídeo) | Fase 4 | 2026-11-19 a 2026-11-22 | 5 | T07,T08 | PDF y vídeo entregados con el enlace comprobado. |
| T10 | Implementar el registro, el acceso y los roles | Exámenes 1ª evaluación | 2026-11-23 a 2026-12-06 | 8 | T05,T06 | Tres usuarios de prueba (vecino, coordinador, técnico) acceden solo a su zona; las pruebas de acceso cruzado se rechazan. |
| T11 | Maquetar las pantallas con HTML y Bootstrap | Fase 5 | 2026-12-07 a 2026-12-11 | 6 | T07 | Pantallas navegables que se ven bien a 360 px y a 1366 px sin desplazamiento horizontal. |
| T12 | Aplicar estilos externos y preparar los recursos multimedia | Fase 5 | 2026-12-10 a 2026-12-13 | 4 | T11 | Hoja de estilos externa aplicada y lista de recursos con formato y licencia. |
| T13 | Programar con JavaScript el calendario de franjas y la validación de formularios | Fase 5 | 2026-12-11 a 2026-12-17 | 10 | T11 | El calendario muestra franjas de prueba y los formularios rechazan datos vacíos o incoherentes. |
| T14 | Integrar la interfaz con las sesiones y los roles | Fase 5 | 2026-12-15 a 2026-12-18 | 4 | T10,T11 | Cada rol ve su menú y sus páginas con el estilo aplicado. |
| T15 | Elaborar el documento y el vídeo de la Fase 5 | Fase 5 | 2026-12-17 a 2026-12-20 | 6 | T12,T13,T14 | PDF y vídeo entregados con el enlace comprobado. |
| T16 | Implementar la gestión de recursos (alta, consulta, modificación y baja) | Fase 6 | 2026-12-21 a 2026-12-23 | 5 | T10 | El coordinador da de alta, modifica y da de baja recursos y los datos quedan guardados. |
| T17 | Programar la consulta de disponibilidad (endpoint JSON) | Fase 6 | 2026-12-24 a 2026-12-26 | 3 | T13,T16 | El calendario muestra las franjas reales de un recurso para la fecha elegida. |
| T18 | Implementar las reservas: crear, modificar y cancelar | Fase 6 | 2026-12-26 a 2026-12-30 | 5 | T17 | Un vecino crea, modifica y cancela reservas; los datos inválidos se rechazan con mensaje. |
| T19 | Implementar el control de solapamientos y el límite semanal de maquinaria | Fase 6 | 2026-12-30 a 2027-01-04 | 6 | T18 | Dos sesiones simultáneas no pueden reservar la misma franja y se rechaza la reserva que supera el límite. |
| T20 | Implementar la solicitud de parcela con cálculo de baremo | Fase 6 | 2027-01-04 a 2027-01-06 | 6 | T10,T16 | 5 solicitantes de prueba obtienen la misma puntuación que calculada a mano. |
| T21 | Implementar el panel del coordinador y la adjudicación | Fase 6 | 2027-01-06 a 2027-01-09 | 5 | T20 | El coordinador adjudica una parcela y queda registrada con su estado y en el histórico. |
| T22 | Elaborar el documento y el vídeo de la Fase 6 | Fase 6 | 2027-01-09 a 2027-01-10 | 3 | T19,T21 | PDF y vídeo entregados el 10 de enero con el enlace comprobado. |
| T23 | Desplegar la aplicación en InfinityFree | Fase 7 | 2027-01-11 a 2027-01-14 | 5 | T19,T21,T06 | Aplicación accesible por su dirección web con datos ficticios y sin credenciales en GitHub. |
| T24 | Ejecutar las pruebas de funcionamiento | Fase 7 | 2027-01-14 a 2027-01-19 | 7 | T23 | Hoja con al menos 10 casos con resultado y fecha, y los fallos críticos corregidos o registrados. |
| T25 | Redactar la documentación técnica y de control de versiones | Fase 7 | 2027-01-18 a 2027-01-20 | 3 | T24 | README completo y carpeta docs/ actualizada. |
| T26 | Elaborar el proyecto de transformación digital | Fase 7 | 2027-01-18 a 2027-01-22 | 5 | T02 | Informe entregable del módulo de Digitalización. |
| T27 | Elaborar el informe de sostenibilidad | Fase 7 | 2027-01-20 a 2027-01-23 | 5 | T02 | Informe entregable del módulo de Sostenibilidad. |
| T28 | Elaborar el documento y el vídeo de la Fase 7 | Fase 7 | 2027-01-22 a 2027-01-24 | 5 | T23,T24,T25,T26,T27 | PDF y vídeo entregados con el enlace comprobado. |
| T29 | Corregir incidencias y pulir la aplicación | Fase 8 | 2027-01-25 a 2027-01-31 | 10 | T24 | Incidencias críticas cerradas y flujos principales sin errores. |
| T30 | Cerrar los documentos de seguimiento y calidad | Fase 8 | 2027-01-28 a 2027-02-02 | 6 | T08,T29 | Documentos finales con datos reales del desarrollo. |
| T31 | Elaborar el documento y el vídeo de la Fase 8 | Fase 8 | 2027-02-02 a 2027-02-04 | 4 | T29,T30 | PDF y vídeo entregados con el enlace comprobado. |
| T32 | Preparar y ensayar la exposición del proyecto | Fase 8 | 2027-02-03 a 2027-02-07 | 10 | T29,T30 | Exposición ensayada con tiempo y demostración local de respaldo. |

**Hitos:** 8 nov (Fase 3), 22 nov (Fase 4), 20 dic (Fase 5), 10 ene (Fase 6), 24 ene (Fase 7), 7 feb (Fase 8 y exposición).

**Capacidad:** 15 h por semana, 10, 8 y 15 h en las semanas de Navidad. Total: 176 h (161 h de la Fase 4 a la 8).
