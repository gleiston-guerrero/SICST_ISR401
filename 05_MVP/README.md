# Producto Mínimo Viable — SICST

Esta carpeta contiene el **Producto Mínimo Viable (MVP)** del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**.

## Estado real del MVP

El MVP corresponde a un **prototipo web estático de demostración**, compuesto
por dos aplicaciones independientes:

- `SICST_Fisioterapeuta_APP/`
- `SICST_Paciente_APP/`

Las aplicaciones se ejecutan completamente en el navegador.

### Limitaciones técnicas actuales

La versión disponible en esta carpeta:

- **no dispone de backend**;
- **no utiliza una base de datos externa**;
- **no implementa autenticación real ni inicio de sesión**;
- **no implementa gestión real de usuarios, roles o permisos**;
- conserva los datos de demostración localmente mediante `localStorage`;
- utiliza datos iniciales ficticios de demostración;
- no mantiene sincronización entre la aplicación del fisioterapeuta y la del paciente;
- no envía notificaciones mediante servicios externos, correo, SMS o push;
- no ejecuta un modelo real de inteligencia artificial ni visión por computadora;
- no captura video real desde la cámara;
- no determina automáticamente si una repetición fue correcta o incorrecta.

Por tanto, el MVP se utiliza únicamente para demostrar flujos de interfaz,
persistencia local y comportamiento básico del prototipo. No debe presentarse
como un sistema clínico desplegado ni como una implementación completa de todos
los requisitos del ERS.

---

## Aplicación del fisioterapeuta

Ubicación:

```text
05_MVP/SICST_Fisioterapeuta_APP/
```

Archivos principales:

```text
index.html
css/styles.css
js/app.js
Fisioterapeuta.mp4
README.md
```

La aplicación permite demostrar localmente:

- registro y consulta de pacientes;
- registro de motivo de consulta;
- registro de dolor y fatiga;
- registro de rango de movimiento;
- selección de nivel de gravedad;
- catálogo local de ejercicios;
- asignación de rutinas;
- registro local de seguimiento;
- generación local de alertas a partir de valores registrados;
- visualización de gráficos y resúmenes;
- cambio de autorizaciones simuladas de privacidad;
- exportación local de datos de demostración.

Todas estas operaciones se ejecutan en el navegador y se almacenan mediante
`localStorage`.

### Lo que no implementa esta aplicación

La aplicación del fisioterapeuta no implementa:

- autenticación de usuarios;
- control de acceso real por roles;
- backend;
- API;
- base de datos centralizada;
- sincronización con la aplicación del paciente;
- envío real de notificaciones;
- procesamiento real de imágenes o video mediante IA.

---

## Aplicación del paciente

Ubicación:

```text
05_MVP/SICST_Paciente_APP/
```

Archivos principales:

```text
index.html
css/styles.css
js/app.js
Paciente.mp4
README.md
```

La aplicación permite demostrar localmente:

- consulta de rutinas de demostración;
- visualización de indicaciones textuales de ejercicios;
- inicio y finalización de una sesión local simulada;
- registro manual de dolor y fatiga;
- marcado manual de rutinas como completadas;
- visualización local del progreso;
- creación de recordatorios almacenados localmente;
- registro local de mensajes para revisión;
- cambio de autorizaciones simuladas de privacidad.

### Cámara simulada

La interfaz de ejercicio guiado contiene un elemento visual:

```text
div.camera-mock
```

que representa una cámara únicamente con fines de demostración.

La aplicación **no solicita acceso a una cámara física**, no utiliza
`getUserMedia`, no captura imágenes o video y no procesa movimiento real.

### Conteo de repeticiones

El conteo de repeticiones se realiza manualmente mediante el botón:

```text
Sumar repetición
```

Cada pulsación incrementa el contador local. Por tanto:

- no existe conteo automático por visión por computadora;
- no se verifica automáticamente la postura;
- no se determina si una repetición es correcta;
- no se rechazan automáticamente repeticiones incorrectas.

### Retroalimentación simulada

Los mensajes de retroalimentación mostrados durante el ejercicio son mensajes
predefinidos en JavaScript. No son el resultado de un modelo de IA ni de un
análisis real del movimiento del paciente.

---

## Ejecución local

Cada aplicación puede ejecutarse independientemente.

1. Abrir la carpeta correspondiente.
2. Abrir `index.html`.
3. Ejecutar con Live Server o abrir directamente el archivo en un navegador compatible.

No se requiere instalar dependencias externas para visualizar el prototipo.

---

## Persistencia de datos

Las dos aplicaciones utilizan `localStorage` del navegador.

Claves utilizadas actualmente:

```text
sicst_fisio_app_v2
sicst_paciente_app_v2
```

Los datos almacenados son locales al navegador y al dispositivo donde se
ejecuta cada aplicación.

Esto significa que:

- no existe una base de datos compartida;
- los datos no se sincronizan entre dispositivos;
- las dos aplicaciones no intercambian información mediante un servidor.

---

## Estado real de los requisitos Must en el MVP

La siguiente tabla documenta exclusivamente el estado observable en el código
actual del MVP. La condición de requisito `Must` proviene de la matriz de
trazabilidad vigente.

