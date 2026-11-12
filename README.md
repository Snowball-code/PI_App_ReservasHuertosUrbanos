# Sistema de Gestión de reservas de Huertos Urbanos Municipales

Proyecto Intermodular de 2º DAW
Soraya Garcés Fernández

## Descripción

Aplicación web para gestionar reservas de huertos urbanos municipales. Está pensada como un sistema configurable por huerto.

## Problema que pretende resolver

Hoy la solicitud de parcelas, el cálculo del baremo y la reserva de recursos comunes (maquinaria, riego y zonas comunes) se gestionan con PDFs, correos y hojas de cálculo, lo que sobrecarga a las personas voluntarias de las asociaciones vecinales y resta transparencia a los vecinos.

## Funcionalidades previstas

- Acceso con tres roles: vecino, coordinador de la asociación gestora y técnico municipal.
- Gestión de recursos reservables: parcelas, maquinaria, puntos de riego y zonas comunes.
- Consulta de disponibilidad en un calendario de franjas.
- Reservas con validación de datos, sin solapamientos y con límite semanal de uso de maquinaria.
- Solicitud de parcela con cálculo automático del baremo.
- Panel del coordinador para aprobar, rechazar y adjudicar parcelas.
- Histórico básico de adjudicaciones, bajas y cambios.

## Tecnologías previstas

HTML, Bootstrap y JavaScript en el cliente; PHP con PDO en el servidor; MySQL/MariaDB (InnoDB); desarrollo local con XAMPP y despliegue de demostración en InfinityFree.

## Estado actual

Fase 3 (planificación de la ejecución). Todavía no hay código de la aplicación: el repositorio contiene la documentación de planificación.

## Documentación

- [Plan de ejecución](repo_inicial/docs/plan-de-ejecucion.md)
- [Cronograma y diagrama de Gantt](repo_inicial/docs/cronograma/README.md)
- [Procedimiento de trabajo](repo_inicial/docs/procedimiento-de-trabajo.md)
- [Registro de riesgos](repo_inicial/docs/riesgos.md)
- [Decisiones](repo_inicial/docs/decisiones.md)
- [Seguimiento semanal](repo_inicial/docs/seguimiento.md)
- [Arquitectura preliminar](repo_inicial/docs/tecnica/arquitectura.md)

## Datos y seguridad

El proyecto usa solo datos ficticios. La configuración real (contraseñas de la base de datos) no se sube al repositorio.