| RF | Requisito | Estado real en el MVP | Evidencia / limitación |
|---|---|---|---|
| RF-01 | Autenticar usuarios | **No implementado** | No existe pantalla ni lógica de autenticación real. |
| RF-02 | Gestionar roles y permisos | **No implementado** | Existen dos páginas separadas, pero no hay control de acceso ni permisos. |
| RF-03 | Registrar datos generales del paciente | **Implementado localmente** | Formulario de pacientes y persistencia en `localStorage`. |
| RF-04 | Registrar motivo de consulta | **Implementado localmente** | Campo de motivo de consulta/evaluación. |
| RF-06 | Clasificar condición clínica | **Parcial** | Se registran motivo y gravedad, pero no existe una clasificación clínica completa diferenciada. |
| RF-07 | Clasificar nivel de gravedad | **Implementado localmente** | Selector de gravedad en evaluación inicial. |
| RF-08 | Registrar signos vitales | **No implementado** | No existen campos funcionales para signos vitales en el MVP actual. |
| RF-09 | Registrar rangos de movimiento | **Implementado localmente** | Campo de rango de movimiento en evaluación. |
| RF-11 | Registrar nivel de dolor | **Implementado localmente** | Registro de dolor en evaluación, seguimiento y aplicación del paciente. |
| RF-12 | Registrar nivel de fatiga | **Implementado localmente** | Registro de fatiga en evaluación, seguimiento y aplicación del paciente. |
| RF-15 | Crear plan terapéutico personalizado | **Parcial** | Se pueden asignar rutinas, pero no existe una entidad completa de plan terapéutico con toda la lógica prevista en el ERS. |
| RF-16 | Gestionar catálogo de ejercicios | **Implementado localmente** | Alta, edición, eliminación, búsqueda y filtrado local de ejercicios. |
| RF-17 | Asignar rutina terapéutica | **Implementado localmente** | Formulario local de asignación de rutina. |
| RF-18 | Mostrar guías visuales | **Parcial** | Se muestran indicaciones textuales y una representación gráfica simple; no existe material audiovisual funcional asociado a cada ejercicio. |
| RF-19 | Iniciar sesión remota de ejercicios | **Parcial / simulada** | Existe temporizador y control local de sesión, pero no una sesión remota conectada con un backend. |
| RF-20 | Capturar movimiento con cámara | **No implementado** | La cámara es un `div` de simulación; no existe captura real. |
| RF-21 | Analizar movimiento del paciente | **No implementado** | No existe modelo de visión por computadora o análisis de movimiento. |
| RF-22 | Detectar errores de postura | **No implementado** | Los mensajes de postura son simulados y predefinidos. |
| RF-23 | Contar repeticiones correctas | **No implementado como requisito** | El contador aumenta manualmente al pulsar `Sumar repetición`; no determina corrección. |
| RF-24 | Rechazar repeticiones incorrectas | **No implementado** | No existe detección ni rechazo automático de repeticiones. |
| RF-26 | Registrar evidencia de cumplimiento | **Parcial** | Se puede seleccionar un tipo de evidencia como etiqueta, pero no se captura ni adjunta un archivo multimedia real. |
| RF-27 | Visualizar progreso terapéutico | **Implementado localmente** | Gráficos y resúmenes construidos a partir de datos locales de demostración. |

Esta tabla no constituye todavía el resultado de las pruebas de ejecución de
E2. La ejecución formal de casos de prueba, fecha, resultado y evidencia se
documentará separadamente.

---

## Funciones adicionales demostradas

El código también contiene funciones de demostración relacionadas con:

- alertas locales;
- reportes;
- recordatorios locales;
- autorización de cámara como estado booleano;
- autorización para compartir avance con familiar;
- mensajes de ayuda;
- gráficos de dolor, fatiga y cumplimiento.

La presencia de una interfaz o de un dato de demostración no se interpreta
automáticamente como cumplimiento completo de un requisito del ERS.

---

## Videos demostrativos

Los recorridos funcionales disponibles son:

```text
SICST_Fisioterapeuta_APP/Fisioterapeuta.mp4
SICST_Paciente_APP/Paciente.mp4
```

Los videos muestran el comportamiento del prototipo existente. No constituyen
evidencia de funcionalidades que no estén implementadas en el código.

---

## Trazabilidad

La matriz vigente del proyecto se encuentra en:

```text
04_Trazabilidad/Matriz_Trazabilidad_Final.csv
```

La clasificación de un requisito como `Must` no implica por sí sola que esté
implementado en el MVP. La cobertura del MVP debe distinguir entre:

- implementado;
- parcial o simulado;
- no implementado.

---

## Alcance académico

El MVP es un artefacto académico de demostración utilizado para visualizar
flujos y apoyar actividades de validación de requisitos.

No debe utilizarse para diagnóstico, tratamiento clínico, vigilancia médica ni
toma autónoma de decisiones terapéuticas.

Las funcionalidades simuladas se mantienen identificadas explícitamente para
evitar atribuir al prototipo capacidades que el código actual no posee.
